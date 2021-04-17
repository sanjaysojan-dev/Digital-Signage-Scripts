sleep 10
ping -c 3 www.google.com > /dev/null
if [ $? = 0 ]
then
echo "CONNECTION STATUS: ONLINE "
cd /home/pi/
sh launch_kiosk.sh
else
echo "CONNECTION STATUS: OFFLINE - Please check WiFi or Ethernet Connection" exec bash;
fi
