import requests
import selectorlib
import time
import sqlite3


URL = "https://programmer100.pythonanywhere.com/"


connection = sqlite3.connect("data_project.db")
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
    # x = f"{date}, {temp}"
    # print(x)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO chart VALUES(?,?)", (date, temp))
    connection.commit()

    # with open('data.txt', 'a') as file:
    #     file.write(f"{date},{temp}" + '\n')


# print(text)
if __name__ == "__main__":
    scraped = scrape(URL)
    temp = extract(scraped)
    store()
