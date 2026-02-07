import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Previsor de Preços", page_icon="🏠")

st.title("🏠 Meu Primeiro App de ML")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_modelo = os.path.join(diretorio_atual, 'modelo_casas.pkl')

if not os.path.exists(caminho_modelo):
    st.error(f"Erro: O arquivo '{caminho_modelo}' não foi encontrado. Rode o 'python train.py' primeiro!")
else:
    model = joblib.load(caminho_modelo)
    st.success("Cérebro do modelo carregado com sucesso!")

    col1, col2 = st.columns(2)
    with col1:
        lot_area = st.number_input("Tamanho do Lote", value=8000)
        year_built = st.number_input("Ano de Construção", value=2010)
        first_flr = st.number_input("Área 1º Andar", value=1200)
        second_flr = st.number_input("Área 2º Andar", value=0)
    with col2:
        bath = st.number_input("Banheiros", value=2)
        rooms = st.number_input("Quartos", value=3)
        total_rooms = st.number_input("Total de Cômodos", value=6)

    if st.button("Prever Preço"):
        input_data = pd.DataFrame([[lot_area, year_built, first_flr, second_flr, bath, rooms, total_rooms]], 
                                 columns=['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd'])
        
        predicao = model.predict(input_data)
        st.balloons() 
        st.metric(label="Preço Estimado", value=f"US$ {predicao[0]:,.2f}")