from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime
from accounts.models import Contact
from django.contrib import messages

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request,'contact.html')



def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')



    else:
        return render(request,'login.html')
    
    

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!')
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        

        else:
            messages.info(request,'password not maching!')
            return redirect('register')

        return redirect('/')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

