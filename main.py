import streamlit as st
from modules.intro import Intro
from modules.components import Components
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page



if __name__ == '__main__':
    st.set_page_config(
            page_title="Streamlit about Streamlit",
            page_icon="streamlit",
            layout="wide",
            initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
        )

    st.markdown(footer, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.48,1,0.2])

    image_container = col2.empty()

    image_container.image("./images/logo1.png", width=500)

    col1, col2, col3 = st.columns([0.35,1,0.2])

    title_container = col2.empty()
    title_container.title("Pythonic Swiss Knife  for Data Apps")


    col1, col2, col3 = st.columns([0.9,0.2,1])
    gap(5, col2)
    button_container = col2.empty()
    
 
    
    if button_container.button("Start the Journey", type='primary'):
        
        switch_page("new_page")
        
        
       