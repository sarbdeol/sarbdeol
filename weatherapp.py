import tkinter as tk
import requests
import time


def getweather(canvas):
    city=text.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9e044a9f94067937fe60ab19ccd8e0e2"
    json_data=requests.get(api).json()
    condition =json_data["weather"][0]['main']
    temp =int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    pressure =json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind= json_data['wind']['speed']
    country= json_data['sys']['country']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-23400))
    sunset= time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-23400))
    final_info= condition + '\n' + str(temp) + "°C" + '\n' + str(country)
    final_data = '\n'+"Min temp : " + str(min_temp) +"°C"+'\n' "Max temp : " + str(max_temp) +"°C"+ '\n' + "pressure : " + str(pressure) +' kPa'+'\n' +"Humidity : " + str(humidity) +'%'+'\n' +'wind speed : ' + str(wind)+ " km\h"+'\n' + "sunrise : " + str(sunrise)+ " AM" + '\n' + "sunset : " + str(sunset) + " PM"
    l1.config(text=final_info)
    l2.config(text=final_data)
canvas=tk.Tk()
canvas.geometry("600x500")
canvas.title("weather app")
canvas.configure(bg='skyblue')

f = ("poppins",15,'bold')
t = ("poppins",35,'bold')

text=tk.Entry(canvas,justify='center',font=t)
text.pack(pady=50)
text.focus()
text.bind('<Return>',getweather)
l1=tk.Label(canvas,font=t,bg='skyblue')
l1.pack()

l2=tk.Label(canvas,font=f,bg='sky blue')
l2.pack()

canvas.mainloop()