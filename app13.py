import streamlit as st 
import pandas as pd 
import seaborn as sns 
import datetime as dt 
import matplotlib.pyplot as plt 


SAR_Data = pd.read_csv("Industry_Combined.csv")

# Convert 'date' column to datetime
SAR_Data['Year'] = pd.to_datetime(SAR_Data['Year'])

# Extract year
SAR_Data['Year'] = SAR_Data['Year'].dt.year


# Plotting the line chart
sns.set_theme(style="whitegrid")


# Create the FacetGrid object
grid = sns.relplot(
    data=SAR_Data,
    x="Year",
    y="Number_of_SARs",
    hue="Industry",
    kind="line",
    marker="o",
    col="Industry",
    col_wrap=3,
    facet_kws={"sharex": False, "sharey": False},
)

# Showing the plot
fig = grid
st.pyplot(fig)