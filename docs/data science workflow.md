# 📘 **Brent Crude Oil Price Change Point Detection Project**

**A Bayesian Time Series Analysis Framework**

---

## 🧭 **1. Research and Development**

### 🎯 Objective

To understand how political, economic, and geopolitical events impact Brent crude oil prices by detecting structural shifts (change points) in the price time series.

### 📚 Research Focus

* Studied change point detection methods: **Bayesian inference**, **MCMC**, and **PyMC3**
* Reviewed historical oil price disruptions (e.g., Gulf War, COVID-19, Russia-Ukraine conflict, OPEC meetings)
* Defined analysis goals:

  * Detect **structural breaks** in oil price time series
  * Link them to **real-world events**
  * **Quantify** the impact of each shift
* Identified key stakeholders:

  * **Investors** (for risk management)
  * **Energy companies** (for strategic planning)
  * **Policymakers** (for economic forecasting)

---

## 📥 **2. Data Collection and Preparation**

### 🗃️ Brent Oil Price Data

* Historical daily Brent crude prices:
  `1987-05-20` to `2022-09-30`
* Source: Public financial datasets (e.g., EIA, Yahoo Finance)

### 🌍 Event Dataset

Manually collected 10–15 major geopolitical or macroeconomic events affecting oil prices. Stored in `events.csv`:

| Event                     | Date       | Description                                        |
| ------------------------- | ---------- | -------------------------------------------------- |
| OPEC Production Cut       | 2020-04-12 | Historic production cut during COVID-19            |
| Russia-Ukraine War Begins | 2022-02-24 | Invasion caused global energy supply disruption    |
| Gulf War Begins           | 1990-08-02 | Iraq invades Kuwait, driving a spike in oil prices |
| COVID-19 Pandemic         | 2020-03-11 | WHO declares pandemic; global demand crashes       |

* Ensured date format consistency
* Mapped events to Brent oil timeline

---

## 🧹 **3. Data Cleaning and Preprocessing**

### 🛠️ Key Steps

* Converted date columns to `datetime` objects
* Sorted data chronologically
* Removed:

  * Missing values
  * Duplicate records
* Created new features:

  * **Log returns**:

    $$
    r_t = \log(\text{price}_t) - \log(\text{price}_{t-1})
    $$
  * Optional: 30-day rolling mean and volatility for trend and noise analysis

---

## 📊 **4. Exploratory Data Analysis (EDA)**

### 🔍 Visual & Statistical Insights

* **Price trends** over time to spot growth, crashes, recoveries
* **Log returns** to detect **volatility clustering**
* Rolling window plots to observe medium-term volatility and regime shifts
* **Event overlays**: Plotted key geopolitical events on price chart
* **Stationarity testing**:

  * ADF (Augmented Dickey-Fuller)
  * KPSS (to validate ADF results)

> EDA confirmed that Brent oil prices exhibit **non-stationarity** and **structural volatility shifts** aligned with known events.

---

## 🧱 **5. Feature Engineering**

### 🔧 Key Features Created

* **Log returns** (main input for Bayesian model)
* **Rolling averages** and **volatility windows** (optional for visualization)
* Binary **event indicators** (for timeline overlays)
* Optional event type encodings:

  * `"war"`, `"pandemic"`, `"OPEC"`, `"economic crisis"`

> 🔍 Note: Feature engineering is minimal in change point detection but may support correlation insights or model extensions later.

---

## 📈 **6. Model Deployment**

### 🔬 A. Bayesian Change Point Detection (via PyMC3)

#### Model Design:

* Prior: Uniform discrete prior over change point location (`tau`)
* Likelihood: Normal distribution of returns with different means/volatilities before and after `tau`
* Use `pm.math.switch()` to create regime behavior:

  ```python
  mu = pm.math.switch(tau >= idx, mu1, mu2)
  ```
* Posterior sampling via MCMC (`pm.sample()`)

#### Output:

* Estimated change point locations
* Pre- and post-change mean/volatility
* Probabilistic confidence intervals

---

### 📉 B. Insight Generation

#### Interpreting Results:

* Pinpointed key change dates
* Quantified change magnitudes (mean price shift, volatility change)
* Mapped change points to known real-world events
* Created annotated timeline (interactive in dashboard)

---

### 🌐 C. Deployment (Flask + React)

#### Backend (Flask):

* Serves:

  * JSON API of model outputs
  * List of change points and associated event metadata

#### Frontend (React):

* Features:

  * Interactive time series plot
  * Zoom, date filtering, change point highlights
  * Event overlays with tooltips

#### Libraries:

* `Recharts`, `Chart.js`, `Plotly`
* `Axios` for API calls

---

## 🛠️ **7. Model Monitoring & Maintenance**

### 🧩 Extensions & Future Work:

* Detect **multiple change points** with full Bayesian segmentation
* Try **Markov Switching Models** for better time-dependency modeling
* Integrate external indicators:

  * GDP, inflation, interest rates, USD index
* Enable **real-time updates** using Brent price APIs
* Automate:

  * Monthly model retraining
  * Event detection using NLP (from news feeds)

---

## 🔁 Summary: End-to-End Workflow Flowchart

```text
+-----------------------------+
| 1. Research & Development   |
+-----------------------------+
            |
            v
+-----------------------------+
| 2. Data Collection & Prep   |
| • Load Brent price data     |
| • Collect 10–15 key events  |
+-----------------------------+
            |
            v
+-----------------------------+
| 3. Data Cleaning & Preproc  |
| • Convert dates             |
| • Compute log returns       |
| • Remove nulls/duplicates   |
+-----------------------------+
            |
            v
+-----------------------------+
| 4. Exploratory Data Analysis|
| • Plot prices & returns     |
| • Stationarity checks (ADF) |
| • Overlay events on timeline|
+-----------------------------+
            |
            v
+-----------------------------+
| 5. Feature Engineering      |
| • Volatility indicators     |
| • Event encodings (optional)|
+-----------------------------+
            |
            v
+-----------------------------+
| 6. Model Deployment         |
| • PyMC3 Bayesian model      |
| • Flask API backend         |
| • React dashboard frontend  |
+-----------------------------+
            |
            v
+-----------------------------+
| 7. Monitoring & Maintenance |
| • Real-time updates         |
| • Multi-CPD or VAR modeling |
+-----------------------------+
```