#!bin/bash

# TO DO : Assign static ip to rpi, this will be given to the ip_here
# TO DO : ssh-copy-id -i ~/.ssh/id_rsa.pub pi@ip_here 

ssh pi@ip_here

cd Desktop/AppleSorting
raspistill -t 500 -o try.jpg
exit

cd /home/tanmay/Desktop/GIT/AppleSorting
# Send this image to my system
scp pi@ip_here:/try.jpg ./

# Angle.txt contains the Angle to be given to servo motor
python3 run.py > Angle.txt

scp ./Angle.txt pi@ip_here:/home/pi/Desktop/AppleSorting

ssh pi@ip_here
cd Desktop/AppleSorting

# proj.py takes angle as input and then run servo 
python3 proj.py < Angle.txt
