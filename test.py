from exp import explyap
import pandas as pd
import openpyxl
data=pd.read_excel(r"C:\Users\salah\OneDrive\Bureau\Projet\Rentabilites_quotidiennes\PEUGEOTTEST.xlsx")
df = pd.DataFrame(data)
print(df)
#print(df["0066353235828410795"])
bdserie=df["Rentabilité"].tolist()

print("L'exposant de Lyapunov vaut : " ,explyap(bdserie,7, 2,10e-3))