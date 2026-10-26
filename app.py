import streamlit as st
import pandas as pd
from style import headerStyle, kpiStyle

@st.cache_data
def load_data(path:str) -> pd.DataFrame:
    df=pd.read_csv(path)
    return df

#clean data and feature engineering
@st.cache_data
def clean_data(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"], format="mixed")
    df["order_time"] = pd.to_datetime(df["order_time"], format="mixed").dt.time
 
    # Feature engineering
    df["Order_Day"]    = df["order_date"].dt.day_name()
    df["Order_Month"]  = df["order_date"].dt.month_name()
    df["month_num"]    = df["order_date"].dt.month
    df["Order_Hour"]   = pd.to_datetime(df["order_time"], format="%H:%M:%S").dt.hour
 
    # Categorical ordering so plots sort correctly
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]
    df["Order_Day"] = pd.Categorical(df["Order_Day"], categories=weekdays, ordered=True)
 
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    df["Order_Month"] = pd.Categorical(df["Order_Month"], categories=months, ordered=True)
 
    return df
#read data using function
df_raw = load_data('Pizza_sales.csv')
df = clean_data(df_raw)



#page Configuration
st.set_page_config(
    page_title='Pizza Sales Dashboard',
    page_icon='🍕',
    layout='wide',
    initial_sidebar_state='auto'
)



st.title('Pizza sales Dashboard')
st.header('KPI')

st.markdown(headerStyle('KPI'),unsafe_allow_html= True)

total_revenue = df ['total_price'].sum()
total_pizza_sold = df['quantity'].sum()
total_orders = df['order_id'].nunique()
average_order_value = total_revenue / total_orders
average_pizza_per_order = total_pizza_sold / total_orders


kpi1, kpi2, kpi3, kpi4,kpi5 = st.columns(5)
kpi1.markdown(kpiStyle('Total Revenue', f"${total_revenue:,.2f}"))
kpi2.markdown(kpiStyle('Total Pizza Sold', f"{total_pizza_sold:,}"))
kpi3.markdown(kpiStyle('Total Orders', f"{total_orders:,}"))
kpi4.markdown(kpiStyle('Average Order Value', f"${average_order_value:,.2f}"))
kpi5.markdown(kpiStyle('Average Pizza per Order', f"{average_pizza_per_order:.2f}"))

st.markdown(headerStyle('Analysis'),unsafe_allow_html= True)
st.header('Analysis')
st.header('Raw Data')
st.dataframe(df)