
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load("models/stock_price_model.pkl")
# Load historical stock data
stock_data = pd.read_csv(
    "dataset/tata_motors_pre_demerger.csv",
    parse_dates=["Date"]
)

# Page configuration
st.set_page_config(
    page_title="Tata Motors Stock Prediction",
    page_icon="📈",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}
</style>
""", unsafe_allow_html=True)

# Dashboard heading
st.title("📈 Tata Motors Stock Price Prediction")
st.write("Machine Learning Based Stock Analysis and Prediction System")
st.caption("Powered by Python, Scikit-learn and Linear Regression")

st.divider()

# Model performance
st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Mean Absolute Error", "₹9.96")

with col2:
    st.metric("Root Mean Squared Error", "₹13.36")

with col3:
    st.metric("R² Score", "0.8771")

st.caption("Performance metrics calculated on the test dataset.")

st.divider()

# Prediction section
st.subheader("🔮 Predict Next Trading Day Price")

st.write(
    "Enter the previous trading day's adjusted closing price "
    "to estimate the next trading day's adjusted closing price."
)

previous_close = st.number_input(
    "Previous Closing Price (₹)",
    min_value=0.01,
    value=400.0,
    step=1.0
)

if st.button("Predict Stock Price", type="primary"):

    input_data = pd.DataFrame(
        [[previous_close]],
        columns=["Previous Close"]
    )

    prediction = model.predict(input_data)[0]

    st.success("Prediction Generated Successfully!")

    st.metric(
        "Predicted Adjusted Closing Price",
        f"₹{prediction:.2f}",
        delta=f"₹{prediction - previous_close:.2f}"
    )

st.divider()

# About project

# Historical Stock Price Trend
st.divider()

st.subheader("📊 Historical Stock Price Trend")

st.write("Historical adjusted closing prices of Tata Motors.")

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(
    stock_data["Date"],
    stock_data["Adj Close"],
    label="Adjusted Closing Price"
)

ax.set_xlabel("Date")
ax.set_ylabel("Price (₹)")
ax.set_title("Tata Motors Historical Stock Price")
ax.legend()
ax.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

plt.close(fig)
st.subheader("About This Project")

st.write("""
This project uses historical Tata Motors stock data and a
Linear Regression algorithm to estimate the next trading
day's adjusted closing price using the previous day's price.
""")

st.info(
    "Educational project only. Predictions are estimates, "
    "not guaranteed market prices or investment advice."
)

st.caption("Stock Price Prediction | Machine Learning Minor Project")
