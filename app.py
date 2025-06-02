import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
EXCEL_FILE = 'damagefactor.xlsx'
SHEET_NAME = 'raw'

@st.cache_data
def load_data():
    df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)
    return df

df = load_data()
#st.write("Columns in data:", list(df.columns))

df = df.rename(columns = {'Measure':'Hazard', 'Units':'Intensity Unit'})

st.title("Damage Factor vs Intensity")

# Specify the filter order explicitly
filter_columns = ['Infrastructure', 'Infra_details', 'Measure', 'Units', 'Model']

# Sidebar filters
st.sidebar.header("Filters")

# Initialize session state for filters
for col in filter_columns:
    if f"{col}_selected" not in st.session_state:
        st.session_state[f"{col}_selected"] = []

# Reset button
if st.sidebar.button("Reset Filters"):
    for col in filter_columns:
        st.session_state[f"{col}_selected"] = []

filtered_df = df.copy()
for col in filter_columns:
    options = filtered_df[col].dropna().unique()
    selected = st.sidebar.multiselect(
        f"Select {col}",
        options,
        default=st.session_state[f"{col}_selected"],
        key=f"{col}_selected"
    )
    if selected:
        filtered_df = filtered_df[filtered_df[col].isin(selected)]
    else:
        filtered_df = filtered_df[filtered_df[col].isnull()]  # Empty DataFrame if nothing selected

# Drop rows with missing values in the required columns
filtered_df = filtered_df.dropna(subset=['Intensity', 'DamageFactor'])
filtered_df = filtered_df.sort_values('Intensity')

# Simple line chart
fig = px.line(
    filtered_df,
    x='Intensity',
    y='DamageFactor',
    title='Damage Factor vs Intensity',
    markers=True
)
fig.update_layout(
    xaxis_title='Intensity',
    yaxis_title='Damage Factor',
    template='plotly_white'
)

st.plotly_chart(fig, use_container_width=True)
