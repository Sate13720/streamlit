import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def app():
# Title of Page 
   
    st.write('---')
    st.write("""
    ### Storage Insights
    """)

    df2 = pd.read_csv(r'csv\bytes_consumed_by_database.csv')

    st.sidebar.header("Filters")
    
    database = st.sidebar.multiselect("DATABASE_NAME",options = df2["DATABASE_NAME"].unique(),default = df2["DATABASE_NAME"].unique())   

    
    df_selection = df2.query("DATABASE_NAME == @database")
    st.write( """
    #### Average Database bytes consumed by Database
    """)
    st.table(df2)
    # st.bar_chart(df_selection, x="DATABASE_NAME", y="AVERAGE_DATABASE_BYTES")
    fig = px.pie(df_selection, names = 'DATABASE_NAME', values = 'AVERAGE_DATABASE_BYTES',
     title='Average Database bytes consumed by Database')
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    df_selection = df2.query("DATABASE_NAME == @database")
    st.write( """
    #### Average Failsafe bytes consumed by Database
    """)
    st.bar_chart(df_selection, x="DATABASE_NAME", y="AVERAGE_FAILSAFE_BYTES")


    df_selection = df2.query("DATABASE_NAME == @database")
    st.write( """
    #### Databytes consumed by Database Daily
    """)
    st.bar_chart(df_selection, x='USAGE_DATE', y="AVERAGE_DATABASE_BYTES")




