# 📈 AI-Powered Stock Market Assistant

An AI-powered stock market analysis application built using **LangChain**, **LangGraph**, **Groq LLM**, and **Streamlit**.

The application retrieves stock market data, analyzes technical indicators, and generates **Buy**, **Sell**, or **Hold** recommendations using an LLM-driven multi-agent workflow.

> **Disclaimer**
>
> This project is intended for educational and demonstration purposes only. It does **not** provide financial or investment advice.

---

## 🚀 Features

- 📊 Retrieve real-time or historical stock market data
- 📈 Calculate technical indicators:
  - Moving Average (5-day)
  - Moving Average (20-day)
  - Latest Closing Price
- 🤖 Generate AI-powered investment recommendations
- 💬 Provide natural language reasoning and justification
- 🔀 Multi-agent orchestration using LangGraph
- 🖥️ Interactive Streamlit web interface
- 📦 Structured JSON responses

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| LangChain | Prompt management and LLM integration |
| LangGraph | Multi-agent workflow orchestration |
| Groq LLM | High-speed LLM inference |
| Streamlit | Interactive web application |
| yfinance | Stock market data retrieval |
| Pandas | Data processing and analysis |

---

## 📂 Project Structure

```text
stock-assistant/
│
├── app.py
├── agents.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-stock-market-analysis.git
cd ai-stock-market-analysis
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the Environment File

Copy the example environment file:

**Linux/macOS**

```bash
cp .env.example .env
```

**Windows (PowerShell)**

```powershell
Copy-Item .env.example .env
```

### 5. Configure the Groq API Key

Add your API key to the `.env` file:

```text
GROQ_API_KEY=your_api_key_here
```

Alternatively, set it as an environment variable.

**Windows**

```cmd
set GROQ_API_KEY=your_api_key_here
```

**Linux/macOS**

```bash
export GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open your browser and navigate to:

```
http://localhost:8501
```

---

## 🔄 Application Workflow

```text
          User Input
               │
               ▼
     Fetch Stock Market Data
               │
               ▼
  Calculate Technical Indicators
               │
               ▼
     LangGraph Multi-Agent Flow
               │
               ▼
   LLM Recommendation Engine
               │
               ▼
      Explanation & Analysis
               │
               ▼
        Display Results
```

---

## 📊 Example Output

### Recommendation

```text
Buy
```

### Justification

```text
The 5-day moving average is above the 20-day moving average, indicating bullish momentum. The latest closing price also supports a positive short-term trend.
```

### Technical Indicators

```json
{
  "ma_5": 182.5,
  "ma_20": 175.2,
  "latest_price": 184.1
}
```

---

## 🔮 Future Enhancements

- 📰 Financial news integration using RAG
- 😊 Market sentiment analysis
- 💼 Portfolio tracking and management
- 📈 Additional technical indicators (RSI, MACD, Bollinger Bands)
- 📊 Multi-stock comparison
- 📄 PDF report generation
- 📉 Historical performance visualization

---

## 📜 License

This project is provided **for educational and demonstration purposes only**.

It is **not intended to provide financial or investment advice**. Users should conduct their own research and consult qualified financial professionals before making investment decisions.

---
```