import pandas as pd
import streamlit as st
import plotly.express as px

url = 'https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/fiscalia/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding='utf-8')

#st.dataframe(df)

#Crea lista de las columnas que me interasan en su propio orden:
selected_columns = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
#Actualizar el dtaframe -df- con las columnas de interes ordendas por fecha y reseteo de indice:
df = df[selected_columns].sort_values(by='FECHA_HECHOS', ascending=True). reset_index(drop=True)

#Convertir fecha object a fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')

df_serie_tiempo = df.copy()
#Extraigo solo la fecha sin hora
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date
#st.dataframe(df)

#Cálculo de los municipio con mas delitos
#.upper() para poner en mayuscula
max_municipio = df ['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
#st.write(max_municipio)

max_cantidad_municipio = df ['MUNICIPIO_HECHOS'].value_counts().iloc[0]
#st.write(f'## Cantidad de Eventos: {max_cantidad_municipio}')



#--------------------------------------------------CONSTRUIR LA PÁGINA
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="wide")
st.markdown(
    """

    <style>
    .block-container {
        padding-top: 1rem 2rem 2rem 2rem;
        max-width: 1600px;  
        }  
    
    </style>
    
    """,
    unsafe_allow_html=True


)
#Para alargar la imagen
st.image('img/encabezado.jpg',use_container_width=True)


#st.subheader("Tipo de Delito")
#delitos = df['DELITO'].value_counts()
#st.bar_chart(delitos)

#CALCULO DE ETAPA MAS RECURRENTE- MAS VECES SE PRESENTA
etapa_mas_frecuente= df['ETAPA'].value_counts().index[0]
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]
st.write(f"## Etapa más frecuente: {etapa_mas_frecuente} con {cant_etapa_mas_frecuente} reportes")
st.header("Tipo de Delito")
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

Departamento_mas_frecuente = df['DEPARTAMENTO'].value_counts()
Departamentos_con_mas_casos = df['DEPARTAMENTO'].value_counts().iloc[0]
st.write(Departamentos_con_mas_casos)

st.header("Departamentos con más casos")
departamento = df['DEPARTAMENTO'].value_counts()
st.bar_chart(departamento)

# Imagen de torta
st.header('Distribucion por Departamento')
fig= px.pie(
values=Departamento_mas_frecuente.values,
names=Departamento_mas_frecuente.index
)
st.plotly_chart(fig)

# Grafico de barras apiladas
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig)

df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig)
st.write(df_delitos)

st.header("Tipo de Delito")
delitos=df['DELITO'].value_counts()
st.bar_chart(delitos)

#CREAR 4 COLUMNAS PARA LAS TARJETAS
col1, col2, col3, col4 = st.columns(4)


#crear columnas para tarjetas
col1, col2, col3, col4 = st.columns(4)




#TARJETA 1
with col1:   
    st.markdown (f"""<h3 style=
             'color:#black;
             background-color:#5E92BF;
             border:2px solid #5176A6;
             border-radius: 10px;
             padding: 10px;
             text-align: center'> 
             Municipio con mas delitos: {max_municipio}</h3><br>""",
             unsafe_allow_html=True)



#TARJETA 2
with col2:
    st.markdown (f"""<h3 style=
             'color:#black;
             background-color:#5E92BF;
             border:2px solid #5176A6;
             border-radius: 10px;
             padding: 10px;
             text-align: center'>Delitos Reportados:<br> {max_cantidad_municipio} delitos.</h3><br>""",unsafe_allow_html=True)





