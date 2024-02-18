import streamlit as st
from modules.intro import Intro
from modules.components import Components
from modules.start import Import
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page


if __name__ == '__main__':

    t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
        'Why Streamlit', 'Import/Config/Run',
        'Components', 'Deploy', 'Tips&Tricks',
        'Community', 'Analogs', 'Why not Streamlit', 'Repo'])

    with t1:
        Intro().render()

    with t2:
        Import().render()

    with t3:
        Components().render()

    with t5:
        tt1, tt2, tt3, tt4 = st.tabs(
            ["Hydralit", "Iframe", "Markdowns", "Cashing"])
        with tt1:
            st.subheader("Hydralit components")
            if st.button("Hydralit demo"):
                switch_page("hydralit")
        with tt2:
            c1, c2 = st.columns([1, 2])
            with c1:
                st.subheader("Iframe")
                st.code("""
                        iframe_html = '''
                        <iframe
                            src="http://localhost:8501/realtime"
                            width="100%"
                            height="800"
                            frameborder="0"
                            scrolling="no">
                        </iframe>
                    '''

                st.markdown(f'<div style="height:800px;overflow:hidden">{iframe_html}</div>', unsafe_allow_html=True)

                        """)
            with c2:
                iframe_html = '''
                        <iframe
                            src="http://localhost:8501/realtime"
                            width="100%"
                            height="800"
                            frameborder="0"
                            scrolling="no">
                        </iframe>
                    '''

                st.markdown(
                    f'<div style="height:800px;overflow:hidden">{iframe_html}</div>', unsafe_allow_html=True)

    with t9:
        c1, c2 = st.columns([1, 1])
        c1.header("Check out the repo")
        with c2:
            gap(5, st)
            st.image("./images/frame.png", width=400)
