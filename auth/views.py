from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from django.db.models import Count

# Project database model.
from main.models import Desination,Tour,Package,Hotel,Activity,Addon
from .forms import PackageForm,ActivityForm,HotelForm,DestinationForm,CreateUser




# Authentication classes.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from main.forms import CreateUserForm,LoginForm
from django.contrib.auth.forms import UserCreationForm

# Email sending classes.
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def authView(request):
    form=UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form =UserCreationForm()

    return render(request,'registration/signup.html',{'form':form})






def user_login(request):
    loginForm=LoginForm()
    if request.method=='POST':
        loginForm=LoginForm(request,request.POST)
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            return redirect("home")
        else:
            context={
                "loginForm":loginForm,
                "error":"Wrong username or password"
            }
        
    else: 
        loginForm=LoginForm
        context={
                "loginForm":loginForm,
                "new":"Note: username and password are case sensitive *"
            }

    

    return render(request,'registration/login.html',context=context)


#Login User



def user_logout(request):
    logout(request)

    return render(request,'registration/login.html',context={})





@login_required
def dashboard_view(request):
    tour=Tour.objects.filter(reject_status=False,book_status=False).order_by('-created')
    
    context={
        "tours": tour
    }

    return render(request, 'registration/dashboard.html',context)






@login_required
def booked_customers(request):
    tour=Tour.objects.filter(book_status=True).order_by('-created')
    context={
        'tours': tour,
        'category': "Booked Customers"
    }
    return render(request, 'registration/customers_list.html',context)

@login_required
def rejected_customers(request):
    tour=Tour.objects.filter(reject_status=True).order_by('-created')
    context={
        'tours': tour,
        'category': "Rejected Bookings",
        
    }
    return render(request, 'registration/rejected-list.html',context)




@login_required
def travelor_view(request):
    if request.method=='GET':
        tid =int(request.GET['id'])
        try:
            travelor = Tour.objects.get(id=tid)
            context = {
                "tour": travelor  # Change the key to "tour"
            }
        except Tour.DoesNotExist:
            # Handle the case where the tour with the specified ID does not exist
            pass
    else:
        context = {"travelor":tid}  # Provide a default context in case of a GET request
    
    return render(request, 'registration/travelor.html', context=context)


@login_required
def reject_booking (request):
    if request.method=='GET':
        id =int(request.GET['id'])
        travelor = Tour.objects.get(id=id)
        travelor.reject_status=True
        travelor.updated_on=timezone.now()
        travelor.reject_reason="Your Booking has been reject for some reason"
        travelor.save()


    return render(request, 'registration/dashboard.html', context={"reject":"reject"})



@login_required
def single_accepted(request):
    if request.method=='GET':
        tid =int(request.GET['id'])
        try:
            travelor = Tour.objects.get(id=tid)
            context = {
                "tour": travelor  # Change the key to "tour"
            }
        except Tour.DoesNotExist:
            # Handle the case where the tour with the specified ID does not exist
            pass
    else:
        context = {"tour":"Could not fetch any data"}  # Provide a default context in case of a GET request
    
    return render(request, 'registration/single-accepted.html', context=context)



@login_required
def single_rejected(request):
    if request.method=='GET':
        tid =int(request.GET['id'])
        try:
            travelor = Tour.objects.get(id=tid)
            context = {
                "tour": travelor  # Change the key to "tour"
            }
        except Tour.DoesNotExist:
            # Handle the case where the tour with the specified ID does not exist
            pass
    else:
        context = {"tour":"Could not fetch any data"}  # Provide a default context in case of a GET request
    
    return render(request, 'registration/single-rejected.html', context=context)












@login_required
def accept_booking (request):
    if request.method=='GET':
        id =int(request.GET['id'])
        try:
            travelor = Tour.objects.get(id=id)
            travelor = Tour.objects.get(id=id)
            travelor.book_status=True
            travelor.updated_on=timezone.now()
            travelor.save()
            
            subject = 'NEW Deenster Booking Request'
            # message = 'Full Name: '+ travelor.full_name +' ID Number: '+ travelor.identity_number + ' Email '+ travelor.email
            from_email = 'noreply@deenstertours.com'
            recipient_list = ['egaldoyows@gmail.com']

            # send_mail(subject, message, from_email, recipient_list)

            html_content=render_to_string("mails/requests.html",{"title":"Booking Request","name":travelor.full_name,"package":travelor.package,"contact":travelor.number,"email":travelor.email})
            text_content=strip_tags(html_content)
            email=EmailMultiAlternatives(
                #subject
                subject,
                #content
                text_content,
                #From
                from_email,
                #receipent list
                recipient_list

            )

            email.attach_alternative(html_content,"text/html")
            email.send()

            return HttpResponse('Email sent successfully!')
            
        except Tour.DoesNotExist:
            # Handle the case where the tour with the specified ID does not exist
            pass

    else:
       return HttpResponse('Email Not Sent!')
    



