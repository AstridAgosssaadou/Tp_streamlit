import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_data = pd.read_csv(r'c:/Users/K/Documents/poto doc/Python/IRIS.csv')
iris_data.columns = ['1', '2', '3', '4','5', '6', '7', '8', '9']

st.title('Exercice avec Iris')

st.subheader('Étape 1 : Manipuler les données')
if st.checkbox('Afficher les premières lignes des données'):
    st.write(iris_data.head())
if st.checkbox('Vérifier les valeurs manquantes'):
    missing_values = iris_data.isnull().sum()
    st.write(missing_values)
if st.checkbox('Filtrer les données où la première colonne est > 5'):
    filtered_data = iris_data[iris_data['1'] > 5]
    st.write(filtered_data)
    
st.subheader('Étape 1 : fficher des graphiques')
st.write('Histogramme des longueurs des pétales')
fig, ax = plt.subplots()
ax.hist(iris_data['5'], bins=20, color='blue', edgecolor='black')
st.pyplot(fig)

st.write('Relation entre longueur et largeur des sépales')
fig2, ax2 = plt.subplots()
sns.scatterplot(data=iris_data, x='1', y='3', hue='9', ax=ax2)
st.pyplot(fig2)

st.write('Boxplot des longueurs des sépales par espèce')
fig4, ax4 = plt.subplots()
sns.boxplot(data=iris_data, x='9', y='1', ax=ax4)
st.pyplot(fig4)

