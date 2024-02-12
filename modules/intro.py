import streamlit as st


class Intro:
    
    def render(self):
        
        col1, col2 = st.columns ([1,2])
        
        with col1:
            st.header("Why Streamlit")
            st.image('.\images\8fiq5l.jpg')
        
        with col2:
            st.text("bla")
        