# Event Driven Oil Analysis

## Overview

This project analyzes how major geopolitical and economic events impact **Brent crude oil prices** over time by detecting statistically significant change points in the price series. Using a **Bayesian Change Point Detection** model implemented with **PyMC3**, we identify structural breaks in the oil price trends and link them to key events like OPEC decisions, wars, sanctions, and pandemics. The insights support investors, policymakers, and energy companies in making informed decisions.

---

## Project Goals

* Detect significant structural changes (change points) in Brent oil prices from 1987 to 2022.
* Associate detected change points with major geopolitical and economic events.
* Quantify the magnitude and impact of these shifts.
* Build an interactive dashboard for stakeholders to explore price changes and event correlations.

---

## Data

* **Brent Oil Price Data:** Daily prices from May 20, 1987 to September 30, 2022 (USD per barrel).
* **Event Dataset:** A curated list of major events (e.g., OPEC meetings, wars, economic crises) with dates and descriptions.

---

## Methodology

1. **Data Preparation**

   * Convert dates to datetime format
   * Calculate log returns to stabilize variance
   * Clean data: handle missing values and duplicates

2. **Exploratory Data Analysis (EDA)**

   * Plot price trends and log returns
   * Perform stationarity tests (ADF, KPSS)
   * Overlay key events on price timeline

3. **Bayesian Change Point Detection**

   * Model a discrete change point (tau) with a uniform prior
   * Define separate means before and after tau
   * Use PyMC3 and MCMC sampling for posterior inference
   * Identify probable change points and estimate price regime shifts

4. **Insight Generation**

   * Map change points to known events
   * Quantify changes in mean price and volatility
   * Generate probabilistic statements on regime changes

5. **Dashboard Development**

   * Backend with Flask serving model outputs and event data via API
   * Frontend with React offering interactive visualizations, filters, and event highlights

---

## Assumptions & Limitations

* **Assumptions:**

  * Major events can cause immediate or delayed impacts on oil prices.
  * Brent prices are driven mainly by external geopolitical and macroeconomic factors.
  * Price series exhibits regime shifts modeled as stochastic processes.

* **Limitations:**

  * Correlation does not imply causation — detected change points may not be caused by identified events.
  * Some changes may be due to market speculation or data noise.
  * Analysis uses only price data without other economic indicators, possibly missing broader context.

---

## How to Use This Repository

* `data/` contains the Brent price data and event list CSV files.
* `notebooks/` contains EDA and modeling Jupyter notebooks.
* `model/` includes PyMC3 Bayesian Change Point Detection implementation.
* `dashboard/` has Flask backend and React frontend source code.

---

## Getting Started

### Setup

```bash
# Clone repo
git clone https://github.com/segnig/event-driven-oil-analysis.git
cd event-driven-oil-analysis

# Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # Unix
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### Run the Model

```bash
python model/change_point_model.py
```

### Start the Dashboard

```bash
cd dashboard/backend
flask run
```

In a separate terminal:

```bash
cd dashboard/frontend
npm install
npm start
```

Open `http://localhost:3000` to explore the dashboard.

---

## Future Work

* Extend to detect multiple change points.
* Integrate macroeconomic variables (GDP, inflation, exchange rates).
* Add real-time data ingestion and automated event detection.
* Explore advanced models (Markov Switching, VAR).

---

## References

* Bayesian Change Point Detection with PyMC3: [https://docs.pymc.io/en/stable/](https://docs.pymc.io/en/stable/)
* Data Science Workflow: [https://www.datascience-pm.com/data-science-workflow/](https://www.datascience-pm.com/data-science-workflow/)
* Change Point Detection tutorials: [https://forecastegy.com/posts/change-point-detection-time-series-python/](https://forecastegy.com/posts/change-point-detection-time-series-python/)
* Historical Brent oil price sources: EIA, Yahoo Finance

---

## Contact

Created by Segni Girma
Email: [segnigirma11@gmail.com](mailto:segnigirma11@gmail.com)