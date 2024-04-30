import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


st.set_option('deprecation.showPyplotGlobalUse', False)

#add logo
st.image('FinCenBar.jpg',use_column_width=True, width=300, caption="https://www.fincen.gov/reports/sar-stats" )

#add title 
st.markdown("<h3 style='text-align: center; color: black;'>Suspicious Activity Report (SAR) Data 2014 - 2023</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
sar_data = load_data("SAR_stats_ALL.csv")
sar_state_data = load_data("SARS_stats_state.csv") 


industry = sar_data['Industry'].unique() # get the unique values of the industry column that will be used to filter dataframes
industry_choice = st.selectbox('Select an Industry for More Details', industry, index=12) # add a selectbox widget
filtered_df = sar_data.loc[sar_data['Industry'] == industry_choice] # filter the dataframe by the selected value
styled_df = filtered_df.style.format({'Year': lambda x: f"{x:.0f}"}) # Remove commas from the years (treated as float/int)

st.dataframe(styled_df, use_container_width=True, height= 200) # display the filterable dataframe

#configure graph
plt.figure(figsize=(20, 8))
fig = sns.lineplot(data=filtered_df, x='Year', y='Count')
plt.xlabel('Year', fontsize=30)
plt.ylabel('Number of SARS', fontsize=30)
plt.xticks(fontsize=20)  #x axis tick labels
plt.yticks(fontsize=20)  #y-axis tick labels 

#fig = industry
st.pyplot()


state = sar_state_data['State'].unique() # get the unique values of the State column that will be used to filter dataframes
state_choice = st.selectbox('Select an State/Territory for More Details', state, index=0) # add a selectbox widget
filtered_state_df = sar_state_data.loc[sar_state_data['State'] == state_choice] # filter the dataframe by the selected value
styled_state_df = filtered_state_df.style.format({'Year': lambda x: f"{x:.0f}"}) # Remove commas from the years (treated as float/int)

st.dataframe(styled_state_df, use_container_width=True, height= 200) # display the filterable dataframe

#configure graph
plt.figure(figsize=(20, 8))
fig2 = sns.lineplot(data=filtered_state_df, x='Year', y='Count')
plt.xlabel('Year', fontsize=30)
plt.ylabel('Number of SARS', fontsize=30)
plt.xticks(fontsize=20)  #x axis tick labels
plt.yticks(fontsize=20)  #y-axis tick labels 

#fig = industry
st.pyplot()



