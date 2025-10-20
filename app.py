import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Life Below Water", layout="wide")

# Load CSS file (styles.css should be in the same folder)
css_path = Path(__file__).with_name("styles.css")
if css_path.exists():
    css = css_path.read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
else:
    # fallback inline style if styles.css is missing
    st.markdown(
"""
<style>
[data-testid="stAppViewContainer"]{min-height:100vh; background: linear-gradient(180deg,#a8edea,#1f8ef1);}
.center-container{min-height:70vh; display:flex; justify-content:center; align-items:center;}
div.stButton > button{background: linear-gradient(180deg,#3da0ff,#005bb5); color: white; border-radius:10px; padding:12px 28px; font-size:18px; margin:0 12px; box-shadow:0 6px 18px rgba(0,0,0,0.15);}
div.stButton > button:hover{transform:translateY(-2px);}
</style>
""",
unsafe_allow_html=True,
)
    
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"❌ CSS file not found: {file_name}")

# Load the CSS
local_css("styles.css")

st.markdown('<h1 class="main-heading">WHERE WE ARE</h1>', unsafe_allow_html=True)

with open("img/image.png", "rb") as f:
    data = f.read()
encoded = base64.b64encode(data).decode()

st.markdown(f"""
<div style="text-align:center; margin-top:30px;">
    <img src="data:image/png;base64,{encoded}" style="width:400px; border-radius:12px;"/>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">
    <button class="main-buttons">&#8592;</button>
    <button class="main-buttons"><span>&#9776;</span></button>
    <button class="main-buttons">&#8594;</button>
</div>
""", unsafe_allow_html=True)

# # Create three columns so the buttons sit side-by-side and are centered
# col1, col2, col3 = st.columns([1,1,1])
# with col1:
#     if st.button("<"):
#         st.info("Previous clicked")


# with col2:
#     if st.button("stats"):
#         st.success("Stats clicked")


# with col3:
#     if st.button(">"):
#         st.info("Next clicked")

