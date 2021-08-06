#!/bin/bash

clear

echo "
This script will download your files from your S3 bucket and stage them for Data Science processing.
						
Ensure that you enter the correct S3 bucket name used in Lab3.

"

echo "Enter your S3 bucket name and press [ENTER]:"
read s3name

echo "Enter your First Name and press [ENTER]:"
read fname

s3loc=$s3name/ml/trainingdata
echo $s3loc

cd SageMaker
wget https://partner-workshops-cn-northwest-1.s3.cn-northwest-1.amazonaws.com.cn/sh-scripts/Movie_Recommender_Lab5.ipynb
sed -i -e "s/S3bucket/$s3name/g" Movie_Recommender_Lab5.ipynb
sed -i -e "s/firstname/$fname/g" Movie_Recommender_Lab5.ipynb


mkdir $fname
cd $fname

aws s3 cp s3://$s3loc/rating/ . --recursive --exclude "*" --include "part*"
mv part* ratings.csv

aws s3 cp s3://$s3loc/movies/ . --recursive --exclude "*" --include "part*"
mv part* movies.csv

aws s3 cp s3://$s3loc/links/ . --recursive --exclude "*" --include "part*"
mv part* links.csv
