from asyncio.log import logger
from importlib.resources import open_binary
from multiprocessing import context
from ntpath import join
import zipfile
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from nbformat import read
import nltk
from . import main





def home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['myfile']
        
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        
        
    return render(request, 'polls/mainpage.html')




def regulated(request):
    y = main.fd.most_common(10)

    

    context= {"y":y}

    return render(request, 'polls/regulated.html', context)



