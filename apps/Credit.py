import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    
    st.write('---')
    st.write("""
    ### Credit Used Insights
    """)

    df = pd.read_csv(r'csv\credit_used_by_warehouse.csv')
    df1 = pd.read_csv(r'csv\warehouse_usage_hourly.csv')
    df2 = pd.read_csv(r'csv\warehouse_usage_daily.csv')

    st.sidebar.header("Filters")

    warehouse = st.sidebar.multiselect("Warehouse Name",options = df["WAREHOUSE_NAME"].unique(),default = df["WAREHOUSE_NAME"].unique()) 
    
    df_selection = df.query("WAREHOUSE_NAME == @warehouse")
    st.write( """
    #### Total Credit used by Warehouse 
    """)
    st.dataframe(df)
    # st.bar_chart(df_selection, x="WAREHOUSE_NAME", y="TOTAL_CREDITS_USED")
    fig = px.pie(df_selection, names = 'WAREHOUSE_NAME', values = 'TOTAL_CREDITS_USED',
     title='Total Credit used by Warehouse ')
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    df_selection1 = df1.query("WAREHOUSE_NAME == @warehouse")
    st.write( """
    #### Hourly Credit used by Warehouses 
    """)
    st.line_chart(df_selection1, x="START_TIME", y="CREDITS_USED_COMPUTE")

    df_selection2 = df2.query("WAREHOUSE_NAME == @warehouse")
    st.write( """
    #### Daily Credit used by Warehouses 
    """)
    st.bar_chart(df_selection2, x="USAGE_DATE", y="TOTAL_CREDITS_USED")


 