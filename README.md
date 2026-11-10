# Tata Motors Stock Price Prediction

A Machine Learning Based Stock Analysis and Prediction System using Python, Scikit-learn, Linear Regression, and Streamlit.

## Project Overview

This project uses historical Tata Motors stock market data to build a machine learning model that estimates the next trading day's adjusted closing price.

The system uses a Linear Regression algorithm and provides an interactive dashboard where users can enter a previous closing price and view the predicted price.

## Objectives

- Collect and analyze historical Tata Motors stock data.
- Perform data preprocessing and feature engineering.
- Build a stock price prediction model using Linear Regression.
- Evaluate the model using standard regression metrics.
- Develop an interactive dashboard using Streamlit.

## Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib
- **Stock Data:** Yahoo Finance using yfinance
- **Dashboard:** Streamlit
- **Development Environment:** Jupyter Notebook and VS Code

## Dataset

Historical Tata Motors stock data was collected using Yahoo Finance through the `yfinance` Python library.

The dataset contains stock information such as:

- Date
- Open
- High
- Low
- Close
- Adjusted Close
- Volume

The data was downloaded using the Yahoo Finance ticker `TMPV.NS`.

**Data preparation note:** The modeling dataset was restricted to dates up to October 13, 2025, to avoid combining price observations across the Tata Motors corporate demerger-related price discontinuity. This is an educational preprocessing choice and does not establish that the resulting historical series is fully comparable across corporate actions.

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded historical stock data.
2. Handled the downloaded dataset's column structure.
3. Converted the date column into a usable date format.
4. Sorted the observations chronologically.
5. Restricted the modeling data to the period ending October 13, 2025.
6. Created a new feature called `Previous Close`.
7. Removed rows containing missing values created during feature engineering.

## Machine Learning Model

**Algorithm:** Linear Regression

The model uses the previous trading day's adjusted closing price (`Previous Close`) as the input feature to estimate the next trading day's adjusted closing price (`Adj Close`).

The dataset was divided chronologically:
- 80% for training
- 20% for testing

## Model Performance

The model was evaluated using the following metrics on the test dataset:

| Evaluation Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | ₹9.96 |
| Root Mean Squared Error (RMSE) | ₹13.36 |
| R² Score | 0.8771 |

These results describe the model's performance on the selected test dataset. They do not guarantee future prediction accuracy.

## Project Structure

```text
stock_price_prediction/
│
├── app.py
├── README.md
├── requirements.txt
│
├── dataset/
│   ├── tata_motors_stock_data.csv
│   └── tata_motors_pre_demerger.csv
│
├── graphs/
│
├── models/
│   └── stock_price_model.pkl
│
├── notebooks/
│   └── stock_prediction.ipynb
│
└── src/
```

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/marwan2627/tata-motors-stock-price-prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd stock_price_prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

## Dashboard Features

- Displays the project's machine learning model performance.
- Accepts a previous closing price as user input.
- Predicts an estimated next trading day's adjusted closing price.
- Displays historical adjusted closing price trends.
- Provides an interactive interface through Streamlit.

## Future Enhancements

- Include additional technical indicators as model features.
- Experiment with other regression and time-series models.
- Improve prediction evaluation using more robust validation methods.
- Incorporate updated stock market