import streamlit as st
from modules.about import About
from modules.intro import Intro
from modules.components import Components







st.set_page_config(
        page_title="Streamlit about Streamlit",
        page_icon="streamlit",
        layout="wide",
        initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
    )

col1, col2, col3 = st.columns([0.3,1,0.2])

image_container = col2.empty()

image_container.image("./images/streamlit-logo-primary-colormark-darktext.png", width=700)

col1, col2, col3 = st.columns([0.35,1,0.2])

title_container = col2.empty()
title_container.title("Pythonic Swiss Knife  for Data Apps")


col1, col2, col3 = st.columns([0.9,0.2,1])

button_container = col2.empty()

if button_container.button("Start the Journey"):
    image_container.empty()
    title_container.empty()
    button_container.empty()
    
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs(["About me", 'Agenda', 
                              'Why Streamlit', 'Import/Config/Run', 
                              'Components', 'Deploy', 'Tips&Tricks',
                              'Community', 'Why not Streamlit'])
    
    with t1:
        about = About()
        about.render()
    
    with t3:
        intro = Intro()
        intro.render()
        
        
    with t5:
        components = Components()
        components.render()
        
    
    
    






