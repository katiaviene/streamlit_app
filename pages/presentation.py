import streamlit as st
from modules.intro import Intro
from modules.components import Components
from modules.start import Import
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page




if __name__ == '__main__':

        
    t1, t2, t3, t4, t5, t6, t7, t8, t9= st.tabs([
                            'Why Streamlit', 'Import/Config/Run', 
                            'Components', 'Deploy', 'Tips&Tricks',
                            'Community', 'Analogs', 'Why not Streamlit', 'Repo'])
    
    
    with t1:
        Intro().render()
        
        
    with t2:
        Import().render()
        
    with t3:
        Components().render()
        
    with t9:
        st.image("./images/frame.png", width=400)
    
        
        
        






