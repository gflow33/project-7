import requests
import selectorlib
import time
import streamlit as st
import plotly.express as px

URL = "https://programmer100.pythonanywhere.com/"

# Get html data from URL
def scrape(url):
    """Scrape the page source from the url"""
    response = requests.get(url)
    source = response.text
    # print(source)
    return source

# 
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    # print(value)
    return value

date = time.strftime("%Y-%m-%d %H:%M:%S")


def store():
    with open('data.txt', 'a') as file:
        file.write(f"{date},{temp}" + '\n')

with open('data.txt', 'r') as file:
    text = file.read()
print(text)
dates = []
temperature = []
lines = text.split('\n')

for i in lines:
    parts = i.split(',')
    # print(parts)
    if len(parts) == 2:
        dates.append(parts[0].strip())
        temperature.append(parts[1].strip())

st.title("Temperature Chart")
figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)

if __name__ == "__main__":
    scraped = scrape(URL)
    temp = extract(scraped)
    store()
