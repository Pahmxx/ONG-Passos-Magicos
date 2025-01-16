import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Dados fictícios baseados na narrativa
data = {
    'Ano': [2020, 2021, 2022],
    'INDE_Medio': [6.0, 7.5, 8.3],
    'Ponto_Virada_Proporcao': [0.3, 0.5, 0.7],
    'Engajamento_Medio': [5.8, 6.7, 7.8],
    'IPS_Medio': [6.2, 7.0, 7.5],
    'Quartzo': [50, 30, 20],
    'Agata': [30, 40, 35],
    'Ametista': [15, 20, 30],
    'Topazio': [5, 10, 15]
}

df = pd.DataFrame(data)

# Título principal
st.title("Impacto da ONG Passos Mágicos")
st.write("Um olhar detalhado sobre a evolução e os resultados dos estudantes atendidos pela ONG entre 2020 e 2022.")

# Seções
st.header("Objetivo")
st.write("Demonstrar o impacto da ONG \"Passos Mágicos\" no desempenho educacional e social dos estudantes atendidos, utilizando dados quantitativos e qualitativos.")

st.header("Narrativa Central")
st.write("\"A educação transforma vidas. O trabalho da Passos Mágicos tem promovido avanços significativos no desempenho educacional e no engajamento dos jovens em vulnerabilidade social. Vamos explorar o impacto por meio dos dados e revelar as histórias por trás dos números.\"")

st.header("Gráficos e Análises")

# Gráfico 1: Evolução do INDE (linha temporal)
st.subheader("Evolução do INDE Médio (2020-2022)")
fig_inde = px.line(
    df, x='Ano', y='INDE_Medio',
    title="Evolução do INDE Médio (2020-2022)",
    markers=True,
    labels={"INDE_Medio": "INDE Médio", "Ano": "Ano"}
)
st.plotly_chart(fig_inde)
st.write("O INDE (Índice de Desenvolvimento Educacional) médio apresentou um crescimento consistente entre 2020 e 2022, indicando melhorias significativas no desempenho educacional geral dos estudantes.")

# Gráfico 2: Distribuição das Pedras (barras empilhadas)
st.subheader("Distribuição das 'Pedras' por Ano")
fig_pedras = px.bar(
    df, x='Ano', y=['Quartzo', 'Agata', 'Ametista', 'Topazio'],
    title="Distribuição das 'Pedras' por Ano",
    labels={"value": "Quantidade de Estudantes", "Ano": "Ano"},
    barmode='stack'
)
st.plotly_chart(fig_pedras)
st.write("Os estudantes demonstraram progresso ao longo dos anos, com uma diminuição na proporção de alunos em 'Quartzo' e 'Ágata' e um aumento em 'Ametista' e 'Topázio'.")

# Gráfico 3: Proporção do Ponto de Virada (pizza)
st.subheader("Proporção de Estudantes que Atingiram o Ponto de Virada")
fig_pv = px.pie(
    names=df['Ano'],
    values=df['Ponto_Virada_Proporcao'],
    title="Proporção de Estudantes que Atingiram o Ponto de Virada",
    labels={"value": "Proporção", "Ano": "Ano"}
)
st.plotly_chart(fig_pv)
st.write("A proporção de estudantes que alcançaram o 'Ponto de Virada' aumentou de forma significativa, mostrando o impacto direto das intervenções realizadas pela ONG.")

# Gráfico 4: Correlação entre IPS e INDE (heatmap)
st.subheader("Correlação entre IPS e INDE")
heatmap_data = pd.DataFrame(
    np.corrcoef([df['IPS_Medio'], df['INDE_Medio']]),
    columns=["IPS Médio", "INDE Médio"],
    index=["IPS Médio", "INDE Médio"]
)
fig_corr = px.imshow(
    heatmap_data,
    text_auto=True,
    color_continuous_scale="Viridis",
    title="Correlação entre IPS e INDE"
)
st.plotly_chart(fig_corr)
st.write("A análise de correlação revela uma forte relação entre o Indicador Psicossocial (IPS) e o INDE, destacando a importância do suporte psicossocial no desempenho educacional.")

# Recomendações
st.header("Recomendações")
st.write("""
- Expandir atividades que promovam o "Ponto de Virada", visto que este indicador impacta diretamente o INDE.
- Oferecer suporte psicológico adicional aos alunos com baixo IPS, que apresentam maior dificuldade em progredir.
- Ampliar o acompanhamento personalizado para alunos em "Quartzo" e "Ágata" para acelerar o avanço em suas classificações.
""")

# Instruções para execução no Google Colab
st.sidebar.header("Instruções para Google Colab")
st.sidebar.write("1. Instale as bibliotecas: `!pip install streamlit pyngrok`.")
st.sidebar.write("2. Rode o comando `!streamlit run app.py`.")
st.sidebar.write("3. Use o Pyngrok para gerar um link público do Streamlit.")
