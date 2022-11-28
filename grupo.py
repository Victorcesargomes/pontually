import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio



st.set_page_config(page_title="Dashboards Grupo NE Segurança", 
layout='wide', page_icon=":bar_chart")

image = Image.open('pontually-removebg.png')
st.image(image, width=600)
st.markdown("---")


st.title("*Quem Somos*")
st.markdown('**Somos uma Empresa Contábil atuando no mercado desde 2008, ajudando centenas de empreendedores a gerir seus negócios. Contamos com profissionais altamente qualificados, especialistas em suas áreas de atuação e comprometidos com o nosso propósito de contribuir para a solidez das empresas em seus respectivos mercados.**')
st.markdown("---")

st.title("*Objetivo do App*")
st.markdown('**Analisar os dados financeiros da empresa tendo como principais variáveis os aspectos da Receita Líquida (Receita Bruta - Impostos e Deduções) e o resultado líquido da Despesa com Folha (Folha de Pagamentos - Descontos e Deduções). Nesse sentido, portanto, o presente App tem como objetivo analisar o impacto da Folha com Pessoal sobre a Receita Corrente Líquida - evidenciando as características quantitavivas e qualitativas das variáveis analisadas.**')

st.markdown("---")
st.title(":bar_chart:Business Intelligence")

st.header("NE SEGURANÇA MATRIZ")

dados = pd.read_csv("ne_seguranca_10.csv", encoding='latin-1', sep=';', decimal=',')

c1, c2 = st.columns(2)

for tem in ["plotly_dark"]:
    fig = px.bar(dados, x='Liquido', y='Cliente',
    labels={"Liquido": "Faturamento Líquido", "Cliente":"Clientes", "Bruto":"Faturamento Bruto"}
    , title="Faturamento por Cliente (10/2022)", template=tem, color_discrete_sequence=["#0083B8"])
    
    c1.plotly_chart(fig)
    c1.markdown("**A Empresa Pandenor apresenta a melhor Receita Líquida. O EDF. Maria da Penha, por sua vez, configura a menor Receita Líquida entre os clientes.**")

for t in ["plotly_dark"]:
    fig1 = px.bar(dados, x='Lucro', y='Cliente', color='Folha', title="Lucro por Cliente (10/2022)",
    labels={"Cliente":"Clientes"}, template=t, color_discrete_sequence=["#0083B8"])
    c2.plotly_chart(fig1)
    c2.markdown("**O cliente Instituto de Vida Consagrada apresentou o melhor Retorno Líquido (Lucro de R$ 29.000,99)**")

st.markdown("---")
c3, c4 = st.columns(2)

for template in ['plotly_dark']:
    fig2 = px.bar(dados,y='Folha', x='Cliente', color='Funcionarios', template=template, 
    title="Folha por Cliente (10/2022)", labels={"Cliente": "Clientes", 'Funcionarios': 'Funcionários'}, color_discrete_sequence=["#0083B8"])
    c3.plotly_chart(fig2)
    c3.markdown("**A empresas TEMAPE configura como um dos clientes com  maior Despesa com Folha. Além disso, a empresa possui 13 funcionários ativos.**")
    

for temas in ["plotly_dark"]:
    fig3 = px.scatter(dados, x='Folha', y='Lucro', color='Liquido',trendline="ols",
     title="Lucro vs Folha (10/2022)",
     template=temas,color_discrete_sequence=["#0083B8"], labels={'Liquido': 'Receita Líquida'})
    
    c4.plotly_chart(fig3)
    c4.markdown("**O gráfico a cima demonstra uma relação positiva entre a Folha e o Lucro, isto é, mesmo com uma Despesa com Folha significativa; o que vai impactar o lucro é o tamaho da Receita. No caso da NE Segurança Matriz, a qualidade da Receita está fortemente ligada ao seu aspecto quantitativo.**")
    #fig3 = px.scatter(dados,x="Cliente", y="Folha", color='Funcionarios',template=template)
    #c4.plotly_chart(fig3)

st.markdown("---")

## Mapa
st.header("**Mapa**")
mapa = dados

