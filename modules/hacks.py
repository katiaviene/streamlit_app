import streamlit as st
import hydralit_components as hc
import time
from streamlit_extras.switch_page_button import switch_page


class Hydralit_layout:

    def render(self):
        over_theme = {'txc_inactive': 'white', 'menu_background': "#8A0886",
                      'txc_active': "#0b5669", 'option_active': "white"}
        menu_data = [
            {'label': 'Nav bar'},
            {'label': "Loaders"},
            {'label': "Option bars"},
            {'label': "Back"}
        ]

        menu = hc.nav_bar(menu_definition=menu_data, override_theme=over_theme)

        if menu == 'Nav bar':

            st.code("""import hydralit_components as hc
                    
menu_data = [{'label': 'Home'}, {'label' : "Another awesome page"}]
menu = hc.nav_bar(menu_definition= menu_data)
                            
if menu == 'Home':
    st.write("Hi")
                    """)

        if menu == "Loaders":
            c1, c2 = st.columns([1.5, 1])
            c1.subheader("Loaders")
            c1.code("""
 

                # for 3 loaders from the standard loader group
                with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=[3,0,5]):
                    time.sleep(5)

                # for 1 (index=5) from the standard loader group
                with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=5):
                    time.sleep(5)

                # for 4 replications of the same loader (index=2) from the standard loader group
                with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=[2,2,2,2]):
                    time.sleep(5)
  
                    """)
            with c2:

                # for 3 loaders from the standard loader group
                with hc.HyLoader('Now doing loading', hc.Loaders.standard_loaders, index=[3, 0, 5]):
                    time.sleep(5)

                # for 1 (index=5) from the standard loader group
                with hc.HyLoader('Now doing loading', hc.Loaders.standard_loaders, index=5):
                    time.sleep(5)

                # for 4 replications of the same loader (index=2) from the standard loader group
                with hc.HyLoader('Now doing loading', hc.Loaders.standard_loaders, index=[2, 2, 2, 2]):
                    time.sleep(5)

        if menu == 'Option bars':
            c1, c2 = st.columns([2, 1])
            option_data = [
                {'label': "Chose me 1"},
                {'label': "Chose me 2"},
                {'label': "Chose me 3"},
            ]
            with c1:
                op = hc.option_bar(option_definition=option_data, title='Option bar 1',
                                   key='PrimaryOption', override_theme=over_theme, horizontal_orientation=True)

                st.code("""
                        option_data = [
                    {'label': "Chose me 1"},
                    {'label': "Chose me 2"},
                    {'label': "Chose me 3"},
                ]   
                    
                op = hc.option_bar(option_definition=option_data,title='Option bar 1',key='PrimaryOption',override_theme=over_theme, horizontal_orientation=True)
                if op == 'Chose me 1':
                    pass
                        """)

            op2 = hc.option_bar(option_definition=option_data, title='Option bar 2',
                                override_theme=over_theme, horizontal_orientation=False)
            st.code("""
                        option_data = [
                    {'label': "Chose me 1"},
                    {'label': "Chose me 2"},
                    {'label': "Chose me 3"},
                ]   
                    
                op = hc.option_bar(option_definition=option_data,title='Option bar 2',override_theme=over_theme, horizontal_orientation=False)
                if op == 'Chose me 1':
                    pass
                        """)

        if menu == "Back":
            switch_page("presentation")
