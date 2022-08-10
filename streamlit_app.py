import streamlit as sl
sl.title("My Mom's New Healthy Diner")
sl.header("Breakfast Favorites")
sl.text("🥣 Omega 3 & Blueberry OatMeal")
sl.text("🥗 Kale, Spinach & Rocket Smoothie")
sl.text("🐔 Hard Boiled Free-Range Egg")
sl.text("🥑🍞 Avocado Toast")
sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
