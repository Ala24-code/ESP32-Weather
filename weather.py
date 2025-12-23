# ============== IMPORTS ==============
import network
import socket
from machine import Pin, ADC
import dht
from time import sleep
import urequests  

# ============== CONFIG ==============
SSID = "TOPNET_A7DE"
PASSWORD = "7XZ26E87SXKV"
API_KEY = "bfc59453ef76c7f1ba0b3acb34e51587"
CITY = "Tozeur"
RAIN_THRESHOLD = 2500  # Adjust for your sensor

# ============== WIFI ==============
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Connecting to WiFi...")
    wlan.connect(SSID, PASSWORD)

    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        print(".", end="")
        sleep(1)
        timeout -= 1

    if wlan.isconnected():
        print("\nConnected:", wlan.ifconfig())
        return wlan.ifconfig()[0]
    else:
        print("\nWiFi failed")
        return None

# ============== SENSORS ==============
dht_sensor = dht.DHT11(Pin(23))
rain = ADC(Pin(34))
rain.atten(ADC.ATTN_11DB)
rain.width(ADC.WIDTH_12BIT)

def read_dht():
    try:
        sleep(2)
        dht_sensor.measure()
        return dht_sensor.temperature(), dht_sensor.humidity()
    except:
        return None, None

def read_rain():
    value = rain.read()
    status = "🌧️ Rain detected" if value < RAIN_THRESHOLD else "☀️ No rain"
    return value, status

# ============== API ==================
def read_api_temp():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        res = urequests.get(url)
        data = res.json()
        temp = data['main']['temp']
        res.close()
        return temp
    except:
        return None

# ============== WEB PAGE  ==============
def web_page(temp_in, hum, rain_val, rain_status, temp_out):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">

<title>ESP32 Ala Weather</title>
<style>
    body {{
        background: linear-gradient(135deg, #ffd1dc, #e0bbff);
        font-family: 'Arial', sans-serif;
        text-align: center;
        color: #6a0572;
    }}
    .card {{
        background: white;
        width: 320px;
        margin: 40px auto;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }}
    h1 {{
        color: #ff69b4;
    }}
    p {{
        font-size: 18px;
        margin: 10px 0;
    }}
    .value {{
        font-weight: bold;
        color: #9c27b0;
    }}
    .footer {{
        margin-top: 15px;
        font-size: 12px;
        color: #888;
    }}
</style>
</head>
<body>

<div class="card">
    <h1>🌸 ESP32 Weather 🌸</h1>
    <p>🌡️ Inside Temperature: <span class="value">{temp_in} °C</span></p>
    <p>🌡️ Outside Temperature: <span class="value">{temp_out} °C</span></p>
    <p>💧 Humidity: <span class="value">{hum} %</span></p>
    <p>☁️ Rain Status: <span class="value">{rain_status}</span></p>
    <div class="footer">Made with 💖 by ESP32</div>
</div>

</body>
</html>
"""

# ============== SERVER ==================
def start_server(ip):
    s = socket.socket()
    s.bind(('', 80))
    s.listen(1)
    print("Web server running...")
    print("Open: http://", ip)

    while True:
        conn, addr = s.accept()
        print("Client:", addr)

        temp_in, hum = read_dht()
        rain_val, rain_status = read_rain()
        temp_out = read_api_temp()

        if temp_in is None:
            temp_in = "Error"
            hum = "Error"
        if temp_out is None:
            temp_out = "Error"

        html = web_page(temp_in, hum, rain_val, rain_status, temp_out)
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.send(html)
        conn.close()

# ============== MAIN ==================
ip = connect_wifi()
if ip:
    start_server(ip)
