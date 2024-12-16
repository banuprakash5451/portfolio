from django.shortcuts import render,get_object_or_404,redirect
from portfo.models import *
from django.http import FileResponse,HttpResponse
import os
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def home(request):
    profile_info=Profile.objects.last()
    education_details=Education.objects.reverse().order_by('year_of_start')
    skills=Skill.objects.all()
    project_details=Project.objects.all().reverse()
    # print(profile_info,education_details,skills,project_details)
    document = Document.objects.last()  
    if request.method=='POST':
        uname=request.POST.get('name')  
        uemail=request.POST.get('replyto')  
        umessage=request.POST.get('message')
        data = contected(name=uname, email=uemail,message=umessage) 
        data.save()
    return render(request, 'index.html', {'info':profile_info,
                                          'document': document,
                                          'education':education_details,
                                          'skills':skills,
                                          'project':project_details,
                                          })


def download_file(request, file_id):
    doc = get_object_or_404(Document, id=file_id)
    file_path = doc.document.path  
    if os.path.exists(file_path):
        file = open(file_path, 'rb')
        response = FileResponse(file, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{doc.document.name}"'
        return response
    else:
        return HttpResponse("File not found", status=404)