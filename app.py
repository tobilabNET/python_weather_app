
import tkinter as tk
import requests
from PIL import Image, ImageTk

app = tk.Tk()

HEIGHT = 500
WIDTH = 600

def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (city, conditions, temp)
    except:
        final_str = 'Couldnt get weather information'
    #final_str = 'hello'
    return final_str


def get_weather(city):
    weather_key = "5e1b31566b3418e508db4e24fa172050"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": "5e1b31566b3418e508db4e24fa172050", "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()
    results['text'] = format_response(response.json())	

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img





#canvas
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file="landscape1.png")
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)
#frame
frame = tk.Frame(app, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")
textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)
#button
submit = tk.Button(frame, text="Show Weather", bg="white", fg="black", font=("Courier", 12), command=lambda:get_weather(textbox.get()))
submit.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(app, bg="navy", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
label = tk.Label(lower_frame, bg="white", font=("Courier", 18))
label.place(relwidth=1, relheight=1)


bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


app.mainloop()

