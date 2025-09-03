import os
def check_network():
    os.system("ping -c 4 8.8.8.8")
    os.system("traceroute 8.8.8.8")