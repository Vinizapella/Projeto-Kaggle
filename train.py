import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

train_data = pd.read_csv('train.csv')
y = train_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = train_data[features]

final_model = RandomForestRegressor(n_estimators=100, random_state=1)
final_model.fit(X, y)

joblib.dump(final_model, 'modelo_casas.pkl')
print("Sucesso! Modelo treinado e salvo.")