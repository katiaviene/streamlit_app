import streamlit as st
from custom_components.ccomponents import gap

class Alternatives:
    
    def render(self):
        c1,c2 = st.columns([1,2])
        with c1:
            st.image("./images/gradio-image-2.png", width=250)
            st.image("./images/featured-image.png", width=250)
            gap(1,st)
            st.image("./images/nicegui.png", width=250)
            gap(2,st)
            st.image("./images/wave.png", width=250)
            gap(2,st)
            st.image("./images/ANVIL-Logo-no-tagline.png", width=250)
            st.image("./images/voila_logo.png", width=250)
        with c2:
            st.subheader("Gradio")
            st.write(" ")