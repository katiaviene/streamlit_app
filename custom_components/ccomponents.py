footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;

color: #FF4B4B;
text-align: left;
}
</style>
<div class="footer">
<p>Ekaterina Korolkoviene // Data Engineer@BITE        <a style='display: block; text-align: left;</p>
</div>
"""


def gap(n, st):
    for i in range(1, n+1):
        st.write(" ")
