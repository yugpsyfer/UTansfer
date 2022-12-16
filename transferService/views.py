from django.shortcuts import render
from Utransfer.utils import get_user_db_handle, get_db_handle_secondary
from .models import UploadFile
from django.core.files.storage import default_storage

# Create your views here.

def upload_file(request):
    
    if request.method == "POST" and request.FILES["file"]:
        file = request.FILES["file"]
        file_name = file.name
        file_details = UploadFile()
        file_details.file = file
        default_storage.save(file_name, file_details.file)
        file_details.file_url = "url to your S3 bucket"+ file_name

        
        db_primary = get_user_db_handle()
        db_secondary = get_db_handle_secondary()
        
        user_collections = db_primary["userData"]
        user_collections.insert_one(file_details.to_dict())

        db_secondary["userData"].insert_one(file_details.to_dict())

    return render(request, 'userService/profile.html')


