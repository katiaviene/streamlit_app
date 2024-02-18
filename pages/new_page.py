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
            initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'))

        
        
        
    t1, t2, t3, t4, t5, t6, t7= st.tabs([
                            'Why Streamlit', 'Import/Config/Run', 
                            'Components', 'Deploy', 'Tips&Tricks',
                            'Community', 'Why not Streamlit'])
    
    
    with t1:
        intro = Intro()
        intro.render()
        
        
    with t3:
        components = Components()
        components.render()
        
        
        
        






