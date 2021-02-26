import os

def inputNumber(message):
  while True:
    try:
       userInput = int(raw_input(message))       
    except ValueError:
       print("NOT A VAILD INTEGER. PLEASE TRY AGAIN")
       continue
    else:
       writeCommandToFile(userInput)
       return userInput 
       break 



def writeCommandToFile (input):
	launch_kiosk = open("launch_kiosk.sh", "w")
	launch_kiosk.write("sleep 15 \n")
	launch_kiosk.write("firefox -kiosk 192.168.1.177/imageSlider/" + str(input))
	launch_kiosk.close()

#MAIN PROGRAM STARTS HERE:
age = inputNumber("PLEASE ENTER NODE NUMBER: ")
