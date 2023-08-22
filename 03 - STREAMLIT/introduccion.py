

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



st.markdown("## Analisis Exploratorio (EDA)")

st.markdown("***")

st.markdown("### En nuestro analisis EDA tuvimos como objetivos las siguientes premisas:")

st.markdown("####  * Capitalizacion de Mercado")

st.markdown("####  * Precio del Activo cripto")

st.markdown("####  * Volumen ")

st.markdown("####  * Exchange mas confiables")

st.markdown("***")

st.markdown("## ¿Por que es inportante saber estos 4 puntos a la hora de pensar en cripto-monedas?")


st.markdown("### 1 - Capitalizacion de Mercado")
st.markdown("La capitalización del mercado es un indicador que mide y sigue el valor de mercado de una criptomoneda. En general, cuanto más alta sea la capitalización del mercado de una criptomoneda, más dominante se considerará esta en el mismo. Por esta razón, la capitalización del mercado suele considerarse el indicador más importante a la hora de clasificar las criptomonedas.")

st.markdown("### 2 - Precio de la moneda")
st.markdown("El valor de una criptomoneda cambia constantemente. El valor de una criptomoneda puede cambiar rápidamente, incluso cada hora. Y el monto de esa fluctuación puede ser considerable. Su valor depende de muchos factores, incluyendo la oferta y la demanda. Las criptomonedas tienden a ser más volátiles que las inversiones tradicionales, como los bonos y acciones.")

st.markdown("### 3 - Exchanges")
st.markdown("Un exchange de criptomonedas es la plataforma en la que se realizan los intercambios de estas a dinero fíat o a otras criptomonedas. En estas casas de cambio online es donde se genera el precio de mercado que finalmente marca el valor de las criptomonedas en base a la oferta y demanda.")

st.markdown("### 4 - Volumen ")
st.markdown("El volumen, también conocido como “volumen de negociación”, es el número de tokens, contratos u otras unidades operadas en un mercado durante un período de tiempo específico.")

st.markdown("***")

st.markdown("### 1 - Capitalizacion de Mercado")

st.markdown("**Estas son las 10 Criptomonedas de mayor capitalizacion**")

mayor_cap=pd.read_csv("../00 - DATA\mayor_cap.csv")


fig = plt.figure(figsize=(12,4))
ax=sns.barplot(x ='name', y ='market_cap',data=mayor_cap)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 30)
ax. set (xlabel = ' Moneda / Coin',
       ylabel = ' Capitalizacion  ',
       title = ' Capitalizacion de Mercado ')

st.pyplot(fig)

st.markdown("***En el grafico podemos observar las 10 monedas de mayor capitalizacion de mercado, y notamos que el Bitcoin esta capitalizada mas de el doble que la segunda moneda mayor capitalizada.-***")

st.dataframe(mayor_cap)

st.markdown("### Aca veremos como fueron capitalizadas las monedas a lo largo de 5 años")


st.markdown("***")

Moneda_cap_hist=pd.read_csv("Moneda_cap_hist.csv")
Moneda_cap_hist['Fecha'] = pd.to_datetime(Moneda_cap_hist['Fecha'])

fig2 = plt.figure(figsize=(12,6))

ax = sns.lineplot(x="Fecha", y="Market_Cap",
             hue="Moneda",
             data=Moneda_cap_hist)
ax. set (xlabel = 'Fecha',
       ylabel = ' Capitalizacion  ',
       title = ' Capitalizacion de Mercado ')

st.pyplot(fig2)

st.markdown("***En Este grafico se observa como otras monedas se van capitalizando a lo largo de estos 5 años.-***")

st.markdown("***")

st.markdown("## Precio Historico de las Monedas.-")

Precio_Total=pd.read_csv("Precio_Total.csv")
Precio_Total['Fecha'] = pd.to_datetime(Precio_Total['Fecha'])

fig3 = plt.figure(figsize=(12,6))
# Plot the responses for different events and regions
ax = sns.lineplot(x="Fecha", y="prices",
             hue="Moneda",
             data=Precio_Total)
ax. set (xlabel = 'Fecha',
       ylabel = 'Precio',
       title = ' Historico de Precio ')

st.pyplot(fig3)


