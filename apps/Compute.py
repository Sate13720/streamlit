import streamlit as st
import pandas as pd
import plotly.express as px 
# import pyplot

# st.set_page_config(layout='wide')

def app():
    # Title of Page 
    st.write('---')
    st.write("""
    ### Compute Usage
    """)

    df = pd.read_csv(r'csv\No_of_jobs_according_to_warehouse.csv')
    df1 = pd.read_csv(r'csv\Average_execution_time_by_user.csv')

    st.sidebar.header("Filters")   

    username = st.sidebar.multiselect("User Name",options = df1["USER_NAME"].unique(),default = df1["USER_NAME"].unique())
    warehouse = st.sidebar.multiselect("Warehouse Name",options = df["WAREHOUSE_NAME"].unique(),default = df["WAREHOUSE_NAME"].unique())
    selected_year = st.sidebar.selectbox('Year', list(reversed(range(2022,2024))))

    st.table(df1)
    df_selection1 = df1.query("USER_NAME == @username")
    st.write("""
    #### Average execution time by each user
    """)
    st.area_chart(df_selection1,  x="USER_NAME", y="AVERAGE_EXECUTION_TIME")

    st.table(df)
    df_selection = df.query("WAREHOUSE_NAME == @warehouse")
    st.write( """
    #### Number of jobs performed by each Warehouse
    """)
    # st.bar_chart(df_selection, x="WAREHOUSE_NAME", y="NUMBER_OF_JOBS")
    fig = px.pie(df, names = 'WAREHOUSE_NAME', values = 'NUMBER_OF_JOBS',
     title='Number of jobs performed by each Warehouse')
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
