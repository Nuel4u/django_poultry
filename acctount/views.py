from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from .form import ContactForm
# Create your views here.

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "form" :contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

def cleaned_email(self):
    email = self.cleaned_data.get("email")
    if not "gmail.com" in email:

        raise forms.ValidationError("email has to be in gmail only.")
        return email







def login(request):
    if request.method == 'POST':
        user_n = request.POST['username']
        paswod = request.POST['password']

        user = auth.authenticate(username = user_n , password = paswod)

        if user is not None:
            auth.login(request ,user)
            return redirect('/')

        else:
            messages.info(request ,'Invalid username or password')
            return redirect('login')    

    

    else:
        return render(request ,'login.html')

def register(request):
    if request.method == 'POST':

        fname = request.POST["fname"]
        lname = request.POST["lname"]
        usern = request.POST["Username"]
        passw = request.POST['Password']
        confirm_p = request.POST["cpassword"]
        mail = request.POST['mail']

        if passw == confirm_p:
            if User.objects.filter(username = usern).exists():
                messages.info(request , 'Username already used')
                return redirect('register')
                #print('Username already used')
            elif User.objects.filter(password = passw).exists(): 
                messages.info(request ,"password taken")
                return redirect('register')   

            elif User.objects.filter(email = mail).exists(): 
                messages.info(request ,"Email already taken")
                return redirect('register')
                #print('Email already taken') 

            else:
                user = User.objects.create_user(first_name =fname ,last_name =lname ,email = mail ,username =usern , password = passw)
                user.save();
                #messages.info(request ,'Registration was successful')
                return redirect('/') 
                messages.info(request ,'Registration was successful')

            
        else:
            messages.info(request ,"Password does not match")
            return redirect('register')
            #print(" password does not match") 


        return redirect('/')      


         


    else:
        return render(request ,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
    #return render(request ,'login.html')

def animate(request):
    content ={
        "title" :"animating things"
    }
    return render(request ,'animate.html',content) 

def heading(request):
    return redirect('heading.html') 
     


def head(request):
    return redirect('live')

#def recipe(request):
 #   return render(request ,'base.html')