# Utransfer

A cloud based data transfer/storage django application.

All the data is stored on S3 and for user details MongoDB has been used.
 
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
