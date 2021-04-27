import os
import requests



def inputNumber():

    try:

        r = requests.get("http://www.google.co.uk", timeout=10)

        print("CONNECTION STATUS: ONLINE")

        print("INSTALLING Mozilla Firefox")

        os.system("sudo apt-get install firefox-esr")
	os.system("sudo apt-get install zenity")
	



        while True:

            try:

                print(">> PLEASE ENTER NODE NUMBER: ")

                userInput = int(raw_input())

            except ValueError:

                print("NOT A VAILD INTEGER. PLEASE TRY AGAIN")

                continue

            else:

                writeCommandToFile(userInput)

                return userInput

                break 

    except requests.ConnectionError as ex:

        print("CONNECTION STATUS: OFFLINE - Please check WiFi or Ethernet Connection")

    
def writeCommandToFile (input):
	launch_kiosk = open("launch_kiosk.sh", "w")
	launch_kiosk.write("firefox -kiosk 192.168.0.36/imageSlider/" + str(input))
	launch_kiosk.close()
	
	os.system("cp check_connectivity.sh /home/pi")
	os.system("cp launch_kiosk.sh /home/pi/")
	os.system("cp launcher.desktop /home/pi/.config/autostart/")
	#os.system("sudo reboot")   


#MAIN PROGRAM STARTS HERE:
inputNumber()
