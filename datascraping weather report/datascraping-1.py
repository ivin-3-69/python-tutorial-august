import requests
from bs4 import BeautifulSoup
import pandas

homepage = requests.get("https://mausam.imd.gov.in")
soup = BeautifulSoup(homepage.content,'html5lib')
city_div= soup.find(class_= 'capitals clearfix')
items = city_div.find_all(class_ = "capital")
   
city_names = [item.find("h3").get_text() for item in items]
city_temp = [item.find(class_ = 'val').get_text() for item in items]
city_pers = [item.find(class_ = 'max').get_text() for item in items]
weather_db = pandas.DataFrame( {
    "City Name" : city_names,
    "City Temp" : city_temp,
    "City Rain" : city_pers,
} )
weather_db.to_csv("weather_db.csv")
print(weather_db)