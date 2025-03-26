import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import datetime


# 01 Setting some basic configurations
st.set_page_config(
    page_icon="https://raw.githubusercontent.com/rhatiro/Curso_EBAC-Profissao_Cientista_de_Dados/main/ebac-course-utils/media/icon/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 02 Adding the school logo to the App
st.markdown('''
<img src="https://raw.githubusercontent.com/marciolws/EBAC_EXERCICIOS/main/EBAC-media-utils/logo/newebac_logo_black_half.png" alt="ebac-logo">
		''',
 		unsafe_allow_html=True)

# 03 Adding some personal details and social media hyperlinks
st.title('Data Science - EBAC - Module 15 - Exercise 1')
st.header('Student: Mikel Tanner - [linkedin](https://www.linkedin.com/in/mikel-tanner/)' +
			' ***   ' + '[Github](https://github.com/Mikel1006/Data_Science)', 
			divider = "rainbow" )


#04 Creating a sidebar with different pages
page = st.sidebar.selectbox("Escolha uma página:", 
	["Home", "A slider", "Badges", "Markdown", "Selectbox", "Scatterplot 1", "Scatterplot 2", 
	"Chart", "Date Input", "PyPlot"])

if page == "Home":
    st.subheader("Welcome to the Home Page. \n ")

    st.write('##### Here is the main page, where I am including some features that can be included in the App. ')
    st.write('##### Feel free to use the sidebar to naviagate through the pages and features. ')

#05  Adding a slider inside the page 1
elif page == "A slider":
    st.write("####  Here is a slider. Feel free to move it around.")
    st.slider("##### There is a range, a minimum value and a maximum value: ", 0, 100, (25, 75))
    st.divider()

#06
elif page == "Badges":
    st.write("This is to show how badges will appear.")
    st.badge("Success", icon=":material/check:", color="green")
    st.badge("Failure", icon=":material/check:", color="red")
#07
elif page == "Markdown":
	st.write("This page deals with MARKDOWN and the texts can be coloured.\n")
	st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
#08
elif page == "Selectbox":
	st.write("This page deals with how the user can pick from a series of numbers and colours.\n")
	with st.form("my_form"):
		st.write("Inside the form")
		my_number = st.slider('Pick a number', 1, 10)
		my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
		st.form_submit_button('Submit my picks')

	# This is outside the form
	st.write(my_number)
	st.write(my_color)

#09 
elif page == "Scatterplot 1":
	df = pd.DataFrame(
    	np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    	columns=['lat', 'lon'])
	st.map(df)
	st.map(df, size=20, color='#0044ff')

#10
elif page == "Scatterplot 2":
	df = pd.DataFrame({
	    "col1": np.random.randn(1000) / 50 + 37.76,
	    "col2": np.random.randn(1000) / 50 + -122.4,
	    "col3": np.random.randn(1000) * 100,
	    "col4": np.random.rand(1000, 4).tolist(),
	})

	st.map(df,
	    latitude='col1',
	    longitude='col2',
	    size='col3',
	    color='col4')

#11 
elif page == "Chart":
	st.markdown('''
		:orange[This page shows the behaviour of a CHART]\n''')
	df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
	st.dataframe(df.style.highlight_max(axis=0))



#12 
elif page == "Date Input":
	d = st.date_input("When's your birthday", value=None)
	st.write('Your birthday is:', d)

#13 
elif page == "PyPlot":
	arr = np.random.normal(1, 1, size=10)
	fig, ax = plt.subplots()
	ax.hist(arr, bins=20)

	st.pyplot(fig)

st.divider()
	


