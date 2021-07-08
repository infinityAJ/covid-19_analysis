import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="covid data analysis")

pages = [
    'Home',
    'India Total',
    'World Total',
    'Country Wise Analysis',
    'State Wise Analysis of India'
    ]

st.sidebar.title("covid-19 data analysis")
choice = st.sidebar.selectbox('Choose a page', pages)

# global functions?
@st.cache
def load_data():
    df = pd.read_csv('covid_19_data.csv')
    return df

def get_indian_data():
    df = load_data()
    df = df[df["Country/Region"] == 'India']
    return df

# page 1 fucntions
def get_raw():
    df = load_data()
    x = 10
    st.header("A slight look of the data")
    st.write("  ")
    st.write(df.head(x))
    st.markdown("<hr>", unsafe_allow_html= True)
    col1, col2 = st.beta_columns(2)
    col1.subheader("Number of Rows:")
    col1.write(df.shape[0])
    col2.subheader("Number of Columns:")
    col2.write(df.shape[1])
    st.markdown("<hr>", unsafe_allow_html= True)

    st.header("Dataset Summary")
    st.write(" ")
    st.write(df.describe())

    st.header("Columns description")
    for i in df.columns:
        st.subheader(i)
        col1, col2 = st.beta_columns(2)
        col1.caption("Unique Values")
        col1.write(len(df[i].unique()))
        col2.caption("Type of Data")
        col2.write("String of Characters" if type(df[i].iloc[0]) is str else "Numerical")
        st.markdown("<hr>",unsafe_allow_html = True)

# page 2 functions
def india_group_date():
    df = get_indian_data()
    df = df.rename(columns={'ObservationDate':'date'})
    df = df.groupby('date', as_index=False).sum()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values('date')
    return df

def get_death():
    df = india_group_date()
    fig = px.line(df, 'date', 'Deaths')
    return fig

def get_recovery():
    df = india_group_date()
    fig = px.line(df, 'date', 'Recovered')
    return fig

def get_confirm():
    df = india_group_date()
    fig = px.line(df, 'date', 'Confirmed')
    return fig

# page 3 functions
def get_world_data():
    df = load_data()
    df = df.rename(columns={'ObservationDate':'date'})
    df = df.groupby('date', as_index=False).sum()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values('date')
    return df

def get_world_death():
    df = get_world_data()
    fig = px.line(df, 'date', 'Deaths')
    return fig

def get_world_recovery():
    df = get_world_data()
    fig = px.line(df, 'date', 'Recovered')
    return fig

def get_world_confirm():
    df = get_world_data()
    fig = px.line(df, 'date', 'Confirmed')
    return fig

# page 4 functions
def get_country():
    df = load_data()
    df = df.groupby('Country/Region', as_index=False).sum()
    return df

def get_country_death():
    df = get_country()
    fig = px.bar(df, 'Country/Region', 'Deaths')
    return fig

def get_country_recovery():
    df = get_country()
    fig = px.bar(df, 'Country/Region', 'Recovered')
    return fig

def get_country_confirm():
    df = get_country()
    fig = px.bar(df, 'Country/Region', 'Confirmed')
    return fig

# page 4 functions
def state_wise():
    df = get_indian_data()
    df = df.groupby("Province/State", as_index=False).sum()
    return df

def get_state_death():
    df = state_wise()
    fig = px.bar(df, 'Province/State', 'Deaths')
    return fig

def get_state_recovery():
    df = state_wise()
    fig = px.bar(df, 'Province/State', 'Recovered')
    return fig

def get_state_confirm():
    df = state_wise()
    fig = px.bar(df, 'Province/State', 'Confirmed')
    return fig

if choice == pages[0]:    
    st.title('Covid-19 Data Analysis')
    get_raw()

if choice == pages[1]:
    st.header("Data of India")
    st.plotly_chart(get_death())
    st.plotly_chart(get_recovery())
    st.plotly_chart(get_confirm())

if choice == pages[2]:
    st.header("Data of Whole World")
    st.plotly_chart(get_world_death())
    st.plotly_chart(get_world_recovery())
    st.plotly_chart(get_world_confirm())

if choice == pages[3]:
    st.header("Country wise Analysis")
    st.plotly_chart(get_country_death())
    st.plotly_chart(get_country_recovery())
    st.plotly_chart(get_country_confirm())

if choice == pages[4]:
    st.header("State wise Analysis")
    st.plotly_chart(get_state_death())
    st.plotly_chart(get_state_recovery())
    st.plotly_chart(get_state_confirm())
