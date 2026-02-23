from openai import OpenAI
import streamlit as st

client=OpenAI(api_key=st.secrets["open-ai-key"])
def generate_executive_summary(metrics_dict):
    prompt=f"""
    You are a senior business intelligence analyst.

    Based on the following KPIs and insights, write a concise executive summary.

    Data:
    {metrics_dict}

    Keep it strategic, concise, and action-oriented.
    """
    response=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system","content":"you are a strategic BI consultant."
            },
            {
                "role":"user","content":prompt
            }
        ]
        ,temperature=0.4
    )
    return response.choices[0].messages.content