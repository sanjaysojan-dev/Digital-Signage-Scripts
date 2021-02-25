echo "CHECKING INTERNET CONNECTION"

ping -w 5 www.google.co.uk

echo "Exit Code: " $?

if [ $? -eq 0 ]; then 
	echo "CONNECTION STATUS: ONLINE"
	echo "ISNTALLING Mozilla Firefox"
	sudo apt-get install firefox-esr
else
	echo "CONNECTION STATUS: OFFLINE - Please check WiFi or Ethernet Connection"
fi
