import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o CSV
file_path = 'results.csv'  # Substitua pelo caminho correto do seu arquivo CSV
data = pd.read_csv(file_path, delimiter=';')

# Título da aplicação
st.title('Visualização de Dados')

# Seleção do tipo de gráfico
chart_type = st.selectbox(
    'Selecione o tipo de gráfico',
    ['Gráfico de Barras', 'Gráfico de Dispersão', 'Boxplot', 'Gráfico de Linhas', 'Histograma']
)

# Seleção das colunas
columns = data.columns.tolist()
x_axis = st.selectbox('Selecione a coluna do eixo X', columns)
y_axis = st.selectbox('Selecione a coluna do eixo Y', columns)

# Gerar gráfico baseado na seleção
if chart_type == 'Gráfico de Barras':
    st.subheader('Gráfico de Barras')
    data.plot(x=x_axis, y=y_axis, kind='bar', figsize=(10, 6))
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(plt)
    
elif chart_type == 'Gráfico de Dispersão':
    st.subheader('Gráfico de Dispersão')
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=x_axis, y=y_axis, hue='dataset')
    plt.title(f'{x_axis} vs {y_axis}')
    plt.xticks(rotation=90)  # Rotacionar os rótulos do eixo X para 90 graus
    st.pyplot(plt)
    
elif chart_type == 'Boxplot':
    st.subheader('Boxplot')
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x=x_axis, y=y_axis)
    plt.title(f'{y_axis} by {x_axis}')
    plt.xticks(rotation=90)  # Rotacionar os rótulos do eixo X para 90 graus
    st.pyplot(plt)

elif chart_type == 'Gráfico de Linhas':
    st.subheader('Gráfico de Linhas')
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x_axis, y=y_axis)
    plt.title(f'{y_axis} over {x_axis}')
    plt.xticks(rotation=90)  # Rotacionar os rótulos do eixo X para 90 graus
    st.pyplot(plt)

elif chart_type == 'Histograma':
    st.subheader('Histograma')
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=x_axis, kde=True)
    plt.title(f'Distribuição de {x_axis}')
    plt.xticks(rotation=90)  # Rotacionar os rótulos do eixo X para 90 graus
    st.pyplot(plt)