@login_required
def create_package(request):
    item_form=PackageForm()
    if request.method=='POST':
        item_form=PackageForm(request.POST,request.FILES)
        if item_form.is_valid():
            item_form.save()
            item_form=PackageForm()

            context={
                "form_type": "Create Package",
                "form": item_form

            }

            return render(request, 'registration/create-package.html',context=context)
            
    else:

        context={
                "form_type": "Create Package",
                "form": item_form

            }
        return render(request, 'registration/create-package.html',context=context)
    



@login_required
def create_activity(request):
    item_form=ActivityForm()
    if request.method=='POST':
        item_form=ActivityForm(request.POST,request.FILES)
        if item_form.is_valid():
            item_form.save()
            item_form=ActivityForm()

            context={
                "form_type": "Create Activity",
                "form": item_form

            }

            return render(request, 'registration/create-activity.html',context=context)
            
    else:

        context={
                "form_type": "Create Activity",
                "form": item_form

            }
        return render(request, 'registration/create-activity.html',context=context)
    



@login_required
def create_Hotel(request):
    item_form=HotelForm()
    if request.method=='POST':
        item_form=HotelForm(request.POST,request.FILES)
        if item_form.is_valid():
            item_form.save()
            item_form=HotelForm()

            context={
                "form_type": "Create Hotel",
                "form": item_form

            }

            return render(request, 'registration/create-hotel.html',context=context)
            
    else:

        context={
                "form_type": "Create Hotel",
                "form": item_form

            }
        return render(request, 'registration/create-hotel.html',context=context)




@login_required
def create_Destination(request):
    item_form=DestinationForm()
    if request.method=='POST':
        item_form=DestinationForm(request.POST,request.FILES)
        if item_form.is_valid():
            item_form.save()
            item_form=DestinationForm()

            context={
                "form_type": "Create Destination",
                "form": item_form

            }

            return render(request, 'registration/create-dest.html',context=context)
            
    else:

        context={
                "form_type": "Create Destination",
                "form": item_form

            }
        return render(request, 'registration/create-dest.html',context=context)
    

@login_required
def SingleHotelView(request):
    if request.method=='GET':
        id =int(request.GET['id'])
        item=Hotel.objects.get(id=id)


    return render(request,'registration/item-view.html',{'item':item,'name':'Hotel'})

@login_required
def SingleDestView(request):
    if request.method=='GET':
        id =int(request.GET['id'])
        item=Desination.objects.get(id=id)


    return render(request,'registration/item-view.html',{'item':item,'name':'Destination'})
    








@login_required
def manage_view(request):
    destinations = Desination.objects.all()
    activities=Activity.objects.all()
    addons=Addon.objects.all()

    # Create a list to store destination and associated hotels
    destination_list = []
    for destination in destinations:
        hotels = Hotel.objects.filter(dest_id=destination)
        destination_data = {
            'destination': destination,
            'hotels': hotels,
        }
        destination_list.append(destination_data)

    context = {
        'destination_list': destination_list,
        'activites': activities,
        'addons':addons
    }

    return render(request, 'registration/manage.html', context)

@login_required
def activity_edit(request):
    a_id=int(request.GET['id'])
    activity=Activity.objects.get(id=a_id)
    form=ActivityForm(instance=activity)
    context={
            "form": form
        }

    if request.method=='POST':
        form=ActivityForm()
        new_form=ActivityForm(request.POST,instance=activity)
        if new_form.is_valid():
            new_form.save
            return redirect('activity-edit')
    
    else:
         context={
            "form": form
        }

         return render(request,'registration/activity-edit.html',context)
    


def managePackages(request):
    packages=Package.objects.all()

    return render(request,"registration/manage-packages.html",{"packages":packages})



def edit_package(request):
    package_id=int(request.GET['package_id'])
    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST,request.FILES, instance=package)
        if form.is_valid():
            form.save()
            packages=Package.objects.all()
            
            return render(request,'registration/manage-packages.html', {"packages":packages})
    else:
        form = PackageForm(instance=package)

    return render(request, 'registration/edit-package.html', {'form': form, 'package': package})


def package_delete(request):
    if request.method=='GET':
        package_id=int(request.GET['package_id'])
        package = Package.objects.get(id=package_id)
        return render(request, 'registration/confirm-delete.html', {'package': package})

    if request.method=='POST':
        package_id=int(request.GET['package_id'])
        package = Package.objects.get(id=package_id)
        package.delete()
        
    return redirect('package-manager')


def advanced_Settings(request):

    
    return render(request,"registration/advanced.html",{})

    



        
   
          

    
  
                

    
            