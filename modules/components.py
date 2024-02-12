import streamlit as st


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
                
      
                
        

        