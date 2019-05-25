#!bin/bash
cd /home/user/Desktop/AppleSorting
mkdir data
cd data
mkdir good
cd good
for i in {1..100}
do
	raspistill -t 500 -tl 1000 -o $i.jpg
done
exit