sleep 10
echo "CHECKING CONNECTION TO HOST"

ping -w 5 www.google.co.uk

echo "Exit Code: " $?

if [ $? -eq 0 ]; then 
	echo "CONNECTION STATUS: ONLINE "
	cd /home/pi/
	sh launch_kiosk.sh
else
	echo "CONNECTION STATUS: OFFLINE - Please check WiFi or Ethernet Connection"
fi
