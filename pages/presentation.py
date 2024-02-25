import streamlit as st
from modules.intro import Intro
from modules.components import Components
from modules.start import Import
from modules.alternatives import Alternatives
from custom_components.ccomponents import footer, gap
from streamlit_extras.switch_page_button import switch_page


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
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = st.tabs([
        'Why Streamlit', 'Import/Config/Run',
        'Components', 'Deploy', 'Tips&Tricks',
        'Community', 'Alternatives', 'Why not Streamlit', 'Repo'])

    with t1:
        Intro().render()

    with t2:
        Import().render()

    with t3:
        Components().render()

    with t5:
        tt1, tt2, tt3, tt4, tt5 = st.tabs(
            ["Markdown", "Cashing", "Hydralit", "Iframe", "Tools for data analysis"])
        with tt1:
            c1, c2 = st.columns([1, 2])
            st.markdown(""" <style> .font {
                 font-size:40px ; font-family: "Helvetica"; color: #4B889C;font-weight: 400} 
                 </style> """, unsafe_allow_html=True)
            c1.markdown('<p class="font"; style="padding-left: 3px;">Markdown</p>', unsafe_allow_html=True)
            c1.code("""
                    
                    st.markdown(' <style> .font {font-size:40px ; font-family: "Helvetica"; color: #4B889C;font-weight: 400 </style> ', unsafe_allow_html=True)
                    st.markdown('<p class="font"; style="padding-left: 3px;">Markdown</p>', unsafe_allow_html=True)
                    
                    """)
            with c2:
                st.subheader("Change styling of widgets")
                st.markdown(
                    """
                <style>
                span[data-baseweb="tag"] {
                  background-color: #637B84 !important;
        
                }
                </style>
                """,
                    unsafe_allow_html=True,
                )
                
                st.multiselect("Multiselect", ("Option 1", "Option 2", "Option 3", "Option 4"))
                
                st.code("""
                        
                        st.markdown('<style> span[data-baseweb="tag"] {background-color: #637B84 !important;}</style>', unsafe_allow_html=True)
   
                        """)
                
                st.markdown(
                    """
                 <style>
  
                [data-testid="stExpander"] {
                    background-color: #637B84;
                    border-color: #ff6666; 
                }
                </style>
                """,
                    unsafe_allow_html=True,
                )
                
                gap(2,st)
                
                st.write("Expander")
                with st.expander("Expander"):
                    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
                    
                    
                    
                st.code("""
                        st.markdown('
                 <style>

                [data-testid="stExpander"] {
                    background-color: #637B84;
                    border-color: #ff6666; 
                }
                </style>
                ',
                    unsafe_allow_html=True,
                )
                        """)
                
                st.write("Footer")
                st.code(f"{footer}")
        
        with tt2:
            c1, c2 = st.columns([1,2])
            c1.subheader("Cache")
            
            with c2:
                st.image("https://docs.streamlit.io/images/caching-high-level-diagram.png")
                st.code("""@cache_resource(func, *, ttl, max_entries, show_spinner, validate, experimental_allow_widgets, hash_funcs=None)
def init_connection():
    host = "hh-pgsql-public.ebi.ac.uk"
    database = "pfmegrnargs"
    user = "reader"
    password = "NWDMCE5xdipIjRrp"
    return psycopg2.connect(host=host, database=database, user=user, password=password)
                        
                        
                        
                        
                        
                        """)
                st.code("""@cashe_data(func=None, *, ttl=60, max_entries=100000, show_spinner=False, persist='disk', experimental_allow_widgets=False, hash_funcs=None)
def expensive_calculations():
    return df

                        """)
                
                st.cache_data.clear()
                st.code("st.cache.clear_cache()")
        
        
        with tt3:
            st.subheader("Hydralit components")
            if st.button("Hydralit demo"):
                switch_page("hydralit")
        with tt4:
            c1, c2 = st.columns([1, 2])
            with c1:
                st.subheader("Iframe")
                st.code("""
                        iframe_html = '''
                        <iframe
                            src="http://localhost:8502/realtime"
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

    with t7:
        Alternatives().render()
    
    
    
    
    
    
    with t9:
        c1, c2 = st.columns([1, 1])
        c1.header("Check out the repo")
        with c2:
            gap(5, st)
            st.image("./images/frame.png", width=400)
