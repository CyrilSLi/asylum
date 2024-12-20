import board, displayio, os, wifi
import adafruit_connection_manager, adafruit_requests

pool = adafruit_connection_manager.get_radio_socketpool (wifi.radio)
ssl_context = adafruit_connection_manager.get_radio_ssl_context (wifi.radio)
requests = adafruit_requests.Session (pool, ssl_context)