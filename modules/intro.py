import streamlit as st
from custom_components.ccomponents import gap


class Intro:

    def render(self):

        c0, col1, col2 = st.columns([0.1, 1, 1.5])

        with col2:
            gap(3, st)
            st.image('.\images\8fiq5l.jpg')

        with col1:
            st.header("Why Streamlit")
            gap(2, st)
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
                gap(1, st)
