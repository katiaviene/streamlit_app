import streamlit as st


st.set_page_config(
        page_title="Streamlit about Streamlit",
        page_icon="streamlit",
        layout="wide",
        initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
    )

col1, col2, col3 = st.columns([0.3,1,0.2])

image_container = col2.empty()

image_container.image("streamlit-logo-primary-colormark-darktext.png", width=700)

col1, col2, col3 = st.columns([0.35,1,0.2])

title_container = col2.empty()
title_container.title("Pythonic Swiss Knife  for Data Apps")


col1, col2, col3 = st.columns([0.9,0.2,1])

button_container = col2.empty()

if button_container.button("Start the Journey"):
    image_container.empty()
    title_container.empty()
    button_container.empty()
    
    t1,t2,t3,t4,t5 = st.tabs(["About me", 'Agenda', 'What is Streamlit', 'Import/Config/Run', 'Components'])
    






