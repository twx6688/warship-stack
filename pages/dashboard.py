# pages/dashoard.py

import pandas as pd
import streamlit as st

from helpers import conn_engin

st.title('Dashboard')


engine = conn_engin.get_engine()

query = "SELECT * FROM ipg_ez LIMIT 100"
df = pd.read_sql(query, engine)
st.dataframe(df)