st.markdown("***Aca observamos que el precio de la moneda estan completamente sesgadas por el bitcoin a lo largo de la historia.***")

st.markdown("**A continuacion se los detallo en 4 graficos distintos para que se vea la volatividad de cada grupo**")


moneda_precio_alto=pd.read_csv("moneda_precio_alto.csv")
moneda_precio_alto['Fecha'] = pd.to_datetime(moneda_precio_alto['Fecha'])

fig4 = plt.figure(figsize=(12,6))
ax = sns.lineplot(x="Fecha", y="prices",
             hue="Moneda",
             data=moneda_precio_alto)
ax. set (xlabel = 'Fecha',
       ylabel = 'Precio',
       title = ' Historico de Precio ')

st.pyplot(fig4)


st.markdown("El Bitcoin es una de las monedas de mayor precio y fluctuacion del mercado de Cripto, es mas se hace en un grafico propio, por que el sezgo entre las otras en mayor a 1000%-")



moneda_precio_medio=pd.read_csv("moneda_precio_medio.csv")
moneda_precio_medio['Fecha'] = pd.to_datetime(moneda_precio_medio['Fecha'])
fig5 = plt.figure(figsize=(12,6))
ax = sns.lineplot(x="Fecha", y="prices",
             hue="Moneda",
             data=moneda_precio_medio)
ax. set (xlabel = 'Fecha',
       ylabel = 'Precio',
       title = ' Historico de Precio ')
st.pyplot(fig5)

st.markdown("Estas dos monedas extrechamente ligadas por ser una dependiente de una de otras oscilaron en un precio de 200 a 5000 dolares los ultimos 5 años.-")

moneda_precio_Bajo=pd.read_csv("moneda_precio_Bajo.csv")
moneda_precio_Bajo['Fecha'] = pd.to_datetime(moneda_precio_Bajo['Fecha'])
fig6 = plt.figure(figsize=(12,6))
ax = sns.lineplot(x="Fecha", y="prices",
             hue="Moneda",
             data=moneda_precio_Bajo)
ax. set (xlabel = 'Fecha',
       ylabel = 'Precio',
       title = ' Historico de Precio ')
st.pyplot(fig6)

st.markdown("Aca Observamos dos monedas que que oscilan entre 25 y 700 Dolares.-")

moneda_precio_estable=pd.read_csv("moneda_precio_estable.csv")
moneda_precio_estable['Fecha'] = pd.to_datetime(moneda_precio_estable['Fecha'])
fig7 = plt.figure(figsize=(12,6))

ax = sns.lineplot(x="Fecha", y="prices",
             hue="Moneda",
             data=moneda_precio_estable)
ax.set(xlabel = 'Fecha', ylabel = 'Precio', title = ' Historico de Precio ')
st.pyplot(fig7)

st.markdown("Aca tenemos las monedas restantes encontramos las que oscilaron entre 0.1 y 3 dolares y las stablescoin monedas que a pesar de todo el movimientos simpre va a valer lo mismos.-")

st.markdown("***")

st.markdown("# Volumen")

Volumen=pd.read_csv("volumen.csv")
Volumen['Fecha'] = pd.to_datetime(Volumen['Fecha'])


fig8 = plt.figure(figsize=(12,6))

ax = sns.lineplot(x="Fecha", y="total_volumes",
             hue="Moneda",
             data=Volumen)
ax. set (xlabel = 'Fecha',
       ylabel = 'Volumen',
       title = ' Historico de Volumen ')
st.pyplot(fig8)

st.markdown("Aca vemos el Volumen en el transcurso de 5 años y el BTC siempre fue la moneda de intercambio de todas las monedas.-")


st.markdown("***")

st.markdown("# Exchange")

Exchance=pd.read_csv("Exchange.csv")

fig9 = plt.figure(figsize=(12,6))
ax=sns.barplot(x ='name', y ='trade_volume_24h_btc_normalized',data=Exchance)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 30)
ax. set (xlabel = ' Exchance ',
       ylabel = ' Volumen ',
       title = ' Volumen de movimientos en las ultimas 24 horas ')

st.pyplot(fig9)

st.markdown("## Y aca estan los 5 Exchange que mayor volumen de mercado")


