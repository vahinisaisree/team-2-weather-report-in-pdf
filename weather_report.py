""" team-2 vahini Weather report printing output in a pdf file format"""
import requests  # importing requests for extracting the data using url it makes simple
import os   # importing os for opening of pdf directly
from datetime import datetime  # importing date and time
import pytz  # importing pytz for taking certain country timezone
from fpdf import FPDF  # importing FPDF for generating pdf

# date and time
timeZ_Kl = pytz.timezone('Asia/kolkata')
dt_Kl = datetime.now(timeZ_Kl)

# initializing the variables with list
count = 1
temp = []
wind = []
weather_looking = []
humidity = []
city_names = []
print("Hi I am weather reporter I wil give weather report for 5 cities")
while count <= 5:  # giving range for 5 cities
    try:
        city_name = input("please Enter the city name: ")
        apikey = "5b420cc97b3e8854d34ef3f969298896"  # API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}' + '&appid=' + f'{apikey}'  # full url
        data = requests.get(url).json()  # getting info in json formate

        city_names.append(city_name)
        temp.append(int(data['main']['temp'] - 272.15))  # max temperature
        wind.append(data['wind']['speed'])  # wind speed
        weather_looking.append(data['weather'][0]['main'])  # weather looking like
        humidity.append(data['main']['humidity'])  # humidity
    except KeyError:
        print("City name not found")  # if city name is incorrect
    count += 1

# pdf creation
pdf = FPDF()
pdf.add_page()  # adding a page to the pdf
pdf.set_font("Times", size=13)  # mentioning total letter size and font

# title and today's date,time
pdf.set_text_color(153, 0, 0)
pdf.cell(200, 1, txt='weather Report', align='C', ln=1)
pdf.set_text_color(0, 0, 0)
pdf.cell(168, 10, txt=f"{(dt_Kl.strftime('Date:- %d-%m-%y'))}", ln=3, align='R')  # today's date will print
pdf.cell(168, 6, txt=f"{(dt_Kl.strftime('Time:- %H:%M:%S'))}", ln=3, align='R')

# printing city number 1
pdf.set_text_color(0, 0, 255)
pdf.cell(20, 10, txt=f"City:- {city_names[0]}", ln=2, align='L')  # printing city name
pdf.set_text_color(0, 0, 0)
pdf.cell(20, 7, txt=f"           Weather looking like - {weather_looking[0]}", ln=4,align='L')  # how weather looking
pdf.cell(20, 7, txt=f"           Maximum temperature - {str(temp[0])}°C", ln=5, align='L')  # maximum temperature
pdf.cell(20, 7, txt=f"           Wind speed - {str(wind[0])}", ln=6, align='L')  # wind speed
pdf.cell(20, 7, txt=f"           Humidity - {str(humidity[0])}", ln=7, align='L') # humidity
pdf.cell(20, 10, txt="_______________________________________________________________", ln=8, align='L')

