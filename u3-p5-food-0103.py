import pandas as pd
import matplotlib.pyplot as plt
## Santiago Medrano NC 0103
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV comida India 0103 ---")
print(df_food_india)
print("\n--- Mostrar nombre comida + ingrediantes, comida India 0103 ---")
recipes = df_food_india [['name', 'ingredients']]
print(recipes)
print("\n---tiempo de cocinado mostrar 10 registros con head 0103 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)