map = px.scatter_mapbox(mapa, lat='Lat', lon='Long', hover_name= 'Cliente',
                         color = 'Bruto',
                         hover_data={'Lat':False, 'Long':False,'Liquido':True, 'Lucro':True,
                         'Folha': True, 'Funcionarios': True},
                         size='Liquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=6,height=300, labels={"Bruto": "Faturamento Bruto",
                         "Liquido": "Faturamento Líquido", "Funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)

st.markdown("---")

st.title(":bar_chart:Business Intelligence")
st.header("NE SEGURANÇA AL")

df = pd.read_csv("ne_seguranca_al.csv", encoding='utf-16', sep=',', decimal=',')

c1, c2 = st.columns(2)

figal = px.bar(df, x='Líquido', y='Cliente', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Faturamento Líquido por Cliente (10/2022)",
labels={'Cliente': 'Clientes','Líquido':'Faturamento Líquido'})
c1.plotly_chart(figal)



figal1 = px.bar(df, x='Cliente', y='Lucro', color_discrete_sequence=["#0083B8"],
title="Lucro por CLiente (10/2022)", labels={'Cliente':'Clientes'}, color='Folha', template='plotly_dark')

c2.plotly_chart(figal1)
c2.markdown("**De acordo com o gráfico, o cliente SPE Maceió Ambiental apresentou o maior Resultado Líquido (Lucro) em relação aos demais clientes. No entanto, o cliente possui o maior quantitativo em termos de Folha com Pessoal. O Atacadão Praia, por sua vez, apresentou um prejuízo e ocupa a 2° colocação em termos de gasto com Folha.**")

st.markdown("---")

st.header("**Mapa**")
mapa = df

map = px.scatter_mapbox(mapa, lat='Lat', lon='Long', hover_name= 'Cliente',
                         color = 'Bruto',
                         hover_data={'Lat':False, 'Long':False,'Líquido':True, 'Lucro':True,
                         'Folha': True, 'Funcionarios': True},
                         size='Líquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=9,height=300, labels={"Bruto": "Faturamento Bruto",
                         "Líquido": "Faturamento Líquido", "Funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)

st.markdown("---")


st.title(":bar_chart:Business Intelligence")
st.header("NE SEGURANÇA PB")

dfpb = pd.read_csv("ne_seguranca_pb_10.csv", encoding='utf-16', sep=',', decimal=',')

c1, c2 = st.columns(2)

figpb = px.bar(dfpb, x="liquido", y='cliente', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Faturamento Líquido por Cliente (10/2022)",
labels={'cliente': 'Clientes','liquido':'Faturamento Líquido'})
c1.plotly_chart(figpb)

figpb1 = px.bar(dfpb, x="cliente", y='lucro', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Lucro por Cliente (10/2022)",
labels={'cliente': 'Clientes', 'lucro':'Lucro', 'folha': 'Folha'}, color='folha')
c2.plotly_chart(figpb1)
c2.markdown("**O cliente Mixx Mateus Guarabira apresenta Resultado Líquido Negativo (Prejuízo).**")

st.markdown("---")

st.header("**Mapa**")
mapa = dfpb

map = px.scatter_mapbox(mapa, lat='lat', lon='long', hover_name= 'cliente',
                         color = 'bruto',
                         hover_data={'lat':False, 'long':False,'liquido':True, 'lucro':True,
                         'folha': True, 'funcionarios': True},
                         size='liquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=6,height=300, labels={"bruto": "Faturamento Bruto",
                         "liquido": "Faturamento Líquido", "funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)

st.markdown("---")

st.title(":bar_chart:Business Intelligence")
st.header("NE SEGURANÇA RN")

dfrn = pd.read_csv("ne_seguranca_RN_10.csv", encoding='utf-16', sep=',', decimal=',')

c1, c2 = st.columns(2)

figrn = px.bar(dfrn, x="liquido", y='cliente', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Faturamento Líquido por Cliente (10/2022)",
labels={'cliente': 'Clientes','liquido':'Faturamento Líquido'})
c1.plotly_chart(figrn)

figrn1 = px.bar(dfrn, x="cliente", y='lucro', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Lucro por Cliente (10/2022)",
labels={'cliente': 'Clientes', 'lucro':'Lucro', 'folha': 'Folha'}, color='folha')
c2.plotly_chart(figrn1)

st.markdown("---")

st.header("**Mapa**")
mapa = dfrn

map = px.scatter_mapbox(mapa, lat='lat', lon='long', hover_name= 'cliente',
                         color = 'bruto',
                         hover_data={'lat':False, 'long':False,'liquido':True, 'lucro':True,
                         'folha': True, 'funcionarios': True},
                         size='liquido',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=6,height=300, labels={"bruto": "Faturamento Bruto",
                         "liquido": "Faturamento Líquido", "funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)


st.markdown("---")

st.title(":bar_chart:Business Intelligence")
st.header("NE SEGURANÇA SE")

dfse = pd.read_csv("ne_seguranca_se.csv", encoding='utf-16', sep=',', decimal=',')

c1, c2 = st.columns(2)

figse = px.bar(dfse, x="cliente", y='fat', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Faturamento Líquido por Cliente (10/2022)",
labels={'cliente': 'Clientes','fat':'Faturamento Líquido'})
c1.plotly_chart(figse)

figse1 = px.bar(dfse, x="cliente", y='lucro', template="plotly_dark", 
color_discrete_sequence=["#0083B8"], title="Lucro por Cliente (10/2022)",
labels={'cliente': 'Clientes', 'lucro':'Lucro', 'folha': 'Folha'}, color='folha')
c2.plotly_chart(figse1)

st.markdown("---")

st.header("**Mapa**")
mapa = dfse

map = px.scatter_mapbox(mapa, lat='lat', lon='long', hover_name= 'cliente',
                         color = 'bruto',
                         hover_data={'lat':False, 'long':False,'fat':True, 'lucro':True,
                         'folha': True, 'funcionarios': True},
                         size='fat',
                         color_continuous_scale=px.colors.cyclical.IceFire,
                         zoom=4,height=300, labels={"bruto": "Faturamento Bruto",
                         "fat": "Faturamento Líquido", "funcionarios": "N° de Funcionários"})

map.update_layout(mapbox_style='open-street-map')
map.update_layout(height=400, margin={'r':0, 't':0, 'l':0, 'b':0})
st.plotly_chart(map)