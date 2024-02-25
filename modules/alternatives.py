import streamlit as st
from custom_components.ccomponents import gap

class Alternatives:
    
    def render(self):
        c1,c2 = st.columns([1,2])
        with c1:
            st.image("./images/gradio-image-2.png", width=250)
            gap(5, st)
            st.image("./images/featured-image.png", width=250)
            gap(6,st)
            st.image("./images/nicegui.png", width=250)
            gap(6,st)
            st.image("./images/wave.png", width=250)
            gap(4,st)
            st.image("./images/ANVIL-Logo-no-tagline.png", width=250)
            gap(3,st)
            st.image("./images/voila_logo.png", width=250)
        with c2:
            st.write("East to use ML Models: Gradio is now part of Hugging Face, and the Hugging Face integration makes it sleek and simple to load ML models and datasets.")
            st.write("Not standalone apps: Gradio apps work best when embedded in another webpage, unlike Streamlit apps which work well as standalone apps.")
            st.write("---")
            st.write("Faster than Streamlit: Dash only needs to run the functions that are called while interacting with the app. With Streamlit, the entire script is re-run with every interaction.")
            st.write("Larger learning curve: Dash is a bit more complicated than Streamlit (you’ll need to use “callbacks” and some HTML, for example), so it isn’t as easy to get started with.")
            st.write("---")
            st.write("Great amount of extra features: notifications, dialogs and menus; ability to add custom routes and data responses;  immediate feedback to user actions without full page reloads.Built on top of FastApi")
            st.write("Lacks a large community and robust support system, resulting in relatively limited information available online compared to other platforms")
            st.write("---")
            st.write("H2O Wave excels at capturing information from multiple sources and broadcasting them live over the web, letting you build and deploy realtime analytics with dramatically less effort.")
            st.write("Complex")
            st.write("---")
            st.write("Out-of-the-box instant cloud hosting , drag-and-drop UI builder, more features for complex apps")
            st.write("Larger learning curve, not all features are available for free")
            st.write("---")
            st.write("Any Jupyter Notebook can also be a Voila dashboard.")
            st.write("More complex dashboards with multiple interacting parts are harder to build.")