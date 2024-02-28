import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

city_list= [{"lat": "40.7128", "long": "-74.0060", "city": "New York"},
            {"lat": "35.6895", "long": "139.6917", "city":"Tokyo"},
            {"lat": "51.5099", "long": "-0.1180", "city": "London"},
            {"lat": "-33.8688", "long": "151.2093", "city": "Sydney"},
            {"lat": "-22.9068", "long": "-43.1729", "city": "Rio de Janeiro"},
            ]
position = [300, 430, 555, 690, 825]

image = Image.open("post.png")
draw = ImageDraw.Draw(image)

font= ImageFont.truetype("Inter.ttf", size=50)
content = "Latest Weather Forecast"
color = "rgb(255,255,255)"
draw.text((55,50), content, color, font=font)


font= ImageFont.truetype("Inter.ttf", size=30)
today = date.today()
content = date.today().strftime("%A - %B %d, %Y ")
color = "rgb(255,255,255)"
draw.text((55,145), content, color, font=font)

index = 0
for city in city_list:
  url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['long']}&current=temperature_2m,wind_speed_10m"
  response = requests.get(url, verify=False)
  data = json.loads(response.text)
  
  #city
  font= ImageFont.truetype("Inter.ttf", size=50)
  color = "rgb(0,0,0)"
  draw.text((135,position[index]), city["city"], color, font=font)
  
  #temp
  font= ImageFont.truetype("Inter.ttf", size=50)
  content=str(data['current']['temperature_2m']) + "\u00b0"
  color = "rgb(255,255,255)"
  draw.text((600,position[index]), content, color, font=font)
  
  #wind speed
  font= ImageFont.truetype("Inter.ttf", size=30)
  content=str(data['current']['wind_speed_10m']) + "km/h"
  color = "rgb(255,255,255)"
  draw.text((810,position[index]), content, color, font=font)
  
  index +=1
  
  
image.show()
image.save("test.png")