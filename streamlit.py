# you can work on python script but there is a possibility to add html script

#import std libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Write a title
st.title('Data Explorer app')

# go on the terminal to run your part: streamlit run <filename.py>

# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write('A **simple** *app* to explore `penguin´ [data](https://allisonhorst.github.io/palmerpenguins/) :penguin:')

# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')

# Write heading for Data
st.header('Data')

# Read csv file and output a sample of 20 data points
df = pd.read_csv('penguins_extra.csv')
st.write(df)

# Add a selectbox for species
species = st.selectbox('Select your SPECIES', df.species.unique())

# Display a sample of 20 data points according to the species selected with corresponding title
df_species = df.loc[df.species == species]
st.write(df_species.sample(10))

# Plotting seaborn
fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='bill_length_mm', y='flipper_length_mm', hue='species', size='sex')
st.pyplot(fig)

# Plotting plotly
fig = px.scatter(df, x='bill_length_mm', y='flipper_length_mm', animation_frame='species', range_x=[25,80], range_y=[150,250], color='sex')
st.plotly_chart(fig)

# Bar chart count of species per island
st.subheader('Counting the number of penguins per island')
st.bar_chart(df.groupby('species')['island'].count())

# Maps
st.subheader('Plotting the data points in a map')
st.map(df)

# create a import doc box
file = st.file_uploader('Upload csv files', type=['csv'])
if file is not None:
    data= pd.read(file)
    st.write(data)

# box to import image
file_img = st.file_uploader('Input image', type=['jpg', 'png', 'jpeg'])
from PIL import Image
if file_img is not None:
    img= pd.read(file_img)
    st.write(img)

# Reference https://deckgl.readthedocs.io/en/latest/
st.write('If you are intersted to further explore mapping check out [pydeck](https://deckgl.readthedocs.io/en/latest/)')

# sidebar comment
choices = st.sidebar.radio('Have you found this interesting', ['yes', 'no'])
if choices == 'yes':
    st.write('YES')
else:
    st.write('NO')

# Add background image in
st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# deploy streamlit but we need to connect to github 

