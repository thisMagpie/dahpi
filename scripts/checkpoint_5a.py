# Import
from webiopi.devices.sensor import DS18S20

# Readout temperature sensor
tmp0 = DS18S20(slave="10-00080265b6d6")
tmp0.getCelsius()
