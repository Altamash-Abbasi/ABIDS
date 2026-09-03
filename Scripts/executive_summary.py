import google.generativeai as genai
import streamlit as st
import os

api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

def generate_executive_summary(metrics_dict):
    prompt = f"""
    You are a senior business intelligence analyst.

    Based on the following KPIs and insights, write a concise executive summary.

    Data:
    {metrics_dict}

    Keep it strategic, concise, and action-oriented.
    """

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction="you are a strategic BI consultant."
    )

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.4
        )
    )

    return response.text