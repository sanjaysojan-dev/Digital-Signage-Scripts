echo "CHECKING INTERNET CONNECTION"

ping -w 5 www.google.co.uk

echo "Exit Code: " $?

if [ $? -eq 0 ]; then 
	echo "CONNECTION STATUS: ONLINE"
	echo "ISNTALLING Mozilla Firefox"
	sudo apt-get install firefox-esr

	cd /home/pi/Documents/Digital-Signage-Scripts/

	ls 

	python launch_kiosk_config.py
	
	cp launch_kiosk.sh /home/pi/

	cp check_connectivity.sh /home/pi
	
	cp launcher.desktop /home/pi/.config/autostart/
	
	#sudo reboot
	
	
	
else
	echo "CONNECTION STATUS: OFFLINE - Please check WiFi or Ethernet Connection"
fi
