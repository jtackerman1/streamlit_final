import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 


st.set_option('deprecation.showPyplotGlobalUse', False)

#add logo
st.image('FinCenBar.jpg',use_column_width=True, width=200)

#add title 
st.markdown("<h4 style='text-align: center; color: black;'>Suspicious Activity Report (SAR) Data 2014 - 2023</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
sar_data = load_data("SAR_stats_ALL.csv")
sar_state_data = load_data("SARS_stats_states.csv") 

    # Define your page functions here
def page1():
    st.write('With the soaring rates of fraud and money laundering in the banking industry, Suspicious Activity Reports (SARs) are increasing in the industry '
             'at a very fast pace, causing banks to face new and difficult regulatory, supervisory, and compliance challenges. Along with those challenges, '
             'there has been a significant increase in BSA/AML enforcement activity by the Federal Banking Agencies (FBAs) and the Financial Crimes Enforcement Network (FinCEN).  '
            'Highlighting this renewed emphasis, in August 2014, FinCEN issued an advisory emphasizing its expectations for financial institutions’ BSA/AML compliance' 
            'programs, including: engagement and accountability of financial institution management and directors; allocation of sufficient compliance staffing and related '
            'resources; sharing of relevant compliance related information across business units; competent and independent testing of an institution’s BSA/AML compliance program,'
            '  as well as periodic updates to address emerging issues and trends; and an enterprise-wide understanding of the critical role of BSA/AML reporting requirements.'
	        '[1]See Financial Crimes Enforcement Network, FIN-2014-A007 '
)

def page2():
    industry = sar_data['Industry'].unique() # get the unique values of the industry column that will be used to filter dataframes
    industry_choice = st.selectbox('Select an Industry for More Details', industry, index=1) # add a selectbox widget
    filtered_df = sar_data.loc[sar_data['Industry'] == industry_choice] # filter the dataframe by the selected value
    styled_df = filtered_df.style.format({'Year': lambda x: f"{x:.0f}"}) # remove commas from the years (treated as float/int)
    yearly_sars_df = filtered_df.groupby('Year')['Count'].sum().reset_index() #sum by year for display

    st.dataframe(styled_df, hide_index =True, use_container_width=True, height= 140) # display the filterable dataframe

    #configure graph
    plt.figure(figsize=(18, 6))
    sns.lineplot(data=yearly_sars_df, x='Year', y='Count')
    plt.xlabel('Year', fontsize=20)
    plt.ylabel('Number of SARS', fontsize=20)
    plt.xticks(fontsize=20)  #x axis tick labels
    plt.yticks(fontsize=20)  #y-axis tick labels 
    
    #plot graph
    st.pyplot()

def page3():
    state = sar_state_data['State'].unique() # get the unique values of the State column that will be used to filter dataframes
    state_choice = st.selectbox('Select an State/Territory for More Details', state, index=0) # add a selectbox widget
    filtered_state_df = sar_state_data.loc[sar_state_data['State'] == state_choice] # filter the dataframe by the selected value
    styled_state_df = filtered_state_df.style.format({'Year': lambda x: f"{x:.0f}"}) # remove commas from the years (treated as float/int)
    yearly_sums_df = filtered_state_df.groupby('Year')['Count'].sum().reset_index() # group by 'Year' and sum the values for each year 

    st.dataframe(styled_state_df, hide_index =True, use_container_width=True, height= 140) # display the filterable dataframe

    #configure graph
    plt.figure(figsize=(18, 6))
    sns.barplot(data=yearly_sums_df, x='Year', y='Count', color='lightblue')
    plt.xlabel('Year', fontsize=20)
    plt.ylabel('Number of SARS', fontsize=20)
    plt.xticks(fontsize=20)  #x axis tick labels
    plt.yticks(fontsize=20)  #y-axis tick labels 

    #plot graph
    st.pyplot()


# create a pages dictionary 
pages = {
    "Overview": page1,
    "SAR Totals by Industry": page2,
    "SAR Totals by State": page3,
}

# create tabs for the pages using a for loop and the pages dictionary
selected_page = st.selectbox("Select an Option", list(pages.keys()))
pages[selected_page]()