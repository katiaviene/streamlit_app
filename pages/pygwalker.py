import streamlit as st
import pygwalker as pyg
import pandas as pd



class Walker:
    
    
    @st.cache_data(ttl=60)
    def read_data(_self,file, n):
        df = pd.read_csv(file, nrows=n)
        return df
    
    def render(self):

        st.subheader("PyGWalker")

        st.code("""
                            import pygwalker as pyg 
                            
                            df = pd.read_csv('./data/automobile_data.csv')
                            pyg.walk(df, env='Streamlit')
                            
                            
                            
                            """)

                    
        df = self.read_data('./data/automobile_data.csv', 100)
        pyg.walk(df, env='Streamlit')