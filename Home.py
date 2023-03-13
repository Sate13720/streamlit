import streamlit as st
from multiapp import MultiApp

from apps import Compute, Storage, Credit# import your app modules here

st.set_page_config(page_title="Snowflake Usage App", layout='wide')

col1, col2= st.columns((1,2))

with col1:
    st.image('hexaware.png',  width=300)

with col2:
    st.write("""
## Welcome to the Usage Insights Application
 """)

    st.markdown(
    """
    This app provides insights on a Demo Snowflake account usage.
    """
)
    
st.write("---")
st.write("### Get started!")
app = MultiApp()   



# Add all your application here
app.add_app("Compute Insights", Compute.app)
app.add_app("Storage Insights", Storage.app)
app.add_app("Credit Insights", Credit.app)

# The main app
app.run()



