import os

def check_application():
    os.system("curl -I https://www.google.com")
    os.system("dig google.com")
    print("Application layer check completed.")