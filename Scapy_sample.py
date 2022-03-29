#import PIL
#from PIL import Image
from numpy import asarray
import numpy as np
from scapy.all import *
import os
import binascii
import pandas as pd

"""
#### TENSOR
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input, Flatten, Conv2D, Dropout, MaxPooling2D
from tensorflow.keras import models, datasets, layers, optimizers
from tensorflow.keras import backend as k
import matplotlib.pyplot as plt
"""

#targeting folder and file pcap 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 's62-eth2-Training.pcap')
#reading file pcap save as variabel pcap_data
pcap_data=rdpcap(my_file)


# Print show summary all packets
print(pcap_data)

# Get raw bytes data from Pcap from specific row , you can change the index number [0] to select specific row
pcap_raw = pcap_data[0]
print(pcap_raw)

# Get length of a pcap raw in bytes
pcap_array = bytearray(bytes(pcap_raw))
pcap_np_array = asarray(pcap_array)
pcap_length = len(pcap_np_array)
print(pcap_length)

# Check packet feature Scapy - Check each of the instruction bellow and See dokumentation here: https://0xbharath.github.io/art-of-packet-crafting-with-scapy/scapy/inspecting_packets/index.html
ls(pcap_raw)
pcap_raw.show()
pcap_raw.show2()
pcap_raw.summary()

