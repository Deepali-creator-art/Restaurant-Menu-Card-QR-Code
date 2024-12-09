from django.shortcuts import render
from .forms import QRcodeform
import qrcode
import os
from django.conf import settings

def home(request):
    if request.method=='POST':
        #create object of QRcodeform class post method
        qr_form=QRcodeform(request.POST)
        if qr_form.is_valid():
            res_name = qr_form.cleaned_data['restaurant_name']
            url = qr_form.cleaned_data['menucardlink']
            #generate qr code
            qr_image=qrcode.make(url)
            #to  rename file name
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            #to save qrcode in media folder
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) 
            qr_image.save(file_path)
            # Create Image URL
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            context={
                'qr_url':qr_url,
                'res_name':res_name,
                'file_name':file_name
            }
            return render(request,'qrfile.html',context)
            
           
    else:    
        #create object of QRcodeform class get method
        qr_form=QRcodeform()
        context={'qr_form':qr_form}
        return render(request,'home.html',context)