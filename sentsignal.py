"""
PyRF: PyRF is a Python library for controlling and interacting with RF instruments. 
It provides a simple and flexible interface for working with RF signals, including the ability to transmit and receive signals. 
PyRF supports a variety of RF instruments, including the Ettus Research USRP software-defined radio.
To send a signal using PyRF, you will need an RF instrument that supports transmission, such as the Ettus Research USRP. 
"""

import numpy as np
import pyrf

# Create a connection to the USRP
usrp = pyrf.devices.usrp.USRP()

# Set the sampling rate and center frequency
usrp.rx_srate = 10e6
usrp.rx_freq = 900e6

# Create a sine wave signal
freq = 1e6
duration = 1 # seconds
samples = int(duration * usrp.rx_srate)
t = np.linspace(0, duration, samples, endpoint=False)
signal = np.sin(2*np.pi*freq*t)

# Transmit the signal
usrp.tx(signal)
