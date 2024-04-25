import streamlit as st 
import pandas as pd 
import seaborn as sns 
import datetime as dt 
import matplotlib.pyplot as plt 

st.set_option('deprecation.showPyplotGlobalUse', False)

casino_df = pd.read_csv("Casino.csv")
deposit_df = pd.read_csv("Deposit.csv")
housing_df = pd.read_csv("Housing.csv")
insurance_df = pd.read_csv("Insurance.csv")
loan_df = pd.read_csv("Loan.csv")
moneyservices_df = pd.read_csv("MoneyServices.csv")
other_df = pd.read_csv("Other.csv")
securities_df = pd.read_csv("Securities.csv")


# dictionary of the dataframe options
dataframes = {
    'Casino': casino_df,
    'Deposit Institutions': deposit_df,
    'Housing Gov. Sponsored Enterprise': housing_df,
    'Insurance': insurance_df,
    'Loan': loan_df,
    'Money Services': moneyservices_df,
    'Other': other_df,
    'Securities': securities_df
}
#add logo
st.image('FinCenLogo.gif',use_column_width='auto')

# app title
st.title('Suspicious Activity Report (SAR) Data from 2014 - 2022')

# create a drop-down menu to select the industry
selected_df = st.selectbox('Select Industry:', list(dataframes.keys()))

# get the selected industry
industry = dataframes[selected_df]



# view grid details
st.write('Industry Filings by State/Year')
st.write(industry)

#configure graph
plt.figure(figsize=(20, 10))
fig = sns.lineplot(data=industry, x='Year', y='Number_of_SARs')
plt.xlabel('Year', fontsize=30)
plt.ylabel('Total Number of SARS', fontsize=30)
plt.xticks(fontsize=20)  #x axis tick labels
plt.yticks(fontsize=20)  #y-axis tick labels

fig = industry
st.pyplot()



