# router2_config.py
from netmiko import ConnectHandler

def configure_router2():
    try:
        router2 = {
            'device_type': 'cisco_ios',
            'host': '192.170.0.65',  # כתובת ה-IP של הנתב השני
            'username': 'admin',
            'password': 'Aa123456',
            'secret': 'Aa123456',  # אם יש צורך במצב enable
        }

        # התחברות לנתב 2
        with ConnectHandler(**router2) as net_connect2:
            net_connect2.enable()

            print("Connected!")


            # יצירת VLAN 5 בנתב 2
            commands2 = [
                'configure terminal',
                'vlan 5',
                'name VLAN_5',
                'exit',
                'interface e0/1',  # נניח שהחיבור ביניהם נמצא על הממשק g0/1
                'switchport mode access',
                'switchport access vlan 5',
                'exit'
            ]
            net_connect2.send_config_set(commands2)
            print("VLAN 5 נוצר בנתב השני")

    except Exception as e:
        print(f"Error occurred while configuring router 2: {e}")
