import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os CSVs
intersectional_file = 'intersectional.csv'
heart_file = 'heart.csv'
data_intersectional = pd.read_csv(intersectional_file, delimiter=';')
data_heart = pd.read_csv(heart_file, delimiter=';')

# Título da aplicação
st.title('Visualização de Dados')

# Função para gerar gráficos
def gerar_grafico(data, file_name):
    st.header(f"Visualização para {file_name}")
    
    # Seleção do tipo de gráfico
    chart_type = st.selectbox(
        f'Selecione o tipo de gráfico para {file_name}',
        ['Gráfico de Barras', 'Gráfico de Dispersão', 'Boxplot', 'Gráfico de Linhas', 'Histograma'],
        key=f"chart_type_{file_name}"
    )

    # Seleção das colunas
    columns = data.columns.tolist()
    x_axis = st.selectbox(f'Selecione a coluna do eixo X para {file_name}', columns, key=f"x_axis_{file_name}")
    y_axis = st.selectbox(f'Selecione a coluna do eixo Y para {file_name}', columns, key=f"y_axis_{file_name}")

    # Gerar gráfico baseado na seleção
    if chart_type == 'Gráfico de Barras':
        st.subheader('Gráfico de Barras')
        plt.figure(figsize=(10, 6))
        data.plot(x=x_axis, y=y_axis, kind='bar')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot(plt)
        plt.close()
    
    elif chart_type == 'Gráfico de Dispersão':
        st.subheader('Gráfico de Dispersão')
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=data, x=x_axis, y=y_axis)
        plt.title(f'{x_axis} vs {y_axis}')
        plt.xticks(rotation=90) 
        st.pyplot(plt)
        plt.close()
    
    elif chart_type == 'Boxplot':
        st.subheader('Boxplot')
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=data, x=x_axis, y=y_axis)
        plt.title(f'{y_axis} by {x_axis}')
        plt.xticks(rotation=90)  
        st.pyplot(plt)
        plt.close()

    elif chart_type == 'Gráfico de Linhas':
        st.subheader('Gráfico de Linhas')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=data, x=x_axis, y=y_axis)
        plt.title(f'{y_axis} over {x_axis}')
        plt.xticks(rotation=90)  
        st.pyplot(plt)
        plt.close()

    elif chart_type == 'Histograma':
        st.subheader('Histograma')
        plt.figure(figsize=(10, 6))
        sns.histplot(data=data, x=x_axis, kde=True)
        plt.title(f'Distribuição de {x_axis}')
        plt.xticks(rotation=90)  
        st.pyplot(plt)
        plt.close()

# Gerar gráficos para ambos os arquivos
gerar_grafico(data_intersectional, "intersectional")
gerar_grafico(data_heart, "heart")
