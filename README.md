# ABIDS – Automated Business Intelligence & Decision System

An end-to-end analytics pipeline and interactive dashboard that processes transactional business data, detects profit leakage, and generates automated, actionable recommendations — built to cut manual reporting effort and speed up decision-making.

## Overview

ABIDS ingests raw transactional data, cleans and validates it, then surfaces KPIs, profitability trends, and hidden losses through a live Streamlit dashboard. It also uses an LLM-powered summarization layer to auto-generate executive summaries from the analytics — turning a dense report into a few readable sentences a decision-maker can act on immediately.

## Preview

![Dashboard Overview](screenshots/dashboard-overview.png)

![KPI Analysis](screenshots/kpi-analysis.png)

![Profit Leakage Detection](screenshots/profit-leakage.png)

## Key Results

- Processed **50,000+ transaction records**
- Reduced manual reporting effort by **~80%** through automated ingestion, validation, and cleaning
- Flagged high-revenue but loss-making products via custom profit leakage detection logic

## Features

- **Automated Data Pipeline** – ingestion, validation, and cleaning of raw transactional data
- **KPI Engine** – tracks revenue growth, profit margins, customer performance, and regional trends
- **Profit Leakage Detection** – identifies products that generate high revenue but low or negative margins, and flags discount-driven losses
- **Recommendation Engine** – maps insights to concrete business actions (e.g., discount optimization, regional focus)
- **Executive Dashboard** – live, interactive Streamlit dashboard for real-time monitoring
- **AI-Powered Summarization** – LLM-based report summarization with engineered prompts to auto-generate concise executive summaries

## Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Visualization/Dashboard:** Streamlit
- **Data Source:** Excel / CSV transactional records

## How to Run

```bash
# Clone the repository
git clone https://github.com/Altamash-Abbasi/ABIDS.git
cd ABIDS

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run Dashboard/app.py
```

## Future Improvements

- Add automated testing for the KPI and leakage-detection logic
- Support live database connections instead of static file uploads
- Extend recommendation engine with predictive forecasting

## Author

**Altamash Abbasi**
[LinkedIn](https://www.linkedin.com/in/altamashabbasi) · [GitHub](https://github.com/Altamash-Abbasi)
