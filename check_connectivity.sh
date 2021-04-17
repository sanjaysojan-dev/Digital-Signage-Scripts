sleep 10
ping -c 3 www.google.com > /dev/null
if [ $? = 0 ]
then
echo "CONNECTION STATUS: ONLINE "
cd /home/pi/
sh launch_kiosk.sh
else
echo "CONNECTION STATUS: OFFLINE - Please check WiFi or Ethernet Connection" exec bash;
zenity --error --width=400 --height=150 --text="An error occurred! Please check Wi-Fi/Ethernet connection: Unable to connect to the internet" --title="Warning - No Internet Connection !"
fi
