from doctest import master
from random import randint
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
# Create your views here.
default_data = {
    # 'user_roles' : Role.objects.all(), 
}
def role_view():
    default_data['role_data'] = Role.objects.all()

def profile_view():
    default_data['profile_data_view'] = Profile.objects.all()

# def del_status():
#     default_data['del_status'] = Profile.objects.all()

def shop_type_view():
    default_data['shop_type_data'] = Shop_Types.objects.all()

def del_type_view():
    default_data['del_type_data'] = Del_Status.objects.all()

def index(request):

    role_view()
    return render(request,'index.html',default_data)

def otp_page(request):
    return render(request,'otp.html')

def page(request):
    return render(request,'page.html')

def registration(request):
    print(request.POST)
    request.session['reg_data'] = {
        'role': int(request.POST['role']),
        'email':request.POST['email'],
        'password':request.POST['password'],
    }

    create_otp(request)
    return redirect(otp_page)

# create otp and send to email
def create_otp(request):
    email_to_list = [request.session['reg_data']['email'],]
    subject = "OTP varification for NEAR.in"

    otp = randint(1000, 9999)

    print('OTP is: ', otp)

    request.session['otp'] = otp

    message = f"Your One Time Password for verification is: {otp}"

    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, email_to_list)

# verification Functionality
def verify_otp(request):
    otp = int(request.POST['otp'])
    if otp == request.session['otp']:
        role = Role.objects.get(id=request.session['reg_data']['role'])
        master = Master.objects.create(
            Role = role,
            Email = request.session['reg_data']['email'],
            Password = request.session['reg_data']['password'],
            IsActive = True
        )
        Profile.objects.create(
            Master = master,
        )
        del request.session['otp']
        del request.session['reg_data']

        print('otp ver Succ')
        return redirect(login)
    else:
        print('invalid OTP')
    return redirect(index)

# def profile(request):
#     return HttpResponse('<h1>Done</h1>')

def login(request):
    return render(request, 'login.html')

def error_page(request):
    return render(request, 'error_page.html')

def profile_page(request):
    # default_data['current_page'] = 'profile_page'
    if 'email' not in request.session:
        return redirect(index)
    profile_data(request)
    profile_view()
    shop_type_view()
    del_type_view()
    # del_status()
    return render(request, 'profile_page.html', default_data)

def home_page(request):
    return render(request, 'home_page.html')

def user_login(request):
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect(home_page)
        else:
            return redirect(error_page)
    except Master.DoesNotExist as err:
        print(err)
        return redirect(login)
    
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    default_data['profile_data'] = profile

def profile_image_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    # if 'profile_image' in request.FILES:
    profile.ProfileImage = request.FILES['profile_image']
    profile.save()
    return redirect(profile_page)

def update_basic_details_merchant(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)
    # customer basic
    profile.OwnerName = request.POST['oname']
    profile.ShopName = request.POST['sname']
    profile.DOS = request.POST['dos']
    profile.Del_Status = Del_Status.objects.get(Del_Status = request.POST['del'])
    profile.Shop_Types = Shop_Types.objects.get(Shop_Types = request.POST['shoptype'])
    # dob = request.POST['dob'].split('-')[::-1]
    # print(dob)


    profile.Contact = request.POST['phonenumber']
    # profile.H_S_no = request.POST['sno']
    # profile.Complex_Name = request.POST['complex_name']
    # profile.Nr_Landmark = request.POST['landmark']
    profile.Country = request.POST['country']
    profile.State = request.POST['state']
    profile.City = request.POST['city']
    profile.Pincode = request.POST['pincode']
    profile.Address = request.POST['address']
    profile.save()
    return redirect(profile_page)

def update_basic_details_customer(request):

    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    profile.First_Name = request.POST['fname']
    profile.Last_Name = request.POST['lname']
    profile.DOB = request.POST['dob']
    profile.Gender = request.POST['gender']
    profile.Contact = request.POST['phonenumber']

    profile.Country = request.POST['country']
    profile.State = request.POST['state']
    profile.City = request.POST['city']
    profile.Pincode = request.POST['pincode']
    profile.Address = request.POST['address']
    profile.save()
    return redirect(profile_page)

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    
    return redirect(index)

def profileImage_remove(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    profile.ProfileImage = ''
    profile.save()
    return redirect(profile_page)

def profile_remove(request, pk):
    # Profile.objects.get(id=pk).delete()
    Master.objects.get(id=pk).delete()
    return redirect(index)