from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('product_list')
            elif user_type == '2':
                return HttpResponse('product_list')
            elif user_type == '3':
                return HttpResponse('product_list')
            else:
                messages.error(request, 'Повторите Пароль или Эл.Почту')
                return redirect('login')
        else:
            messages.error(request, 'Повторите Пароль или Электронную Почту')
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')



def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user":user,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('home')
        except:
            messages.error(request, 'Failed to Update Profile')

    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new User object
        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Redirect to the registration success page
        return redirect('login')

    return render(request, 'registration.html')