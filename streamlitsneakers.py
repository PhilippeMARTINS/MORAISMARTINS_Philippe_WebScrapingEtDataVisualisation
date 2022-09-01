from tkinter import *
from calendar import c
from contextlib import nullcontext
import streamlit as st
import plotly_express as px
import pandas as pd
from PIL import Image
import requests
import json
import PIL.Image
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="Sneakers: Reebok/Adidas", page_icon=":athletic_shoe:", layout="wide")

#header
image = PIL.Image.open('imgsneaker.jpg')
st.image(image,use_column_width=True)
st.subheader("Bonjour, bienvenue sur mon streamlit sur les sneakers Reebok et Adidas")
st.title("Sneakers:")
st.write("Vous retrouverez ici les différents modèles de sneakers des marques Reebok et Adidas:")

#sidebar
st.sidebar.subheader("Filtrer")

#setup file upload
DATA_URL = ('http://127.0.0.1:80')

def load_data():
    data = pd.read_json(DATA_URL)
    return data

df = load_data()
df = df.drop(columns=[''], axis=1)

st.dataframe(df)

df2 = df

with st.sidebar.form(key = "form4"):
    marque = st.multiselect('Marque recherché',('','Reebok', 'Adidas'),('Reebok', 'Adidas'))
    submit4 = st.form_submit_button(label = "Submit")

with st.sidebar.form(key = "form1"):
    modele = st.text_input(label="Modèle recherché:")
    submit1 = st.form_submit_button(label = "Submit")
    
with st.sidebar.form(key = "form2"):
    gamme = st.multiselect('Gamme Reebok recherché',('','Classics', 'Hommes Classics', 'Femmes Classics',
 'Hommes Fitness & Training', 'Enfants Classics', 'Garçons Running',
 'Garçons Classics', 'Running', 'Filles Classics', 'Fitness & Training',
 'Enfants Running', 'Filles Running', 'Hommes City Outdoor',
 'Femmes Fitness & Training', 'Hommes Natation', 'Hommes Marche',
 'Hommes Running', 'Femmes City Outdoor', 'Femmes Marche', 'Marche',
 'Hommes Cross Training', 'Lifestyle', 'Femmes Running', 'City Outdoor',
 'Femmes Cross Training', 'Filles Fitness & Training', 'Femmes Natation',
 'Garçons Fitness & Training'),('Classics', 'Hommes Classics', 'Femmes Classics'))
    submit2 = st.form_submit_button(label = "Submit")
    #st.write('Gaamme recherché:', gamme)
    
with st.sidebar.form(key = "form5"):
    gamme2 = st.multiselect('Gamme Adidas recherché',('','Golf', 'Femmes Originals', 'Enfants Originals', 'Originals',
 'Hommes Originals', 'Enfants Sportswear', 'Femmes Sportswear', 'Sportswear',
 'Hommes Sportswear', 'Hommes Golf', 'Hommes Tennis', 'Femmes Tennis',
 'Enfants Basketball', 'Hommes Running', 'Femmes Running', 'TERREX',
 'Hommes TERREX', 'Football', 'Basketball', 'Femmes Basketball',
 'Tennis De Table', 'Femmes TERREX', 'Hommes Basketball', 'Running',
 'Enfants Football', 'Cyclisme', 'Futsal',
 'Femmes adidas by Stella McCartney', 'Hommes Fitness Et Training',
 'Femmes Tennis De Table', 'Enfants TERREX', 'Femmes Fitness Et Training',
 'Y-3', 'Five Ten', 'Enfants Tennis', 'Hommes Tennis De Table',
 'Haltérophilie', 'Enfants Futsal', 'Enfants Running', 'Hommes Randonnée',
 'Femmes Lifestyle', 'Enfants Tennis De Table', 'Boxe', 'Athlétisme',
 'Femmes Golf', 'Rugby', 'Hommes Hockey Sur Gazon', 'Femmes Five Ten',
 'Femmes Hockey Sur Gazon', 'Enfants Golf', 'Hommes Five Ten',
 'Enfants Five Ten', 'Hockey Sur Gazon', 'Hommes Haltérophilie',
 'Enfants Hockey Sur Gazon', 'Hommes Athlétisme', 'Lifestyle', 'Hommes Rugby',
 'Hommes Y-3'),('Originals', 'Hommes Originals', 'Femmes Originals'))
    submit5 = st.form_submit_button(label = "Submit")
    
with st.sidebar.form(key = "form3"):
    min_prix, max_prix = st.slider("Sélection par prix", 0, 1000, (0, 1000))
    submit3 = st.form_submit_button(label = "Submit")
    #st.write('Prix entre', min_prix, 'et', max_prix)
                          
df_filtred = df2.loc[(df2["Modèle"].str.contains(modele))
    & ((df2["Gamme"].isin(gamme)) | (df2["Gamme"].isin(gamme2)))
    & (df2["Prix"].between(min_prix, max_prix))
    & (df2["Marque"].isin(marque)) 
    ] 

st.dataframe(df_filtred)

st.write('Nombre de modèle selectionné:',df_filtred.shape[0])

df_gamme = df_filtred.Gamme.value_counts()
st.dataframe(df_gamme)

fig = plt.figure(figsize = (10, 5))
plt.bar(df_gamme.index, df_gamme)
plt.xlabel("Gammes")
plt.ylabel("Nombre de Sneakers")
plt.title("Nombre de sneakers sur les différentes gammes séléctionnées")
st.pyplot(fig)

df_prix = df_filtred.Prix.value_counts()
st.dataframe(df_prix)

fig3 = plt.figure(figsize=(8, 4))
plt.pie(df_prix, labels = df_prix.index, textprops={'fontsize': 5})
plt.title("Prix les plus présent")
st.pyplot(fig3)
