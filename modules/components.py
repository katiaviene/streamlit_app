import streamlit as st
import pandas as pd


class Concepts:

    def render(self):
        st.subheader("Runs from top to bottom")
        st.write(" - Source code is modified")
        st.write(" - App status is changes (widget has been interacted with)")
        st.image("./images/top_to_b.png")
        
        


class Widgets:

    def render(self):
        st.subheader("Main widgets")
        iframe_html = '''
                        <iframe
                            src="https://docs.streamlit.io/library/api-reference/widgets/?embedded=true"
                            width="100%"
                            height="800"
                            frameborder="0"
                            scrolling="yes">
                        </iframe>
                    '''

        st.markdown(
                    f'<div style="height:800px;overflow:hidden">{iframe_html}</div>', unsafe_allow_html=True)

class Charts:
    
    
    def render(self):
        st.subheader("Standart")
        iframe_html = '''
                        <iframe
                            src="https://docs.streamlit.io/library/api-reference/charts"
                            width="100%"
                            height="800"
                            frameborder="0"
                            scrolling="yes">
                        </iframe>
                    '''

        st.markdown(
                    f'<div style="height:800px;overflow:hidden">{iframe_html}</div>', unsafe_allow_html=True)
        st.subheader("Echarts")
        iframe_html = '''
                        <iframe
                            src="https://echarts.streamlit.app/?embedded=true"
                            width="100%"
                            height="800"
                            frameborder="0"
                            scrolling="yes">
                        </iframe>
                    '''

        st.markdown(
                    f'<div style="height:800px;overflow:hidden">{iframe_html}</div>', unsafe_allow_html=True)

        st.subheader("Vizzu")
        iframe_html = '''
                        <iframe
                            src="https://vizzu-builder.streamlit.app/?embedded=true"
                            width="100%"
                            height="800"
                            frameborder="0"
                            scrolling="yes">
                        </iframe>
                    '''

        st.markdown(
                    f'<div style="height:800px;overflow:hidden">{iframe_html}</div>', unsafe_allow_html=True)


class Tables:

    @st.cache_data(ttl=600)
    def read_data(_self, file):
        df = pd.read_csv(file, delimiter=';', nrows=10000)
        return df

    def render(self):
        st.checkbox("Build-in dataframe visualizations", True)
        st.code("st.table(df)")
        df = self.read_data("./data/games_data.csv")

        st.table(df.head(10))
        st.code("st.dataframe(df)")
        st.dataframe(df.head(10), width=1200)

        st.code("st.data_editor(df)")

        df["Battles"] = df["battles"].apply(
            lambda x:  [x, x+10, x-4, x+30, x-20])
        df["Battles2"] = df["Battles"]

        st.data_editor(df,
                       column_config={"Battles": st.column_config.LineChartColumn(
                           "Battles",
                           width="medium",
                           y_min=0,
                           y_max=100),
                           "Battles2": st.column_config.BarChartColumn(
                           "Battles2",
                           width="medium",
                           y_min=0,
                           y_max=100
                       )
                       },

                       width=1200)


class Components:

    def render(self):

        col1, col2 = st.columns([0.4, 2])

        with col1:
            st.header("Concepts & Components")

        with col2:

            t1, t2, t3, t4 = st.tabs(
                ["Concepts", "Layot", "Tables", "Plots"])

            with t1:
                Concepts().render()
        

            with t2:
                Widgets().render()

            with t3:
                tables = Tables()
                tables.render()
            
            with t4:
                Charts().render()
