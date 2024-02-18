import streamlit as st
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page
from random import randint
from time import sleep

if __name__ == '__main__':
    st.set_page_config(
        page_title="Streamlit about Streamlit",
        page_icon="🥷",
        layout="wide",
        # if you have multipage app but dont want to show the sidebar
        initial_sidebar_state=st.session_state.get(
            'sidebar_state', 'collapsed'),
    )

    st.markdown(footer, unsafe_allow_html=True)

    st.header("Some awesome dashboard, that stakeholders dream of")
    if st.button("Stop this madness"):
        switch_page("presentation")
    gap(2, st)
    placeholder = st.empty()
    while True:
        with placeholder:
            c1, c2, c3 = st.columns([1, 1, 3])
            x = randint(1, 100)
            c1.metric("Metric", x)
            c2.metric("Metric 2", 100-x)
            df = {"sales": [x, 100-x], "costs": [50-x, 75-x]}
            c3.bar_chart(df, height=500, color=['#8000ff', '#bf00ff'])
            sleep(2)
