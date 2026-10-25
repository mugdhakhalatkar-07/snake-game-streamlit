
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Snake Game",
    page_icon="🐍",
    layout="centered"
)

st.title("🐍 Snake Game")
st.write("Use your keyboard arrow keys to control the snake!")

game_file = Path(__file__).parent / "game.html"

if game_file.exists():
    html_code = game_file.read_text(encoding="utf-8")
    components.html(html_code, height=600, scrolling=False)
else:
    st.info("Your game is almost ready! We are setting it up.")
