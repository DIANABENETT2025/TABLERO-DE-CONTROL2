import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ruta = "https://github.com/VMjavier/claseAnalisisDatos/raw/refs/heads/main/datos_reales.zip"
df = pd.read_csv(ruta)

print(df.head())


n = 10 # Número de variables más comunes a mostrar
columna = "Crime" # Cambia esto por la columna que desees analizar

topN = df[columna].value_counts().nlargest(n).index
plt.figure(figsize=(10,6))
sns.countplot(data=df[df[columna].isin(topN)], 
              x=columna, 
              order=topN, 
              palette="tab10")

plt.title("Top n tipos de crimen", fontsize=14)#<-- Cambia el título según la columna
plt.xlabel("Tipo de crimen") #<-- Cambia la etiqueta según la columna
plt.ylabel("Número de casos") #<-- Cambia la etiqueta según la columna
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("img/graficoHurto.png", dpi=300, bbox_inches="tight")
plt.show()