from datetime import datetime as dt
import time

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.teamtrees.org", "teamtrees.org", "www.wix.com", "wix.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        print("Working hours")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Non-working hours")
    time.sleep(5)
