from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN
import time

settings = initialize_VPN(save=1,area_input=['Ireland'])

while True: 
    rotate_VPN(settings,google_check=1) 
    time.sleep(1800) #e.g. rotate servers every hour