import os
#Check network interface status.
def check_physical():
    os.system("ip link show")
    print("Physical layer checked.")
    # Additional checks can be added here, such as checking for link lights, cable connections,
