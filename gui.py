import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather
from file_manager import save_weather_to_file, log_summary

def launch_app():
    def get_and_display_weather():
        city = city_entry.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return
        data = get_weather(city)
        if data:
            temp_f = round((data["main"]["temp"] * 9/5) + 32, 1)
            description = data["weather"][0]["description"]
            result_label.config(
                text=f"{city}:\n{temp_f}°F, {description.capitalize()}"
            )
            save_weather_to_file(city, data)
            log_summary(city, data)
        else:
            result_label.config(text=f"Could not retrieve weather for '{city}'.")

    root = tk.Tk()
    root.title("Weather GUI App")
    root.geometry("350x250")
    
    tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
    city_entry = tk.Entry(root, width=30)
    city_entry.pack()
    
    tk.Button(root, text="Get Weather", command=get_and_display_weather).pack(pady=10)
    
    result_label = tk.Label(root, text="", font=("Arial", 11), justify="center")
    result_label.pack(pady=10)
    
    root.mainloop()
