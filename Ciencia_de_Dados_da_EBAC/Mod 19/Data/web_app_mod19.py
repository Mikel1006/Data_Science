import timeit
import pandas            as pd
import streamlit         as st
import seaborn           as sns
import matplotlib.pyplot as plt
from PIL                 import Image


sns.set_theme(style='ticks',
              rc={'axes.spines.right': False,
                  'axes.spines.top': False})


# Function to load the Data
@st.cache_data
def load_data(file_data: str, sep: str) -> pd.DataFrame:
    return pd.read_csv(filepath_or_buffer=file_data, sep=sep)

def multiselect_filter(data: pd.DataFrame,
                       col: str,
                       selected: list[str]
                       ) -> pd.DataFrame:
    if 'all' in selected:
        return data
    else:
        return data[data[col].isin(selected)].reset_index(drop=True)


def main():
    st.set_page_config(page_title = 'EBAC | Module 19 | Exercise 1', \
        page_icon = 'C:\\Users\\mtidi\\Documents\\EBAC\\Data Science (Ciência de dados)\\data science- Ebac blue - logo.png',
        layout="wide",
        initial_sidebar_state='expanded'
    )

    # Title
    st.markdown('''
    <div style="text-align:center">
        <a href="https://github.com/Mikel1006/Data_Science/tree/main/Ciencia_de_Dados_da_EBAC/Mod%2019">
            <img src="https://raw.githubusercontent.com/Mikel1006/Data_Science/refs/heads/main/Ciencia_de_Dados_da_EBAC/Mod%2019/Data/data_science.png", alt="data_science" width=100%>
        </a>
    </div> 

    ---
    

    <!-- # **Profession: Data Scientist** -->
    ### **Module 19** | Streamlit II | Exercise 1

    **Student:** [Mikel Tanner](https://www.linkedin.com/in/mikel-tanner/)<br>
    **Date:** 12th August 2025.

    ---
    ''', unsafe_allow_html=True)

    st.write('# Telemarketing Analysis')
    st.markdown(body='---')

    start = timeit.default_timer()
    
    # Sidebar
    image = Image.open("C:\\Users\\mtidi\\Documents\\EBAC\\Data Science (Ciência de dados)\\Desenvolvimento em Ciência de Dados e Metodologia Crisp-DM\Módulo 19 - Streamlit II\\image.png")
    st.sidebar.image(image)

    #Loading the data
    bank_raw = pd.read_csv('./bank-additional-full.csv', sep=';')

    bank = bank_raw.copy()

    st.write('## Raw Data')
    st.write(bank_raw.head())
    st.write('Number of lines:', bank_raw.shape[0])
    st.write('Number of columns:', bank_raw.shape[1])

    with st.sidebar.form(key ='my_form'):
        # Age
        max_age = int(bank.age.max())
        min_age = int(bank.age.min())
        age = st.sidebar.slider(label='Age Range', 
                        min_value = min_age,
                        max_value = max_age, 
                        value = (min_age, max_age),
                        step = 1)
        # st.sidebar.write('Age Range:', age)
        # st.sidebar.write('Min. Age:', age[0])
        # st.sidebar.write('Max. Age:', age[1])

        # PROFESSIONS
        jobs_list = bank['job'].unique().tolist()
        jobs_list.append('all')
        jobs_selected = st.multiselect(
            label='Profession', options=jobs_list, default=['all'])

        # MARITAL / CIVIL STATUS
        marital_list = bank['marital'].unique().tolist()
        marital_list.append('all')
        marital_selected = st.multiselect(
            'Civil Status', marital_list, ['all'])

        # DEFAULT
        default_list = bank['default'].unique().tolist()
        default_list.append('all')
        default_selected = st.multiselect(
            'Default', default_list, ['all'])

        # Mortgage
        housing_list = bank['housing'].unique().tolist()
        housing_list.append('all')
        housing_selected = st.multiselect(
            'Does client have a mortgage?', housing_list, ['all'])

        # Loan
        loan_list = bank['loan'].unique().tolist()
        loan_list.append('all')
        loan_selected = st.multiselect('Does client have a loan?', loan_list, ['all'])

        # CONTACT
        contact_list = bank['contact'].unique().tolist()
        contact_list.append('all')
        contact_selected = st.multiselect('Means of Contact ', contact_list, ['all'])

        # MONTH OF CONTACT
        month_list = bank['month'].unique().tolist()
        month_list.append('all')
        month_selected = st.multiselect('Month of contact', month_list, ['all'])

        # DAY OF THE WEEK
        day_of_week_list = bank['day_of_week'].unique().tolist()
        day_of_week_list.append('all')
        day_of_week_selected = st.multiselect(
            'Day of the week of contact', day_of_week_list, ['all'])

        bank = (bank.query('age >= @age[0] and age <= @age[1]')
                    .pipe(multiselect_filter, 'job', jobs_selected)
                    .pipe(multiselect_filter, 'marital', marital_selected)
                    .pipe(multiselect_filter, 'default', default_selected)
                    .pipe(multiselect_filter, 'housing', housing_selected)
                    .pipe(multiselect_filter, 'loan', loan_selected)
                    .pipe(multiselect_filter, 'contact', contact_selected)
                    .pipe(multiselect_filter, 'month', month_selected)
                    .pipe(multiselect_filter, 'day_of_week', day_of_week_selected))

        submit_button = st.form_submit_button(label='Apply')


    bank = bank[(bank['age'] >= age[0]) & (bank['age'] <= age[1])]
    
    st.write('## Filtered Data')
    st.write(bank.head())
    st.write('Number of lines:', bank.shape[0])
    st.write('Number of columns:', bank.shape[1])

    st.markdown("---")

    # PLOTS   
    fig, ax = plt.subplots(1, 2, figsize = (12,4))

    bank_raw_target_perc = bank_raw.y.value_counts(normalize = True).to_frame()*100
    bank_raw_target_perc = bank_raw_target_perc.sort_index()
    sns.barplot(x = bank_raw_target_perc.index, 
                y = 'proportion',
                data = bank_raw_target_perc, 
                ax = ax[0],
                palette='Set1')
    ax[0].bar_label(ax[0].containers[0])
    ax[0].set_title('Raw Data',
                    fontweight ="bold")
    
    bank_target_perc = bank.y.value_counts(normalize = True).to_frame()*100
    bank_target_perc = bank_target_perc.sort_index()
    sns.barplot(x = bank_target_perc.index, 
                y = 'proportion', 
                data = bank_target_perc, 
                ax = ax[1],
                palette='Set2' )
    ax[1].bar_label(ax[1].containers[0])
    ax[1].set_title('Filtered Data',
                    fontweight ="bold")
    
    st.write('## Acceptance Rate')

    st.pyplot(plt)


if __name__ == '__main__':
	main()
    









