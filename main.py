import streamlit as st
from modules.intro import Intro
from modules.components import Components
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page
from time import sleep

# Hi, friend. Welcome to the Streamlit app about Streamlit.



if __name__ == '__main__': 
    
    # You have to configure the page, but just once during the developenent process
    st.set_page_config(
            page_title="Streamlit about Streamlit",
            page_icon="🥷",
            layout="wide",
            initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'), # if you have multipage app but dont want to show the sidebar
        )

    st.markdown(footer, unsafe_allow_html=True) # chechout my custom components, such as footer

    c1,c2 = st.columns([3,1])
   
   
    with c1:
        image_container = st.empty()
        image_container.image("./images/logo1.png", width=700,)
        title_container = st.empty()
        title_container.title("Pythonic Swiss Knife  for Data Apps")

    with c2:
        gap(20, st) # little custom function/hack to make vertical gap
        button_container = st.empty()
        if button_container.button("Start the Journey", type='primary'):
            image_container.empty()
            title_container.empty()
            button_container.empty()
            sleep(1)
            switch_page("realtime")
        
        
       