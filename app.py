import imp
from turtle import right
import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title='My Workpage', page_icon=':tada:', layout='wide')

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# USE LOCAL CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html =True)

local_css("style/style.css")

# LOAD ASSETS
lottie_coding= load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_rjkkxapa.json')
img_project = Image.open('images/wq.jpg')

# HEADER SECTION
st.subheader('Hi, I am Ekta :wave:')
st.title('A Data Analyst from India')
st.write('I am passionate about finding ways to use Python and VBA to  be more efficient and effective in business setting.')
st.write('[Learn More >](https://github.com/EktaSingh1612)')

# WHAT I DO
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('About me')
        st.write('##')
        st.write('''I am graduated as Mechanical engineer and done post-graduation in Production Engineering from SSTC, Bhilai. After my graduation I was preparing for civil services. During my civil services preparation I learned about machine learning and AI & how data has become the new oil since last decade which made me enthusiastic to learn more related to this space. So, after giving enough number of years to civil services preparation, I decided to change my career path to Data Analytics.
                    Right now I am learning various tools such as Python, MySQL, Microsoft Excel, Power Point, Power BI, Tableau etc from various online sources.''')
        st.write('[LinkedIn >](https://www.linkedin.com/in/ektasingh1612/)')
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')

# PROJECTS
with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_project)
    with text_column:
        st.subheader('Wine quality analysis')
        st.write(
            '''
            This datasets is related to red variants of the Portuguese "Vinho Verde" wine.The dataset describes the amount of various chemicals present in wine and their effect on it's quality. The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).Your task is to predict the quality of wine using the given data.
            A simple yet challenging project, to anticipate the quality of wine. The complexity arises due to the fact that the dataset has fewer samples, & is highly imbalanced. Can you overcome these obstacles & build a good predictive model to classify them?
            '''
        )
        st.markdown('[Look at the project...](https://github.com/EktaSingh1612/Wine_quality)')

    with st.container():
        st.write('---')
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_project)
        with text_column:
            st.subheader('Wine quality analysis')
            st.write(
                '''
                This datasets is related to red variants of the Portuguese "Vinho Verde" wine.The dataset describes the amount of various chemicals present in wine and their effect on it's quality. The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).Your task is to predict the quality of wine using the given data.
                A simple yet challenging project, to anticipate the quality of wine. The complexity arises due to the fact that the dataset has fewer samples, & is highly imbalanced. Can you overcome these obstacles & build a good predictive model to classify them?
                '''
            )
            st.markdown('[Look at the project...](https://github.com/EktaSingh1612/Wine_quality)')


# CONTACT
with st.container():
    st.write('---')
    st.header('Get in touch with me!')
    st.write('##')

    # Documentation from https://formsubmit.co 
    contact_form = '''
    <form action="https://formsubmit.co/ektas1612@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


