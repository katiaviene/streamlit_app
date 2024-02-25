import streamlit as st
import pygwalker as pyg
import pandas as pd
import hydralit_components as hc


class Walker:

    def read_data(self, file, n):
        df = pd.read_csv(file, nrows=n)
        return df

    def render(self):

        st.subheader("PyGWalker")

        st.code("""
                            import pygwalker as pyg 
                            
                            df = pd.read_csv('./data/automobile_data.csv')
                            pyg.walk(df, env='Streamlit')
                            
                            
                            
                            """)

        # with hc.HyLoader('Now doing loading', hc.Loaders.standard_loaders):
        df = self.read_data('./data/automobile_data.csv', 1000)
        st.dataframe(df)
        pyg.walk(df, env='Streamlit')
