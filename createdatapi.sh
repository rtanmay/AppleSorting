#!bin/bash
ssh user@192.168.10.101 'bash -s' < im.sh
cd /home/tanmay/Desktop/GIT/AppleSorting/data/
# Send this image to my system
scp -r user@192.168.10.101:~/Desktop/AppleSorting/data/good/ ./