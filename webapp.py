import streamlit as st
import plotly.express as px
import sqlite3


connection = sqlite3.connect("data_project.db")

# with open('data.txt', 'r') as file:
#     text = file.read()

# dates = []
# temperature = []
# lines = text.split('\n')

# for i in lines:
#     parts = i.split(',')
#     # print(parts)
#     if len(parts) == 2:
#         dates.append(parts[0].strip())
#         temperature.append(parts[1].strip())

cursor = connection.cursor()
cursor.execute("SELECT date FROM chart")
dates = cursor.fetchall()
# print(dates)
dates = [item[0] for item in dates]
# print(dates)

cursor = connection.cursor()
cursor.execute("SELECT temperature FROM chart")
temperature = cursor.fetchall()
# print(temperature)
temperature = [item[0] for item in temperature]
# print(temperature)

st.title("Temperature Chart")
figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)