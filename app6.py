import streamlit as st 
import pandas as pd 
import seaborn as sns 
import datetime as dt 
import matplotlib.pyplot as plt 


SAR_Data = pd.read_csv("Industry_Combined.csv")
#print(SAR_Data.info())
# Plotting the line chart
plt.figure(figsize=(20, 6))
sns.relplot(
    data=SAR_Data, 
    x='Year',
    y='Number_of_SARs',
    hue='Industry',
    kind='line', 
    marker='o', 
    errorbar=None,
    col='Industry', 
    col_wrap=3,
    facet_kws={'sharex': False, 'sharey': False})  # Modify the scales of facet_wrap


# Adding ties and labels
plt.title("Number of SARs by Year")
plt.xlabel("Year")
plt.ylabel("Number")

# Showing the plot

st.pyplot(fig=None, clear_figure=None, use_container_width=True)
#st.pyplot(fig)