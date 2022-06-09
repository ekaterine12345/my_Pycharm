# import pyowm
#
# key='b0382a9da8d31051dd5eecdc220673dc'
#
# from pyowm import OWM
#
# # ---------- FREE API KEY examples ---------------------
#
# owm = OWM('your free OWM API key')
# mgr = owm.weather_manager()
#
#
# # Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
import sqlite3
conn = sqlite3.connect('covid.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS covid 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            country VARCHAR(15),
            province VARCHAR(40),
            population INTEGER,
            confirmed INTEGER,
            deaths INTEGER            
            )''')




