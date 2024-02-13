import streamlit as st
from custom_components.ccomponents import gap


class Intro:
    
    def render(self):
        
        col1, col2 = st.columns ([2,1])
        
        with col1:
            gap(3, st)
            st.image('.\images\8fiq5l.jpg')
        
        with col2:
            st.header("Why Streamlit")
            options = [
                "Ease of Use", 
                "Rapid Prototyping", 
                "Pythonic",
                "Interactive Widgets",
                "Sharing and Deployment",
                "Community and Ecosystem",
                "Customization"
                
            ]
            
            for opt in options:
                st.checkbox(opt, True)
                st.write(" ")
        