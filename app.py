import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Título principal
st.title("Impacto da ONG Passos Mágicos")
st.write("Um olhar detalhado sobre a evolução e os resultados dos estudantes atendidos pela ONG.")

# Carregar a base de dados
st.sidebar.header("Upload de Arquivo CSV")
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo CSV", type=["csv"])

# Verifica se o arquivo foi carregado
if uploaded_file is not None:
    # Lendo o arquivo CSV
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Dados carregados com sucesso!")
        
        # Mostrando os primeiros dados para validação
        st.dataframe(df.head())
        
        # Renomeando as colunas para manter o padrão do código
        df.rename(
            columns={
                'ano': 'Ano',
                'indice_desenvolvimento_educacional_medio': 'INDE_Medio',
                'proporcao_ponto_virada': 'Ponto_Virada_Proporcao',
                'indice_engajamento_medio': 'Engajamento_Medio',
                'indice_psicossocial_medio': 'IPS_Medio',
                'nivel_quartzo': 'Quartzo',
                'nivel_agata': 'Agata',
                'nivel_ametista': 'Ametista',
                'nivel_topazio': 'Topazio'
            },
            inplace=True
        )

        # Verificando se todas as colunas estão no DataFrame
        required_columns = ['Ano', 'INDE_Medio', 'Ponto_Virada_Proporcao', 
                            'Engajamento_Medio', 'IPS_Medio', 'Quartzo', 
                            'Agata', 'Ametista', 'Topazio']

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"As seguintes colunas estão faltando no arquivo: {', '.join(missing_columns)}")
            st.stop()

        # Continuando com os gráficos
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

        # Gráfico 2: Distribuição das Pedras (barras empilhadas)
        st.subheader("Distribuição das 'Pedras' por Ano")
        fig_pedras = px.bar(
            df, x='Ano', y=['Quartzo', 'Agata', 'Ametista', 'Topazio'],
            title="Distribuição das 'Pedras' por Ano",
            labels={"value": "Quantidade de Estudantes", "Ano": "Ano"},
            barmode='stack'
        )
        st.plotly_chart(fig_pedras)

        # Gráfico 3: Proporção do Ponto de Virada (pizza)
        st.subheader("Proporção de Estudantes que Atingiram o Ponto de Virada")
        fig_pv = px.pie(
            names=df['Ano'],
            values=df['Ponto_Virada_Proporcao'],
            title="Proporção de Estudantes que Atingiram o Ponto de Virada",
            labels={"value": "Proporção", "Ano": "Ano"}
        )
        st.plotly_chart(fig_pv)

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

        # Recomendações
        st.header("Recomendações")
        st.write("""
        - Expandir atividades que promovam o "Ponto de Virada", visto que este indicador impacta diretamente o INDE.
        - Oferecer suporte psicológico adicional aos alunos com baixo IPS, que apresentam maior dificuldade em progredir.
        - Ampliar o acompanhamento personalizado para alunos em "Quartzo" e "Ágata" para acelerar o avanço em suas classificações.
        """)
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
else:
    st.warning("Nenhum arquivo carregado. Selecione um arquivo na barra lateral.")
