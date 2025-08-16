import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your OpenWeather API key
API_KEY = "390c01e63e78c45868ba070821aae102"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(data)  # Debugging

    # Check if valid response
    if response.status_code == 200 and "main" in data:
        main = data["main"]
        weather = data["weather"][0]

        temp = main["temp"]
        humidity = main["humidity"]
        description = weather["description"].capitalize()

        return f"🌡 Temp: {temp}°C\n💧 Humidity: {humidity}%\n☁️ Condition: {description}"
    else:
        return f"❌ Error: {data.get('message', 'City not found')}"

# GUI
def show_weather():
    city = city_entry.get().strip()
    if city:
        result = get_weather(city)
        messagebox.showinfo("Weather Report", result)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name!")

# UI Setup
root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("400x300")
root.configure(bg="#2c3e50")

title_label = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#34495e", padx=20, pady=20, relief="raised", bd=3)
frame.pack(pady=10)

tk.Label(frame, text="Enter City:", font=("Arial", 14), fg="white", bg="#34495e").pack(pady=10)
city_entry = tk.Entry(frame, font=("Arial", 14), width=20)
city_entry.pack(pady=5)

tk.Button(frame, text="Get Weather", command=show_weather, font=("Arial", 14, "bold"),
          bg="#1abc9c", fg="white", relief="flat", padx=10, pady=5).pack(pady=20)

footer = tk.Label(root, text="Powered by OpenWeather 🌍", font=("Arial", 10), fg="white", bg="#2c3e50")
footer.pack(side="bottom", pady=10)

root.mainloop()
