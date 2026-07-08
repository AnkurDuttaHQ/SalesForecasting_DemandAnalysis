# 📈 Sales Forecasting & Demand Intelligence Dashboard

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?style=for-the-badge\&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-Forecasting-orange?style=for-the-badge)
![Prophet](https://img.shields.io/badge/Prophet-Time%20Series-purple?style=for-the-badge)

</p>

## 🚀 Live Demo

🌐 **Live Application:** https://salesforecasting01.streamlit.app/

📂 **GitHub Repository:** https://github.com/AnkurDuttaHQ/salesforecasting_demandanalysis

# 📖 Project Overview

Businesses rely on accurate sales forecasting to optimize inventory, reduce stock-outs, identify unusual sales behavior, and make informed decisions.

This project delivers an **end-to-end Sales Forecasting & Demand Intelligence System** that combines **Time Series Forecasting, Machine Learning, Anomaly Detection, Customer/Product Analytics, and Interactive Business Dashboards** into one unified application.

The dashboard enables business users to:

* 📊 Analyze historical sales performance
* 🔮 Forecast future sales
* 🚨 Detect unusual sales anomalies
* 📦 Identify product demand segments
* 📈 Support inventory planning and business decision-making

---

# ✨ Features

## 📊 Sales Overview Dashboard

* KPI Cards
* Total Sales by Year
* Monthly Sales Trend
* Interactive Region Filter
* Interactive Category Filter
* Sales by Region
* Sales by Category

---

## 🔮 Forecast Explorer

* Category-wise Forecast
* Region-wise Forecast
* 1–3 Month Forecast Horizon
* Interactive Forecast Visualization
* Model Performance Metrics
* MAE
* RMSE

Models Used

* Prophet
* XGBoost

---

## 🚨 Anomaly Detection

Detect abnormal sales patterns using:

* Isolation Forest
* Rolling Z-Score

Features

* Interactive anomaly chart
* Weekly anomaly report
* Detected anomaly dates
* Sales values of anomalies

---

## 📦 Product Demand Segmentation

K-Means Clustering based on

* Total Sales
* Growth Rate
* Sales Volatility
* Average Order Value

Features

* PCA Cluster Visualization
* Radar Chart Comparison
* Cluster-wise Business Interpretation
* Inventory Recommendations
* Download Cluster Report

---

# 🛠️ Tech Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost
* Prophet
* Isolation Forest
* K-Means Clustering
* PCA

### Visualization

* Plotly
* Matplotlib

### Web Application

* Streamlit

---

# 📂 Project Structure

```text
SalesForcasting_AnkurDuta
│
├── app.py
├── data/
├── pages/
├── utils/
├── models/
├── charts/
├── requirements.txt
└── analysis.ipynb
```

---

# 📈 Machine Learning Workflow

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Time Series Analysis
      │
      ▼
Forecasting
 (Prophet + XGBoost)
      │
      ▼
Anomaly Detection
      │
      ▼
Demand Segmentation
      │
      ▼
Interactive Dashboard
      │
      ▼
Deployment
```

---

# 💼 Business Value

This dashboard helps organizations to

* Improve inventory planning
* Reduce stock-outs
* Detect abnormal sales activity
* Understand product demand behavior
* Improve forecasting accuracy
* Make data-driven business decisions

---

# 🚧 Challenges Faced During Development

Building the dashboard involved several real-world engineering challenges beyond model development.

### 1. Time Series Data Preparation

**Challenge**

* Handling inconsistent date formats
* Creating weekly and monthly aggregated datasets

**Solution**

* Standardized datetime parsing
* Built reusable preprocessing pipeline

---

### 2. Forecasting Multiple Categories

**Challenge**

Generating separate forecasts for different product categories and business regions.

**Solution**

* Created independent forecasting datasets
* Built dynamic forecast selection inside the dashboard

---

### 3. Deployment Issues

One of the biggest challenges occurred during deployment.

**Problem**

After deploying the application, every dashboard page showed `FileNotFoundError` because local file paths worked on the development machine but failed on the cloud deployment.

**How it was solved**

* Reorganized the project structure
* Centralized file path management
* Updated data loading logic to use project-relative paths instead of relying on the current working directory
* Redeployed the application after validating the directory structure

This made the application portable and compatible with cloud deployment environments.

---

### 4. Multi-Page Dashboard Integration

**Challenge**

Managing multiple Streamlit pages while sharing datasets across the application.

**Solution**

* Modularized the codebase
* Created reusable utility functions
* Used caching for faster performance

---

# 📊 Future Improvements

* Deep Learning Forecasting (LSTM)
* Real-Time Sales Dashboard
* Cloud Database Integration
* User Authentication
* Automated Report Generation
* API Integration
* Live Business KPI Monitoring

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/AnkurDuttaHQ/salesforecasting_demandanalysis.git
```

Move into the project folder

```bash
cd SalesForcasting_AnkurDuta
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```
# 👨‍💻 Author

## Ankur Dutta

**AI & Machine Learning Engineer | Full Stack Developer | BCA (Hons) Student**

- 🎓 BCA (Hons), Adamas University
- 💻 Passionate about Machine Learning, Data Science, Generative AI, and Full Stack Development
- 🌐 Portfolio: https://ankurdev.in
- 💼 LinkedIn: https://www.linkedin.com/in/ankur-dutta/
- 📂 GitHub: https://github.com/AnkurDuttaHQ

---

⭐ **If you found this project helpful, please consider giving it a star!**
