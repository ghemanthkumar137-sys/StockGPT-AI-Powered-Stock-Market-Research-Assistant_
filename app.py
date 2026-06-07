from dotenv import load_dotenv
import os
import streamlit as st
import yfinance as yf
import base64

from langchain_google_genai import ChatGoogleGenerativeAI

# =========================
# Load Environment Variables
# =========================
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# =========================
# Check API Key
# =========================
if not GOOGLE_API_KEY:
    st.error("Google API Key not found")
    st.stop()

# =========================
# Streamlit Page Config
# =========================
st.set_page_config(
    page_title="StockGPT",
    page_icon="📈",
    layout="wide"
)

# =========================
# Function to Load Background Image
# =========================
def get_base64_image(image_path):

    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode()

# =========================
# Load Background Image
# =========================
background_image = get_base64_image("stock.jpeg.jpeg")

# =========================
# Custom CSS
# =========================
st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpeg;base64,{background_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }}

    .main {{
        background: rgba(0, 0, 0, 0.7);
        border-radius: 15px;
        padding: 20px;
    }}

    .title {{
        font-size: 48px;
        font-weight: bold;
        color: #00FFAA;
        text-align: center;
        text-shadow: 2px 2px 8px black;
    }}

    .subtitle {{
        text-align: center;
        color: #FFFFFF;
        margin-bottom: 30px;
        font-size: 22px;
        text-shadow: 1px 1px 5px black;
    }}

    section[data-testid="stSidebar"] {{
        background-color: rgba(17, 24, 39, 0.95);
    }}

    .stChatMessage {{
        background-color: rgba(0, 0, 0, 0.65);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }}

    div[data-testid="metric-container"] {{
        background-color: rgba(0, 0, 0, 0.65);
        border: 1px solid #00FFAA;
        padding: 15px;
        border-radius: 10px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# Title
# =========================
st.markdown(
    '<p class="title">📈 StockGPT</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">AI Powered Stock Market Research Assistant</p>',
    unsafe_allow_html=True
)

# =========================
# Sidebar
# =========================
st.sidebar.title("📊 Stock Settings")

stock_symbol = st.sidebar.text_input(
    "Enter Stock Symbol",
    value="TCS"
)

# Automatically Add NSE Extension
if ".NS" not in stock_symbol and ".BO" not in stock_symbol:
    stock_symbol = stock_symbol + ".NS"

investment_type = st.sidebar.selectbox(
    "Investment Type",
    [
        "Short Term",
        "Long Term",
        "High Risk",
        "Low Risk"
    ]
)

# =========================
# Clear Chat Button
# =========================
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# =========================
# Fetch Stock Data
# =========================
try:

    stock = yf.Ticker(stock_symbol)

    stock_info = stock.info

    current_price = stock_info.get("currentPrice", "N/A")
    market_cap = stock_info.get("marketCap", "N/A")
    pe_ratio = stock_info.get("trailingPE", "N/A")
    company_name = stock_info.get("longName", stock_symbol)

    # Historical Data
    hist = stock.history(period="6mo")

except Exception as e:

    st.error(f"Error Fetching Stock Data: {e}")

    current_price = "N/A"
    market_cap = "N/A"
    pe_ratio = "N/A"
    company_name = stock_symbol
    hist = None

# =========================
# Display Stock Information
# =========================
st.subheader(f"📌 {company_name}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current Price",
        current_price
    )

with col2:
    st.metric(
        "Market Cap",
        market_cap
    )

with col3:
    st.metric(
        "P/E Ratio",
        pe_ratio
    )

# =========================
# Display Stock Chart
# =========================
if hist is not None and not hist.empty:

    st.subheader("📉 Stock Price Trend")

    st.line_chart(hist["Close"])

# =========================
# Gemini Model
# =========================
model = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY,
    model="gemini-2.5-flash",
    temperature=0.7
)

# =========================
# Initialize Chat History
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Display Previous Messages
# =========================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================
# Chat Input
# =========================
user_input = st.chat_input(
    "Ask stock market questions..."
)

# =========================
# User Conversation
# =========================
if user_input:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant Response
    with st.chat_message("assistant"):

        with st.spinner("📊 StockGPT is analyzing the market..."):

            try:

                # Conversation History
                conversation_history = ""

                for msg in st.session_state.messages:

                    conversation_history += (
                        f"{msg['role']}: {msg['content']}\n"
                    )

                # Final Prompt
                final_prompt = f"""
You are StockGPT, an AI-powered Stock Market Research Assistant.

Stock Information:
- Company Name: {company_name}
- Stock Symbol: {stock_symbol}
- Current Price: {current_price}
- Market Cap: {market_cap}
- P/E Ratio: {pe_ratio}

Investment Type:
{investment_type}

Conversation History:
{conversation_history}

Current User Question:
{user_input}

Instructions:
- Give educational financial insights
- Explain stock performance clearly
- Mention risks when needed
- Suggest investment ideas professionally
- Be conversational and intelligent
- Avoid financial guarantees
"""

                # Gemini Response
                response = model.invoke(final_prompt)

                ai_response = response.content

                # Display AI Response
                st.markdown(ai_response)

                # Save AI Response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": ai_response
                    }
                )

            except Exception as e:

                st.error(f"Error: {e}")

# =========================
# Footer
# =========================
st.markdown("---")

st.markdown(
    """
    <center>
    <h4>Made with ❤️ </h4>
    </center>
    """,
    unsafe_allow_html=True
)