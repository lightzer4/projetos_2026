import streamlit as st
import plotly.express as px
from dados import gerar_dados

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("Dashboard de Vendas")

df = gerar_dados()

# Filtro na barra lateral
categoria = st.sidebar.multiselect(
    "Filtrar categoria",
    options=df["categoria"].unique(),
    default=df["categoria"].unique()
)
df_filtrado = df[df["categoria"].isin(categoria)]

# KPIs no topo
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R$ {df_filtrado['vendas'].sum():,.0f}")
col2.metric("Total de Lucro",  f"R$ {df_filtrado['lucro'].sum():,.0f}")
col3.metric("Ticket Médio",    f"R$ {df_filtrado['vendas'].mean():,.0f}")

# Gráficos
col_a, col_b = st.columns(2)

with col_a:
    fig_linha = px.line(
        df_filtrado.groupby("mes")["vendas"].sum().reset_index(),
        x="mes", y="vendas",
        title="Vendas por Mês"
    )
    st.plotly_chart(fig_linha, use_container_width=True)

with col_b:
    fig_pizza = px.pie(
        df_filtrado.groupby("categoria")["vendas"].sum().reset_index(),
        names="categoria", values="vendas",
        title="Vendas por Categoria"
    )
    st.plotly_chart(fig_pizza, use_container_width=True)

fig_barra = px.bar(
    df_filtrado, x="mes", y="vendas",
    color="categoria", barmode="group",
    title="Comparativo por Categoria e Mês"
)
st.plotly_chart(fig_barra, use_container_width=True)