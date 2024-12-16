# router1_config.py
from netmiko import ConnectHandler

def configure_router1():
    try:
        router1 = {
            'device_type': 'cisco_ios',
            'host': '192.170.0.66',  # כתובת ה-IP של הנתב הראשון
            'username': 'admin',
            'password': 'Aa123456',
            'secret': 'Aa123456',  # אם יש צורך במצב enable
        }

        # התחברות לנתב 1
        with ConnectHandler(**router1) as net_connect1:
            net_connect1.enable()

            print("Connected!")

            # יצירת VLAN 5 בנתב 1
            commands1 = [
                'configure terminal',
                'vlan 5',
                'name VLAN_5',
                'exit',
                'interface e0/1',  # נניח שהחיבור ביניהם נמצא על הממשק e0/1
                'switchport mode access',
                'switchport access vlan 5',
                'exit'
            ]
            net_connect1.send_config_set(commands1)
            print("VLAN 5 נוצר בנתב הראשון")

    except Exception as e:
        print(f"Error occurred while configuring router 1: {e}")
