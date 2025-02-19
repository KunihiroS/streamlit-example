from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

user_input = st.text_input("入力してください")
st.write("入力: ", user_input)

if st.checkbox("Show/hide"):
    st.write("Checkbox is checked")

option = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected: ", option)

df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=['a', 'b', 'c', 'd', 'e']
)
st.dataframe(df)


fig, ax = plt.subplots()
ax.scatter(df['a'], df['d'])
st.pyplot(fig)

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 5000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
