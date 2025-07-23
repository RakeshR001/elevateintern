import streamlit as st
import requests
import smtplib
from email.message import EmailMessage
import datetime
import pandas as pd
import time

# Page setup
st.set_page_config(page_title="Crypto Price Tracker", layout="wide")
st.title("📈 Crypto Price Tracker (Auto-Tracking)")

# --- Session State Initialization ---
if 'prices' not in st.session_state:
    st.session_state.prices = []
if 'timestamps' not in st.session_state:
    st.session_state.timestamps = []

# --- Sidebar: Email Settings ---
st.sidebar.header("📧 Email Alert Settings")
EMAIL_SENDER = st.sidebar.text_input("Sender Email (Gmail)", value="", type="default")
EMAIL_PASSWORD = st.sidebar.text_input("App Password", value="", type="password")
EMAIL_RECEIVER = st.sidebar.text_input("Receiver Email", value="", type="default")

REFRESH_INTERVAL = st.sidebar.slider("Auto Refresh Interval (seconds)", 30, 300, 60)
ALERT_LOG = "alert_log.txt"

if st.sidebar.button("🔄 Reset Trend Data"):
    st.session_state.prices = []
    st.session_state.timestamps = []
    st.success("Tracking data has been reset.")

# --- Coin Selection & Thresholds ---
coins = st.multiselect("Select Cryptocurrencies", ["bitcoin", "ethereum", "dogecoin", "solana"], default=["bitcoin"])
currency = "inr"

thresholds = {}
for coin in coins:
    thresholds[coin] = st.number_input(f"Set alert price for {coin.capitalize()} (INR)", min_value=0.0, step=0.01)

# --- Fetch Prices ---
def fetch_prices():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return {coin: data[coin][currency] for coin in coins}
    except Exception as e:
        st.error(f"Error fetching prices: {e}")
        return {}

# --- Email Alert ---
def send_email_alert(coin, price, threshold):
    if not EMAIL_SENDER or not EMAIL_PASSWORD or not EMAIL_RECEIVER:
        st.warning("Please enter email credentials in the sidebar.")
        return

    msg = EmailMessage()
    msg['Subject'] = f"💰 {coin.capitalize()} Price Alert"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content(f"The price of {coin.capitalize()} is ₹{price}, which crossed your alert threshold of ₹{threshold}.")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        log_alert(coin, price)
        st.success(f"✅ Email sent for {coin} at INR{price}")
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
        with open(ALERT_LOG, "a") as f:
            f.write(f"{datetime.datetime.now()} - ERROR sending email for {coin}: {e}\n")

# --- Alert Logging ---
def log_alert(coin, price):
    with open(ALERT_LOG, "a") as f:
        f.write(f"{datetime.datetime.now()} - {coin} alert sent at price: INR{price}\n")

def load_alert_log():
    try:
        with open(ALERT_LOG, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No alerts sent yet."

# --- Main Auto-Tracking Logic ---
placeholder = st.empty()
with placeholder.container():
    current_prices = fetch_prices()
    if not current_prices:
        st.stop()

    now = datetime.datetime.now()
    st.session_state.timestamps.append(now)
    st.session_state.prices.append(current_prices)

    df = pd.DataFrame([current_prices])
    df.index = [now.strftime("%H:%M:%S")]
    st.dataframe(df.T.rename(columns={df.index[0]: 'Price (INR)'}))

    # Email Alerts
    for coin, price in current_prices.items():
        if price <= thresholds[coin] and price != 0:
            send_email_alert(coin, price, thresholds[coin])

    # Trend Line Chart
    if len(st.session_state.prices) > 1:
        st.subheader("📊 Price Trends")
        df_trend = pd.DataFrame(st.session_state.prices, index=st.session_state.timestamps)
        st.line_chart(df_trend)
    else:
        st.info("Waiting for more data to show trends...")

    # Log
    st.subheader("📬 Alert Log")
    st.text(load_alert_log())

    # Auto-refresh
    time.sleep(REFRESH_INTERVAL)
    st.rerun()