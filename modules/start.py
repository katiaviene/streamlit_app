import streamlit as st
from custom_components.ccomponents import gap


class Import:

    def render(self):
        c1, c0, c2 = st.columns([1, 0.2, 1])
        with c1:
            st.subheader("Install and import")
            st.code("pip install streamlit")
            st.code("import streamlit as st")

            st.subheader("Config the page")

            st.code("""
                        st.set_page_config(
                        page_title="Streamlit about Streamlit",
                        page_icon="🥷",
                        layout="wide",
                        initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed') # if you have multipage app but hate the sidebar:)
                    )
                    """)

            st.subheader("Release the monster")
            st.code("streamlit run app.py")

            st.subheader("Release the monster on a leash")

            st.code("streamlit run app.py --server.port 8502 --theme.base light")
        with c2:
            gap(6, st)
            st.image(".\images\easy2.jpg")
