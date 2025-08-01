## 🔁 Data Science Workflow Flowchart – Brent Oil Price Project

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
| • Future real-time updates  |
| • Multi-CPD or VAR modeling |
+-----------------------------+
```
---
### 🧪 **1. Research and Development**

**Objective:** Understand the business context, research relevant models, and define analysis goals.

**Project-specific Actions:**

* Understand the main question: *How do political, economic, or geopolitical events impact Brent oil prices?*
* Read challenge documentation and references (Bayesian inference, PyMC3, MCMC, Change Point Detection).
* Study past major oil price shocks (e.g., Gulf War, COVID-19, 2022 Russia-Ukraine war, OPEC announcements).
* Define analysis goals:

  * Detect structural changes in oil prices.
  * Link these changes to real-world events.
  * Quantify impact.
* Identify suitable stakeholders (investors, energy companies, policymakers).

---

### 📥 **2. Data Collection and Preparation**

**Objective:** Acquire all relevant data and prepare it for analysis.

**Project-specific Actions:**

* Load the historical Brent oil price dataset (1987-05-20 to 2022-09-30).
* Research and compile **10–15 major events** that may have influenced oil prices.
* Create an **event dataset** (`events.csv`) with the following structure:

```csv
Event,Date,Description
"OPEC Production Cut",2020-04-12,"OPEC+ agreed on historic production cut during COVID-19"
"Russia-Ukraine War Begins",2022-02-24,"Invasion led to global energy supply concerns"
```

* Ensure **date format consistency** between datasets.
* Align event dates with the Brent price timeline for correlation analysis.

---

### 🧹 **3. Data Cleaning and Preprocessing**

**Objective:** Ensure high data quality and prepare for modeling.

**Project-specific Actions:**

* Convert `Date` column to `datetime` format.
* Sort records chronologically.
* Check and handle:

  * Missing values
  * Duplicates
  * Outliers (if any)
* Create new features:

  * **Log returns**: `log_return = log(price_t) - log(price_{t-1})` to stabilize variance.
  * Optional: Rolling mean, rolling std deviation (for volatility).
* Clean and format the event dataset (no typos, proper spacing, valid dates).

---

### 📊 **4. Exploratory Data Analysis (EDA)**

**Objective:** Visually and statistically explore patterns, trends, and anomalies.

**Project-specific Actions:**

* Plot Brent oil prices over time.
* Plot **log returns** to detect **volatility clustering**.
* Use **rolling averages** to highlight long-term trends.
* Overlay major events on price plots to **visually assess impacts**.
* Perform stationarity tests:

  * ADF (Augmented Dickey-Fuller)
  * KPSS (Kwiatkowski-Phillips-Schmidt-Shin)
* Highlight periods of extreme volatility, price drops, or jumps.

---

### 🧱 **5. Feature Engineering**

**Objective:** Create additional relevant variables for better modeling and analysis.

**Project-specific Actions:**

* Calculate:

  * Log returns
  * Rolling mean (e.g., 30-day moving average)
  * Rolling standard deviation (volatility)
* Encode event types (optional): e.g.,
  `event_type = { "war", "sanction", "OPEC decision", "pandemic", "economic crisis" }`
* Create lag features if needed (e.g., price lag, volatility lag).
* Binary indicators for whether an event occurred on a given date.

> ✅ **Note:** Feature engineering is minimal in change point analysis, but helpful for future model extensions or correlation exploration.

---

### 🔧 **6. Model Deployment**

**Objective:** Apply Bayesian Change Point Detection and deploy interactive insights.

**Project-specific Actions:**

#### A. **Modeling (using PyMC3)**

* Define a **Bayesian Change Point model**:

  * Set a **discrete uniform prior** over time for the change point `tau`.
  * Define two means: `mu_1` (before change), `mu_2` (after change).
  * Use `pm.math.switch()` to change behavior after `tau`.
  * Use `pm.Normal()` for likelihood.
  * Run `pm.sample()` to generate posterior samples via MCMC.

#### B. **Insight Generation**

* Identify most probable **change point dates**.
* Quantify change:

  * “Mean price shifted from \$X to \$Y”
  * “Volatility increased by Z%”
* Match change points to known events from the dataset.

#### C. **Dashboard Deployment (Flask + React)**

* Flask backend:

  * Serve API with model outputs (e.g., change points, summary stats).
  * Optionally include event-to-change-point mapping.
* React frontend:

  * Interactive time series visualization.
  * Highlight known events.
  * Allow users to explore price trends, zoom on change points, filter by date or event type.
* Use libraries like:

  * `Recharts`, `Chart.js`, or `D3.js` for graphs.
  * Axios or Fetch for API calls.

---

### 🛠️ **7. Model Monitoring and Maintenance**

**Objective:** Plan for long-term model improvement and system sustainability.

**Project-specific Actions:**

* Discuss potential extensions:

  * Multi-change-point detection
  * Use of **Markov Switching models** or **VAR models**
  * Integration of **macroeconomic indicators** (GDP, inflation, currency rates)
* Suggest pipeline for real-time oil price ingestion (e.g., from APIs like EIA).
* Highlight the importance of regular:

  * Model re-calibration
  * Dashboard updates
  * Stakeholder feedback loops
