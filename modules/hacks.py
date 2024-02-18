import streamlit as st
import hydralit_components as hc



class Hydralit_layout:
    
    def render(self):
        over_theme = {'txc_inactive': 'white', 'menu_background': "#8A0886", 'txc_active': "#0b5669", 'option_active': "white"}
        menu_data = [
            {'label': 'Home'},
            {'label' : "Another awesome page"}
        ]

        menu = hc.nav_bar(menu_definition= menu_data, override_theme=over_theme)
        
        if menu == 'Home':

            st.code("""import hydralit_components as hc
                    
menu_data = [{'label': 'Home'}, {'label' : "Another awesome page"}]
menu = hc.nav_bar(menu_definition= menu_data)
                            
if menu == 'Home':
    st.write("Hi")
                    """)