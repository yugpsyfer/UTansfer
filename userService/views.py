from django.shortcuts import render
# from django.views.decorators.cache import cache_page
# from django.views.decorators.csrf import csrf_protect

from .models import User 

# import importlib.util       
# import os

from Utransfer.utils import get_user_db_handle, get_db_handle_secondary
import qrcode
from PIL import Image, ImageDraw
import io
import base64

# Create your views here.

def showfiles(request):
    try: 
        db = get_user_db_handle()
    except:
        db = get_db_handle_secondary()

    user_collections = db["userData"]
    user_data = user_collections.find({})
    files_list = []

    imageObject = []
    for dic in user_data:
        files_list.append(dic["file_url"])

        qr_code = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 30, border = 4)    
        qr_code.add_data(dic["file_url"])
        qr_code.make(fit = True)
        img = qr_code.make_image(back_color = "white", fill_color = "black")

        img_out = io.BytesIO()
        img.save(img_out, "PNG")
        img_contents = base64.b64encode(img_out.getvalue())
        img_out.close()

        imageObject.append(img_contents.decode("utf-8"))
        files_data = zip(files_list,imageObject)
		
    return render(request, 'transferService/view_files.html', context={"user_data":files_data}) 

def upload(request):
    return render(request, 'transferService/upload.html')

def make_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username_signup')
        email = request.POST.get('email_signup')
        password = request.POST.get('password_signup')

        user = User()
        user.user_name = username
        user.email = email
        user.password = password
        
        
        db_primary = get_user_db_handle()
        
        db_secondary = get_db_handle_secondary()

        userD = db_primary["userDetails"]
        userD.insert_one(user.to_dict())

        userD_secondary = db_secondary["userDetails"]
        userD_secondary.insert_one(user.to_dict())

        return render(request, 'userService/login.html')


def index(request):
    return render(request, 'userService/index.html')

def login(request):
    return render(request, 'userService/login.html')

def signup(request):
    return render(request, 'userService/signup.html')

def profile(request):
    username = request.POST.get('username_login')
    password = request.POST.get('password_login')

    try: 
        db = get_user_db_handle()
    except:
        db = get_db_handle_secondary()

    userD = db["userDetails"]

    data = userD.find_one({"user_name":username, "password":password})

    if data:
        user_details={"user_name":data["user_name"], "email":data["email"]}
        return render(request, 'userService/profile.html', context=user_details)
    else:
        return render(request, 'userService/failure.html')
