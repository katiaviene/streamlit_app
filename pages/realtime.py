import streamlit as st
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page
from random import randint
from time import sleep
import matplotlib.pyplot as plt

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
            c1, c2= st.columns([1, 1], gap='large')
            x = randint(1, 100)
            
            df = {"sales": [x, 200-x], "costs": [150-x, 175-x]}
            c1.dataframe(df, use_container_width=True)
            with c1:
                cc1, cc2 = st.columns([1,1])
                cc1.metric("Metric", x)
                cc2.metric("Metric 2", 100-x)
                fig, ax = plt.subplots()
                ax.pie(df["sales"], labels=df["sales"], colors=['#0489B1', '#04B486'])
                cc1.pyplot(plt)
                fig, ax = plt.subplots()
                ax.pie(df["costs"], labels=df["costs"], colors=['#D7DF01', '#DF0174'])
                cc2.pyplot(plt)
            c2.bar_chart(df, height=500, color=['#8000ff', '#bf00ff'])
            sleep(2)
