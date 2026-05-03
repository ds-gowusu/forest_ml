import streamlit as st 
import pandas as pd

st.set_page_config(layout='wide')

ba_df = pd.read_csv('prov_ba.csv')
spha_df = pd.read_csv('spha.csv')

col1, col2 = st.columns([3, 3], gap='large')

with col1:
    st.markdown("### Basal Area Per Provenances")

    st.bar_chart(
        data=ba_df,
        x='Provenance2', 
        y='ba_per_ha', 
        x_label='Provenance',
        y_label='Basal Area (m$^2$/ha)'
    )

with col2:
    st.markdown("### Stands Per Hectare")

    st.bar_chart(
        data=spha_df,
        x='Provenance2',
        y='stems_per_ha',
        x_label='Provenance',
        y_label='Stems Per Hectare'
    )
