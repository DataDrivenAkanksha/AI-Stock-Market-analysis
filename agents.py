from langgraph.graph import StateGraph, END
from typing import TypedDict
import yfinance as yf
import pandas as pd

from langchain_groq import ChatGroq
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


# -----------------------------
# State Definition
# -----------------------------

class StockState(TypedDict):
    symbol: str
    data: pd.DataFrame
    analysis: dict
    recommendation: str
    justification: str


# -----------------------------
# Fetch Stock Data Agent
# -----------------------------

def fetch_data(state: StockState) -> StockState:

    ticker = yf.Ticker(state["symbol"])
    hist = ticker.history(period="1y", interval="1d")

    state["data"] = hist

    return state


# -----------------------------
# Technical Analysis Agent
# -----------------------------

def analyze_data(state: StockState) -> StockState:

    df = state["data"]

    close_prices = df["Close"]

    state["analysis"] = {
        "ma_5": float(close_prices.tail(5).mean()),
        "ma_20": float(close_prices.tail(20).mean())
        if len(close_prices) >= 20 else None,
        "latest": float(close_prices.iloc[-1])
    }

    return state


# -----------------------------
# Structured LLM Output
# -----------------------------

class StockAdvice(BaseModel):

    recommendation: str
    justification: str



# -----------------------------
# Groq LLM
# -----------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


structured_llm = llm.with_structured_output(
    StockAdvice
)


# -----------------------------
# Recommendation Agent
# -----------------------------

def recommend(state: StockState) -> StockState:

    prompt = f"""
You are a stock market analysis assistant.

Analyze the stock using these indicators:

Stock Symbol:
{state["symbol"]}

Indicators:
{state["analysis"]}


Provide:
1. Recommendation:
   - Buy
   - Sell
   - Hold

2. Short justification based only on the indicators.

Do not provide code.
Do not provide markdown.
"""


    try:

        response = structured_llm.invoke(prompt)

        state["recommendation"] = response.recommendation
        state["justification"] = response.justification


    except Exception as e:

        state["recommendation"] = "Hold"
        state["justification"] = (
            f"Unable to generate AI recommendation: {str(e)}"
        )


    return state



# -----------------------------
# Explanation Agent
# -----------------------------

def explain(state: StockState) -> StockState:

    return state



# -----------------------------
# LangGraph Workflow
# -----------------------------

graph = StateGraph(StockState)


graph.add_node(
    "fetch",
    fetch_data
)

graph.add_node(
    "analyze",
    analyze_data
)

graph.add_node(
    "recommend",
    recommend
)

graph.add_node(
    "explain",
    explain
)



graph.set_entry_point("fetch")


graph.add_edge(
    "fetch",
    "analyze"
)


graph.add_edge(
    "analyze",
    "recommend"
)



# Only explain Buy/Sell decisions
def should_explain(state: StockState) -> str:

    if state["recommendation"] != "Hold":
        return "explain"

    return END



graph.add_conditional_edges(
    "recommend",
    should_explain,
    {
        "explain": "explain",
        END: END
    }
)


# Compile LangGraph application

app = graph.compile()