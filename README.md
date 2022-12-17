# Utransfer

### Description
A cloud based data transfer/storage django application. The media files are being stored on [S3 : https://aws.amazon.com/] and for user details MongoDB has been used. To run this application fire a S3 bucket and make a [mongoDB instance : https://cloud.mongodb.com]. Also change the settings.py as required, you can find comments. The database connector is in file utransfer/utils.py

To run the application on localhost:
```
pyhon manage.py runserver
```





To run the application on EC2 the instructions have been given below.
 
aws ec2 userdata installations:
```
#!/bin/bash

sudo apt update 
sudo apt install python3
sudo apt install python3-pip

pip install django
pip install pymongo 
pip install django-storages  
pip install boto3
pip install qrcode
pip install pillow

cd /home
git clone https://<PAT>@github.com/<git-repo>

python3 manage.py runserver 0.0.0.0:8000
```
