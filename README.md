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
