# ESP32  Weather Dashboard 🌸☀️🌧️

This project creates a **web-based weather dashboard** using **ESP32**, a **DHT11 sensor** for indoor temperature & humidity, a **Rain Sensor (A0)** for detecting rain, and **OpenWeatherMap API** for outdoor temperature. The dashboard features a ** CSS design** with pink/purple gradients for a cute and colorful look.

---

## 📌 Use Cases
- Real-time monitoring of indoor and outdoor temperature  
- Rain detection for smart home automation  
- Display weather on mobile or desktop  
- Educational IoT project for beginners  

---

## 🛠️ Components
- **ESP32**  
- **DHT11 or DHT22** sensor (Indoor Temperature & Humidity)  
- **Rain Sensor (A0)**  
- **Jumper wires**  
- **Breadboard** (optional)  
-**Internet connection for API access**  

---

## ⚙️ System Logic
- **Indoor temperature & humidity** → measured by DHT sensor  
- **Rain detection** → analog reading from A0 pin  
- **Outdoor temperature** → fetched from **OpenWeatherMap API**  
- Dashboard displays all readings **real-time** with **Girly CSS** design  

---

## 🧩 Features
- Real-time indoor and outdoor temperature monitoring  
- Rain detection with analog sensor  
- Girly-themed web dashboard (pink/purple gradient, cute cards)  
- Mobile-friendly  
- Optional auto-refresh with `<meta http-equiv="refresh">`  
- Clean and modular code for easy expansion  

---

## 📷 Demo Video
👉 [Click here to watch the demo](https://youtu.be/YiXlZvJFgB4?si=78ODaE-Ys2R4eTza)

---

## 📡 Wiring Diagram

**DHT Sensor (Indoor Temperature & Humidity):**  
- DATA → GPIO 23  
- VCC → 3.3V  
- GND → GND  

**Rain Sensor (A0):**  
- A0 → GPIO 34  
- VCC → 3.3V  
- GND → GND  

> ⚠️ Do **not** use 5V with ESP32 for sensors  

---

## 💻 Code
- MicroPython: `weather.py`  
- Insert your **OpenWeatherMap API_KEY** in the code:
API_KEY = "YOUR_OPENWEATHERMAP_KEY"

---

## 👩‍💻 Author

**Ala Toumi**
3rd-year Computer Engineering Student
Embedded Systems & IoT enthusiast

---

## 📎 License

MIT License – Free to use and modify.
