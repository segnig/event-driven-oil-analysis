import os
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_all_wikitables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    all_tables = soup.find_all("table", class_="wikitable")

    if not all_tables:
        print(f"No tables found at {url}")
        return [], []

    all_data = []
    final_headers = []

    for table in all_tables:
        headers = [th.text.strip() for th in table.find_all("th")]
        if "Year" not in headers:
            headers = ["Year"] + headers

        rows = []
        current_year = "0000"

        for row in table.find_all("tr")[1:]:  # skip header row
            cols = row.find_all(["td", "th"])

            # Clean text and remove bracketed footnotes
            row_data = [re.sub(r"\[.*?\]", "", col.text.strip().replace("\xa0", " ")) for col in cols]

            if not row_data:
                continue
            if len(row_data) == len(headers) - 1:
                row_data.insert(0, current_year)
            elif len(row_data) == len(headers):
                current_year = row_data[0]
            else:
                print(f"Skipping row with unexpected column count: {row_data}")
                continue

            rows.append(row_data)

        all_data.extend(rows)
        final_headers = headers

    return all_data, final_headers

def try_parse_date(date_str):
    for fmt in ("%d %B %Y", "%B %d %Y", "%B %Y"):
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    return pd.NaT

def clean_and_save_data(data, headers, output_csv_file):
    if not data or not headers:
        print(f"Skipping save for {output_csv_file} due to empty data.")
        return pd.DataFrame()

    df = pd.DataFrame(data, columns=headers)

    if "Date" not in df.columns or "Year" not in df.columns:
        print(f"Required columns not found in {output_csv_file}. Found: {df.columns}")
        return pd.DataFrame()

    # Drop empty rows and columns
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # Filter rows with incomplete date strings (expecting two words: '1 July')
    df["bad_rows"] = df["Date"].apply(lambda x: len(x.split()) == 2 if isinstance(x, str) else False)
    df = df[df["bad_rows"]]

    # Combine with Year and parse as datetime
    df["Date"] = df["Date"] + " " + df["Year"]
    df["Date"] = df["Date"].apply(try_parse_date)

    # Drop rows with unparseable dates
    df.dropna(subset=["Date"], inplace=True)

    df.drop(columns=["bad_rows", "Year"], inplace=True)

    # Save to CSV
    df.to_csv(output_csv_file, index=False)
    print(f"Saved cleaned data to {output_csv_file} with shape {df.shape}")
    return df

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    # Scrape and clean 2000–present
    all_data, final_headers = scrape_all_wikitables(
        url="https://en.wikipedia.org/wiki/Timeline_of_geopolitical_changes_(2000%E2%80%93present)"
    )
    df_2000_present = clean_and_save_data(
        data=all_data,
        headers=final_headers,
        output_csv_file="data/geopolitical_2000-present.csv"
    )

    # Scrape and clean 1900–1999
    all_data, final_headers = scrape_all_wikitables(
        url="https://en.wikipedia.org/wiki/Timeline_of_geopolitical_changes_(1900%E2%80%931999)"
    )
    df_1900_1999 = clean_and_save_data(
        data=all_data,
        headers=final_headers,
        output_csv_file="data/geopolitical_1900-1999.csv"
    )

    # Combine and save final dataset
    df = pd.concat([df_1900_1999, df_2000_present], ignore_index=True)
    df.to_csv("data/geopolitical_changes.csv", index=False)
    print("Combined dataset saved.")
    print("Final shape:", df.shape)
