import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage",page_icon = ":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
         return None
    return r.json()

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css(r'style\style.css')
## Where to find lottie aninmations ----   https://lottiefiles.com/search?q=oil+and+gas&category=animations
# Load Assets
lottie_coding =load_lottieurl("https://lottie.host/e7bcaffe-8ade-4a1c-a95f-60bace084a01/c47FULOmKE.json")
img_bpx_logo = Image.open('images//bpxlogo.png')
img2 = Image.open('images//imageoilandgaspng1.png')

#header_sections
with st.container():
    st.subheader("Hi, I am Max Duron :wave:")
    st.title("A Production Systems Engineer at BPX")
    st.write('I am passionatte about finding way to find way to improve ops efficiency and cashflow. ')
    st.write('[BPX HOME PAGE>](https://core.bpx.com/)')

with st.container():
    st.write("---") 
    left_column,right_columns = st.columns(2)
    with left_column:
            st.header("What I do")
            st.write("##")
            st.write("On BPX Energy, I work in a dynamic Oil and Gas work environment, which my expertise lay on creating solution for the Operations group.")
            st.warning("[LinkedIn Profile>](https://www.linkedin.com/in/max-duron-29a183b4/details/experience/)")
    #lottie file json file for animation.
    with right_columns:
        st_lottie(lottie_coding,height=500,key="coding")

# Projects
with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')
    image_column, text_columns = st.columns((1,2))
    with image_column:
         #inset image
        st.image(img2)
    with text_columns:
        st.subheader("Provide Central Operations Solutions for BPX Operations")
        st.write("BPX OPS Tool Kit is one of many Performance and Systems initiative that enables the Business to a centrally located PowerBI repository.")
        st.markdown("[BPXOPSTOOKIT](https://app.powerbi.com/groups/me/apps/d4f6ba4b-1cb1-4c62-8fe2-dac1b13c01d8/reports/417976b4-e5c7-4e33-8f7a-eb5d0b3f6279?experience=power-bi)")

with st.container():
    image_column, text_columns = st.columns((1,2))
    with image_column:
         #inset image
        st.image(img_bpx_logo)
    with text_columns:
        st.subheader("Who is BPX Energy?")
        st.write("bpx energy is a subsidiary of BP P.L.C.1. It is a premier U.S. onshore oil and gas producer with operations in Texas and Louisiana12. The company focuses on safely producing high-margin barrels while driving down emissions2. bpx energy operates in the Permian-Delaware and Eagle Ford basins in Texas and the Haynesville basin in Texas and Louisiana2. In 2022, the company's unconventional oil and gas assets in Texas and Louisiana produced an average of 325,000 barrels of oil equivalent per day.")
        st.markdown("[BP Home Page](https://www.bp.com)")

# --- Contact ---

with st.container():
    st.write('---')
    st.header('Get in Touch with me!')
    st.write("##") #additional space
    
    contact_form = """
    <form action="https://formsubmit.co/max.duron@bpx.com" method="POST">
        <input type="hidden" name="_captcha" value="false">    
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name ="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>"""


    left_column,right_columns = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_columns:
        st.empty()

