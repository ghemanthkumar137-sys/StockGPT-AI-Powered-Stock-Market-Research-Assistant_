#  StockGPT – AI-Powered Stock Market Research Assistant

##  Overview

StockGPT is an AI-powered stock market research assistant that combines real-time financial data with Google's Gemini AI to provide intelligent stock analysis, investment insights, and interactive financial conversations.

Users can enter a stock symbol, view key financial metrics, analyze stock performance through visualizations, and ask natural-language questions about investment opportunities and market trends.

---

##  Problem Statement

Investors often spend significant time analyzing stock data from multiple platforms before making decisions.

Challenges include:

* Understanding financial metrics
* Interpreting stock performance
* Evaluating investment risks
* Accessing reliable market insights

StockGPT simplifies this process through AI-powered analysis and real-time market data.

---

##  Solution

StockGPT integrates:

* Real-time stock market data
* Interactive financial dashboards
* Generative AI-powered analysis
* Conversational investment guidance

This enables users to perform stock research efficiently using natural language.

---

##  Features

###  Real-Time Stock Information

* Current stock price
* Market capitalization
* P/E ratio
* Company information

###  Stock Performance Visualization

* Historical stock price trends
* Interactive charts
* Performance tracking

###  Gemini AI Financial Assistant

* Stock analysis
* Investment insights
* Risk assessment
* Financial explanations

###  Conversational Interface

* Natural language interaction
* Context-aware responses
* Chat history support

###  Modern Dashboard

* Responsive Streamlit UI
* Financial market-themed design
* User-friendly experience

---

##  System Architecture

User Input
│
▼
Stock Symbol Selection
│
▼
Yahoo Finance API
│
▼
Stock Data Retrieval
│
▼
Financial Metrics & Charts
│
▼
Gemini AI Analysis
│
▼
Investment Insights
│
▼
Streamlit Dashboard

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frontend

* Streamlit

### Generative AI

* Google Gemini 2.5 Flash

### Financial Data

* Yahoo Finance (yfinance)

### Libraries

* LangChain Google GenAI
* Pandas
* yfinance
* Python Dotenv

---

##  Project Structure

StockGPT/

├── app.py

├── requirements.txt

├── assets/

│   └── stock_market_banner.jpg

├── .gitignore

└── README.md

---

##  Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/StockGPT.git
cd StockGPT
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

##  Run Application

```bash
streamlit run app.py
```

---

## 📸 Application Preview

### Dashboard

(Add screenshot here)

### Stock Trend Analysis

(Add screenshot here)

### AI Investment Chat

(Add screenshot here)

---

## 📈 Example Questions

* Is TCS a good long-term investment?
* Explain the company's P/E ratio.
* What are the major risks associated with this stock?
* Analyze the recent stock performance.
* Compare growth potential and valuation.

---

## 🎓 Skills Demonstrated

### Generative AI

* Prompt Engineering
* Gemini API Integration
* Conversational AI Development

### Financial Analytics

* Stock Market Analysis
* Investment Research
* Financial Metrics Interpretation

### Data Engineering

* API Integration
* Real-Time Data Processing
* Data Visualization

### Application Development

* Streamlit Dashboard Development
* Interactive User Interfaces
* Session State Management

---

##  Future Enhancements

* Portfolio Analysis
* Multi-Stock Comparison
* News Sentiment Analysis
* Technical Indicators
* Earnings Report Analysis
* AI-Powered Stock Recommendations
* RAG-Based Financial Research System

---

##  Business Impact

StockGPT helps investors, analysts, and finance enthusiasts quickly access market information, understand stock performance, and make informed investment decisions using AI-powered insights.

---

##  Author

**Hemanth Kumar**

Aspiring Data Scientist | Machine Learning Engineer | Generative AI Enthusiast

---

⭐ If you found this project useful, consider giving the repository a star.
