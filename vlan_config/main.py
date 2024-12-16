# main.py
from config.router1_config import configure_router1
from config.router2_config import configure_router2
from netmiko import ConnectHandler

def test_connectivity():
    try:
        # התחברות לנתב 1
        router1 = {
            'device_type': 'cisco_ios',
            'host': '192.170.0.66',  # כתובת ה-IP של הנתב הראשון
            'username': 'admin',
            'password': 'Aa123456',
            'secret': 'Aa123456',
        }
        with ConnectHandler(**router1) as net_connect1:
            net_connect1.enable()

            # שליחת פינג מנתב 1 לנתב 2
            ping_command = 'ping 192.170.0.65'
            output1 = net_connect1.send_command(ping_command)
            print("ping from device 1 to device 2\n", output1)

        # התחברות לנתב 2
        router2 = {
            'device_type': 'cisco_ios',
            'host': '192.170.0.65',  # כתובת ה-IP של הנתב השני
            'username': 'admin',
            'password': 'Aa123456',
            'secret': 'Aa123456',
        }
        with ConnectHandler(**router2) as net_connect2:
            net_connect2.enable()

            # שליחת פינג מנתב 2 לנתב 1
            output2 = net_connect2.send_command(ping_command)
            print("ping from device 2 to device 1\n", output2)

    except Exception as e:
        print(f"Error occurred during connectivity test: {e}")

def main():
    try:
        # קונפיגורציה לנתב 1 ונתב 2
        configure_router1()
        configure_router2()

        # בדיקת תקשורת בין הנתבים
        test_connectivity()

    except Exception as e:
        print(f"Error occurred during main execution: {e}")

if __name__ == '__main__':
    main()
