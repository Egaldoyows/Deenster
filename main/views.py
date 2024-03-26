from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import date
from django.contrib import messages

from .  models import Desination,Tour,Package,Hotel
from .forms import CreateUserForm,LoginForm
from django.db.models import Count



from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.







def index_view(request):
    
        destinations = Desination.objects.annotate(num_hotels=Count('hotel')).all()
        today=date.today()
        packages_all=Package.objects.filter(end_date__gte=today)[:10]
        
        
        return render(request, 'index.html', {'destinations': destinations,'hot':packages_all})




        

       
                
                
        
                

            


def packages_view_all(request):
    if request.method=='GET':
        
        destination_name = request.GET['name']
        destination = Desination.objects.get(des_name=destination_name)
        hotels_in_maasai_mara = Hotel.objects.filter(dest_id=destination)
        
        
        # packages=Package.objects.filter(destination=hotel_instance)
        packages=Package.objects.filter(name__in=hotels_in_maasai_mara)
        
    
    

        context={
            "packages": packages,
            "name":destination_name
            
            
        }
        return render(request, 'package.html',context)


         






def hotel_view(request):
    if request.method=='GET':
        name = request.GET['name']
        destination_instance = Desination.objects.get(des_name=name)
        packages = Package.objects.filter(destination=destination_instance)
        # hotels_with_packages = hotels_with_package_counts.filter(num_packages__gt=0)
    

        context={
            "hotels": packages,
            "name":name,
            
            
        }
    

    return render(request, 'package.html',context=context)






def book_view(request):
    
    if request.method=='GET':
        id =int(request.GET['id'])
        package=Package.objects.get(id=id)

        context={
            "package": package,
            
        }


    return render(request, 'bookings.html', context=context)






def tour_save(request):
    
    if request.POST:
        full_name=request.POST['fullname']
        email=request.POST['email']
        identity_number=request.POST['identity']
        phone_number=request.POST['phone']
        naitionality=request.POST['resident']
        package=request.POST['package']
        mode=request.POST['price']
        
        if package:
            package_id=int(package)
            package_new =Package.objects.get(pk=package_id)



        

            if 'Land Cuiser' in mode:
                 price = package_new.cruiser_price
            
            elif 'Van' in mode:
              price = package_new.van_price

            else:
                price = package_new.cruiser_price


        else: 
            return render(request,'bookings.html',context={'exists':"No Package Selected "})
         
            
        
        if Tour.objects.filter(email=email).exists():
           
           return render(request,'bookings.html',context={'fail':"Email Has been Used in an existing Booking, Please use another Email or contact us for help"})
        
        else:
           booking=Tour.objects.create(full_name=full_name,email=email,identity_number=identity_number,phone_number=phone_number,naitionality=naitionality,package=package_new,price=price)
        
           subject = 'Booking Request Confirmation'
           message = 'Dear '+ full_name +' Your Booking has been received and is being acted on. We shall notify you in due course. Thank you for choosing Deenster.'
           from_email = 'noreply@deenstertours.com'
           recipient_list = ['egaldoyows@gmail.com']

           send_mail(subject, message, from_email, recipient_list)
           

           return render(request,'bookings.html',context={'success':f"Booking request has been submitted successfully. A confirmation email has been sent to {email}. Thank you for choosing Deenster!"})
        




def single_package(request):

    if request.method=='GET':
        id =int(request.GET['id'])
        package=Package.objects.get(id=id)
        schedule = package.schedule.all().order_by('days')
        

        context={
            "package": package,
            "schedule": schedule
            
        }
        return render(request,'package-view.html',context=context)
    
    else:
        return render(request,'package-view.html',{"error":"No package selected"})
    




def manage_packages(request):
    
        packages =Package.objects.all()
        
        return render(request, 'manage-package.html', {'packages': packages})



    

   

   






            

        
        
        

        
        

