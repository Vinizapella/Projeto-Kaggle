# 🏠 Previsão de Preços de Casas - Kaggle Ames Housing

Este projeto foi desenvolvido como parte do desafio **"Housing Prices Competition for Kaggle Learn Users"** do Kaggle. A aplicação utiliza Machine Learning para estimar o valor de venda de imóveis em Ames, Iowa, com base em características estruturais.

### 🔗 Link da Aplicação Online
> **Acesse o App aqui:** [https://projeto-kagglegit-rgwkz5z2ms2km46awzuhra.streamlit.app/](https://projeto-kagglegit-rgwkz5z2ms2km46awzuhra.streamlit.app/)

---

## 📊 Sobre o Projeto
O projeto demonstra um fluxo de trabalho completo em Ciência de Dados, cobrindo desde a análise e treinamento do modelo até o deploy em produção usando uma interface web.

### 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.13
* **Machine Learning:** Scikit-Learn (`RandomForestRegressor`)
* **Manipulação de Dados:** Pandas
* **Interface Web:** Streamlit
* **Deploy:** Streamlit Community Cloud
* **Versionamento:** GitHub

## 🤖 O Modelo de Machine Learning
O modelo utiliza o algoritmo **Random Forest** para prever o `SalePrice`. As variáveis (*features*) selecionadas para a predição foram:

| Variável | Descrição |
| :--- | :--- |
| **LotArea** | Tamanho do lote em pés quadrados |
| **YearBuilt** | Ano original de construção |
| **1stFlrSF** | Área do primeiro andar (sq ft) |
| **2ndFlrSF** | Área do segundo andar (sq ft) |
| **FullBath** | Quantidade de banheiros completos |
| **BedroomAbvGr** | Quantidade de quartos acima do solo |
| **TotRmsAbvGrd** | Total de cômodos (exceto banheiros) |

## 📁 Estrutura do Repositório
* `app.py`: Script principal que contém a interface do site e a lógica de predição.
* `train.py`: Script de treinamento que gera o arquivo do modelo.
* `modelo_casas.pkl`: O modelo treinado e serializado (binário).
* `requirements.txt`: Lista de dependências necessárias para rodar o projeto na nuvem.

---

## 🚀 Como Executar Localmente


```bash
# 1. Clone o repositório
git clone https://github.com/vinizapella/projeto-kaggle.git

# 2. Entre na pasta
cd projeto-kaggle

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode a aplicação
streamlit run app.py
```

A aplicação deve abrir automaticamente no navegador em:
http://localhost:8501

---

Desenvolvido por **Vinícius Zapella**  🚀
