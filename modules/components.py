import streamlit as st
import pandas as pd


class Connections:
    
    
    def render(self):
        st.write("Connect your data from any source")


class Layout:
    
    def render(self):
        st.write("Main layout components")
        
        c1, c2 = st.columns([1,2])
        
        with c1:
            options = st.radio("", options=["Columns", "Containers"])
            
            if options == "Columns":
                st.write("columns")
                st.code(" c1, c2 = st.columns([1,1])")
            
            elif options == "Containers":
                st.write("Containers")
                
                
class Tables:
    
    def read_data(self,file):
        df = pd.read_csv(file, delimiter=';', nrows=10000)
        return df
    
    def render(self):
        st.checkbox("Build-in dataframe visualizations", True)
        st.code("st.table(df)")
        df = self.read_data(".\data\games_data.csv")
        
        st.table(df.head(10))
        st.code("st.dataframe(df)")
        st.dataframe(df.head(10), width=1200)
        
        st.code("st.data_editor(df)")
        st.data_editor(df, width=1200)        
        
        
        
        
        
        
class Components:
    
    def render(self):
        
        col1, col2 = st.columns([0.5, 2])
        
        with col1:
            st.header("Components")
            
        with col2:
            
            t1, t2, t3, t4 = st.tabs(["Connections", "Layot", "Tables" , "Plots"])
            
            with t1:
                connections = Connections()
                connections.render()
            
            with t2:
                layout = Layout()
                layout.render()
            
            with t3:
                tables = Tables()
                tables.render()
      
                
        

        