# printing city number 2
pdf.set_text_color(0, 0, 255)
pdf.cell(20, 10, txt=f"city:- {city_names[1]}", ln=2, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(20, 7, txt=f"           Weather looking like - {weather_looking[1]}", ln=4, align='L')
pdf.cell(20, 7, txt=f"           Maximum temperature - {str(temp[1])}°C", ln=9, align='L')
pdf.cell(20, 7, txt=f"           Wind speed - {str(wind[1])}", ln=6, align='L')
pdf.cell(20, 7, txt=f"           Humidity - {str(humidity[1])}", ln=7, align='L')
pdf.cell(20, 7, txt="________________________________________________________________", ln=8, align='L')

# printing city number 3
pdf.set_text_color(0, 0, 255)
pdf.cell(20, 10, txt=f"city:- {city_names[2]}", ln=2, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(20, 7, txt=f"           Weather looking like - {weather_looking[2]}", ln=4, align='L')
pdf.cell(20, 7, txt=f"           Maximum temperature - {str(temp[2])}°C", ln=9, align='L')
pdf.cell(20, 7, txt=f"           Wind speed - {str(wind[2])}", ln=6, align='L')
pdf.cell(20, 7, txt=f"           Humidity - {str(humidity[2])}", ln=7, align='L')
pdf.cell(20, 10, txt="______________________________________________________________", ln=8, align='L')

# printing city number 4
pdf.set_text_color(0, 0, 255)
pdf.cell(20, 10, txt=f"city:- {city_names[3]}", ln=2, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(20, 7, txt=f"           Weather looking like - {weather_looking[3]}", ln=4, align='L')
pdf.cell(20, 7, txt=f"           Maximum temperature - {str(temp[3])}°C", ln=9, align='L')
pdf.cell(20, 7, txt=f"           Wind speed - {str(wind[3])}", ln=6, align='L')
pdf.cell(20, 7, txt=f"           Humidity - {str(humidity[3])}", ln=7, align='L')
pdf.cell(20, 10, txt="______________________________________________________________", ln=8, align='L')

# printing city number 5
pdf.set_text_color(0, 0, 255)
pdf.cell(20, 10, txt=f"city:- {city_names[4]}", ln=2, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(20, 7, txt=f"           Weather looking like - {weather_looking[4]}", ln=4, align='L')
pdf.cell(20, 7, txt=f"           Maximum temperature - {str(temp[4])}°C", ln=9, align='L')
pdf.cell(20, 7, txt=f"           Wind speed - {str(wind[4])}", ln=6, align='L')
pdf.cell(20, 7, txt=f"           Humidity - {str(humidity[4])}", ln=7, align='L')
pdf.cell(200, 10, txt="________THANK YOU______", ln=8, align='C')

# weather images for city 1
if weather_looking[0] == 'Smoke' or weather_looking[0] == 'Haze' or weather_looking[0] == 'Mist':
    pdf.image("haze mist smoke.png", x=90, y=30)
elif weather_looking[0] == "Clouds" or weather_looking[0] == 'Broken clouds' or weather_looking[0] == 'scattered clouds' or weather_looking[0] == 'Few clouds':
    pdf.image("clouds.png", x=100, y=30)
elif weather_looking[0] == "overcast clouds":
    pdf.image("clouds.png", x=90, y=30)
elif weather_looking[0] == "Clear" or weather_looking[0] == 'clear sky':
    pdf.image("sun.png", x=100, y=30)
elif weather_looking[0] == "Rain" or weather_looking[0] == "Drizzle" or weather_looking[0] == "moderate rain":
    pdf.image("Rain.png", x=90, y=30)
elif weather_looking[0] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=99, y=30)
else:
    print("wrong")

# weather images for city 2
if weather_looking[1] == 'Smoke' or weather_looking[1] == 'Haze' or weather_looking[1] == 'Mist':
    pdf.image("haze mist smoke.png", x=100, y=80)
elif weather_looking[1] == "Clouds" or weather_looking[1] == 'Broken clouds' or weather_looking[1] == 'scattered clouds' or weather_looking[1] == 'Few clouds':
    pdf.image("clouds.png", x=100, y=80)
elif weather_looking[1] == "overcast clouds":
    pdf.image("clouds.png", x=100, y=80)
elif weather_looking[1] == "Clear" or weather_looking[1] == 'clear sky':
    pdf.image("sun.png", x=100, y=80)
elif weather_looking[1] == "Rain" or weather_looking[1] == "Drizzle" or weather_looking[1] == "moderate rain":
    pdf.image("Rain.png", x=90, y=79)
elif weather_looking[1] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=99, y=80)
else:
    print("wrong")

# weather images for city 3
if weather_looking[2] == 'Smoke' or weather_looking[2] == 'Haze' or weather_looking[2] == 'Mist':
    pdf.image("haze mist smoke.png", x=90, y=120)
elif weather_looking[2] == "Clouds" or weather_looking[2] == 'Broken clouds' or weather_looking[2] == 'scattered clouds' or weather_looking[2] == 'Few clouds':
    pdf.image("clouds.png", x=95, y=125)
elif weather_looking[2] == "overcast clouds":
    pdf.image("clouds.png", x=90, y=120)
elif weather_looking[2] == "Clear" or weather_looking[2] == 'clear sky':
    pdf.image("sun.png", x=90, y=120)
elif weather_looking[2] == "Rain" or weather_looking[2] == "Drizzle" or weather_looking[2] == "moderate rain":
    pdf.image("Rain.png", x=90, y=125)
elif weather_looking[2] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=99, y=120)
else:
    print("wrong")

# weather images for city 4
if weather_looking[3] == 'Smoke' or weather_looking[3] == 'Haze' or weather_looking[3] == 'Mist':
    pdf.image("haze mist smoke.png", x=90, y=170)
elif weather_looking[3] == "Clouds" or weather_looking[3] == 'Broken clouds' or weather_looking[3] == 'scattered clouds' or weather_looking[3] == 'Few clouds':
    pdf.image("clouds.png", x=100, y=170)
elif weather_looking[3] == "overcast clouds":
    pdf.image("clouds.png", x=90, y=170)
elif weather_looking[3] == "Clear" or weather_looking[3] == 'clear sky':
    pdf.image("sun.png", x=90, y=170)
elif weather_looking[3] == "Rain" or weather_looking[3] == "Drizzle" or weather_looking[2] == "moderate rain":
    pdf.image("Rain.png", x=90, y=175)
elif weather_looking[3] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=99, y=170)
else:
    print("wrong")

# weather images for city 5
if weather_looking[4] == 'Smoke' or weather_looking[4] == 'Haze' or weather_looking[4] == 'Mist':
    pdf.image("haze mist smoke.png", x=90, y=220)
elif weather_looking[4] == "Clouds" or weather_looking[4] == 'Broken clouds' or weather_looking[4] == 'scattered clouds' or weather_looking[4] == 'Few clouds':
    pdf.image("clouds.png", x=100, y=220)
elif weather_looking[4] == "overcast clouds":
    pdf.image("clouds.png", x=90, y=220)
elif weather_looking[4] == "Clear" or weather_looking[4] == 'clear sky':
    pdf.image("sun.png", x=90, y=220)
elif weather_looking[4] == "Rain" or weather_looking[4] == "Drizzle" or weather_looking[4] == "moderate rain":
    pdf.image("Rain.png", x=90, y=220)
elif weather_looking[4] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=99, y=220)
else:
    print("wrong")

pdf.output("weather011.pdf")  # get output in pdf  and the name of the pdf is arithmetic.pdf
os.system('weather011.pdf')
