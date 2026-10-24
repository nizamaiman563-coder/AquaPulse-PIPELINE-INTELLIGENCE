"""AquaPulse — Streamlit wrapper around a responsive, interactive HTML dashboard.

Run: python -m streamlit run app.py
The included UI is intentionally self-contained and uses SIMULATED data.
Replace the JavaScript simulation with your real pipeline inputs when ready.
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AquaPulse | Pipeline Intelligence",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"],
      [data-testid="stMain"] {background:#041426!important;}
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], footer, #MainMenu {display:none!important;}
      [data-testid="stMainBlockContainer"], .block-container {
        max-width:100%!important; padding:0!important; margin:0!important;
      }
      [data-testid="stVerticalBlock"] {gap:0!important;}
      [data-testid="stElementContainer"] {width:100%!important;}
      iframe[title="streamlit.components.v1.html"] {
        width:100%!important; display:block!important; border:0!important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_file = Path(__file__).with_name("aquapulse_dashboard.html")
if not html_file.is_file():
    st.error("Missing aquapulse_dashboard.html. Keep it in the same folder as app.py.")
    st.stop()
components.html(html_file.read_text(encoding="utf-8"), height=955, scrolling=True)
