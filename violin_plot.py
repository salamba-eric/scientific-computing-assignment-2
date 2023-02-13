# Import the required packages
import seaborn as sb
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Get the data
def get_dataframe():
	dataframe = pd.read_csv('gapminder_with_codes.csv')

	# Columns containing strings...expectation = [country, continent, Iso-alpha]
	__dataframe__ = dataframe.select_dtypes(['object'])
	string_dataframe_cols = __dataframe__.columns

	# A list of all the available countries
	countries_column = dataframe["country"]
	countries = countries_column.unique()

	# A list of all the years in the file
	year_column = dataframe["year"]
	years = year_column.unique()

	return dataframe, string_dataframe_cols, countries, years

# Giving the aquired data global variable names
dataframe, word_columns, countries, years = get_dataframe()
number_columns = pd.Series(["lifeExp", "pop", "gdpPercap", "iso_num"])

#Rendering the obtained info in streamlit
# The sidepanel
st.sidebar.title("Side Panel")

check_box = st.sidebar.checkbox(label = "Display Dataset")
if check_box:
	st.write(dataframe)

st.sidebar.subheader("Parameters for the plot")

# The parameters to display
year_selection = st.sidebar.selectbox(label = "Year", options = years)
x_axis_selection = st.sidebar.selectbox(label = "x axis", options = number_columns)
y_axis_selection = st.sidebar.selectbox(label = "y axis", options = word_columns)

# Filter by year
dataframe = dataframe[dataframe["year"] == year_selection]

# Drawing the figure
fig, ax = plt.subplots()
ax = sb.violinplot (data = dataframe, x = x_axis_selection, y = y_axis_selection)

# Showing the figure in streamlit
check_box2 = st.sidebar.checkbox(label = " Show plot")
if check_box2:
	if st.sidebar.button(" Generate Violin plot"):
		st.pyplot(fig)

if not check_box and not check_box2:
	st.title("Generate Plot")
	st.markdown("Generate a violin plot by selecting the appropriate parameters from the side bar and checking the 'Generate Plot' box")
	st.markdown("If you wish to view the data frame of a specicific year, select the year and check the 'Display Dataset' box")
