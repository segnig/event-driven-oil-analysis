# 📊 Brent Oil Price Analysis Dashboard

A modern dashboard built with **React**, **TypeScript**, and **Vite** for interactive exploration of Brent oil prices, volatility, and major market events.

---

## 🚀 Features

- **📅 Date Range Filtering:**
  - Select start and end dates to filter the time series data displayed.

- **📈 Data Visualization:**
  - Line chart of daily Brent oil prices and log returns (volatility).
  - Key events are marked with vertical lines and labels.
  - Bayesian changepoint periods are highlighted with shaded regions and descriptions.

- **🔗 API Integration:**
  - Fetches price data, event data, and changepoint analysis from a Flask backend.

- **📝 Summary Card:**
  - Displays key findings, such as detected volatility shifts and their timing (e.g., during the 2008 Global Financial Crisis).

---

## 🛠️ Technologies Used

- ⚛️ React, TypeScript, Vite
- 📊 recharts (for charting)
- 📆 react-datepicker (for date selection)
- 🔗 axios (for API requests)
- 🐍 Flask backend (for data serving)

---

## 📦 How It Works

1. **Select a date range** to filter the data.
2. **View interactive charts** showing price and volatility, with key events and changepoint periods highlighted.
3. **Read summary insights** about market regime shifts and volatility transitions.

---

## 🖥️ Quick Start

1. Start the Flask backend server.
2. Run the React frontend with Vite.
3. Open the dashboard in your browser and explore!

---

## 💡 Example Insight

> A **Daily Volatility Increase** of **57.89%** was detected during the transition period from 2008-05-19 to 2008-08-21, coinciding with the build-up to the 2008 Global Financial Crisis.

---
