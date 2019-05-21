#!bin/bash

# TO DO : Assign static ip to rpi, this will be given to the ip_here DONE
# TO DO : ssh-copy-id -i ~/.ssh/id_rsa.pub pi@ip_here  DONE

ssh user@192.168.10.101 'bash -s' < runpi.sh

# cd /home/user/Desktop/AppleSorting
# raspistill -t 500 -o try.jpg
# exit

cd /home/tanmay/Desktop/GIT/AppleSorting
# Send this image to my system
scp user@192.168.10.101:~/Desktop/AppleSorting/try.jpg ./
python3 run.py > Angle.txt
scp ./Angle.txt user@192.168.10.101:~/Desktop/AppleSorting/
