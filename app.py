#python tkinter library 
#pip install requests
#pip install Pillow Pillow is the python images library
#pip install needs to be run in the terminal, not in the python file and also not in the python interpreter
#the filename should not be tkinter.py. python will import the wron tkinter in the code below giving this error message AttributeError: module 'tkinter' has no attribute 'Tk'
#pyinstaller enables the conversion of the app to an exe

#this code creates a basic window without any content
import tkinter as tk
from tkinter import font
import requests
HEIGHT = 500
WIDTH = 600
def test_function(entry):
    print("this is the entry", entry)

#api key from openweather.org goes here  4e1b31566b3418e508db4e24fa172050
# insert api key api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=5e1b31566b3418e508db4e24fa172050
def get_weather(city):
    weather_key = "5e1b31566b3418e508db4e24fa172050"
    url = "api.openweathermap.org/data/2.5/forecast"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather["name"])
    print(weather["weather"][0]["description"])
    print(weather["main"]["temp"])

root = tk.Tk() #root is the main  structuré
#canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
#frame
frame = tk.Frame(root, bg="grey", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n") #relx and rely define a frame inside the application window
# we place widgets inside the window for functionality

#button
button = tk.Button(frame, text="Test button", bg="white", fg="black", font=("Courier", 12), command=lambda:test_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)
#entry
entry= tk.Entry(frame, font=("Courier", 18))
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg="green", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
label = tk.Label(lower_frame, bg="white", font=("Courier", 18))
label.place(relwidth=1, relheight=1)



root.mainloop()

