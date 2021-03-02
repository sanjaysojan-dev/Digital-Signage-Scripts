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
	#launch_kiosk = open("launch_kiosk.sh", "a")
	#launch_kiosk.write("\n sleep 15 \n")
	#launch_kiosk.write("firefox -kiosk 192.168.0.36/imageSlider/" + str(input))
	#launch_kiosk.close()

	readFile = open("launch_kiosk.sh")
	lines = readFile.readlines()
	readFile.close()
	w = open("launch_kiosk.sh",'w')
	w.writelines([item for item in lines[:-1]])
	w.close()

	launch_kiosk = open("launch_kiosk.sh", "a")
	launch_kiosk.write("firefox -kiosk 192.168.0.36/imageSlider/" + str(input))

	


#MAIN PROGRAM STARTS HERE:
age = inputNumber("PLEASE ENTER NODE NUMBER: ")
