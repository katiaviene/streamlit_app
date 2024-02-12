import streamlit as st 

class About:
    
    
    def render(self):
        col1, col2 = st.columns([1,1])
        
        with col1:
            st.image('./images/IMG_2807.jpg', width=280)
            st.text("Ekaterina Korolkoviene // Data Engineer@BITE ")
             
            
