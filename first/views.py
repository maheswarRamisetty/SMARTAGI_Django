from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import SignUpForm
from django.conf import settings
import random
from django.core.mail import send_mail
import string
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Register
from math import sqrt
from .models import LOTP
from .forms import SignInForm
from django.contrib import messages
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def generate_otp4():
    return ''.join(random.choices(string.digits, k=4))

def generate_otp8():
    return ''.join(random.choices(string.digits, k=8))

def mahiValid(s_otp,e_otp):
     return s_otp==e_otp + 2*(sqrt(0.5))

def cheap(request):
    return HttpResponse("<h1>Default Route</h1>")

def login(request):
    return render(request,"LOGIN_OTP.html")

def home(request):
    if not request.session.get('visited_home', False):
        request.session['visited_home'] = True
    return render(request, "ss.html")
def get_last_row():
    try:
        last_row = Register.objects.last()
        return last_row
    except Register.DoesNotExist:
        return None
def send_otp_email(request):
    email = request.session.get('email')

    otp = request.session.get('otp')

    if email and otp:
        subject = 'Your OTP for Registration'

        message = f'Your OTP is: {otp}'

        email_from = settings.EMAIL_HOST_USER

        recipient_list = [email]

        send_mail(subject, message, email_from, recipient_list)
    else:
        print("Email or OTP not found in session.")

def sendmail(request):
    pass

def signup(request):
    if not request.session.get('visited_home', False):
        return redirect('home')   

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']

                email = form.cleaned_data['email']

                password = form.cleaned_data['password']  

                otp = generate_otp()

                request.session['otp'] = otp

                request.session['email'] = email

                send_mail(
                    'Validate Form',  
                    f'Your OTP is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )  

                Register.objects.create(username=username, email=email, password=password, otp=otp)
                print("Data saved successfully to the database.")
                
                return render(request, 'REGISTER_OTP.html')
              
            except Exception as e:
                print(f"Error occurred while saving data: {e}")
                return render(request, 'error.html', {'error_message': 'An error occurred while saving data. Please try again.'})
        else:
            print("Form is not valid. Errors:", form.errors)
            return HttpResponse("<h1>Hello</h1>")
    else:
        form = SignUpForm()
        return HttpResponse("<h1>Hello</h1>")
def get_first_row_with_otp():
    try:
        first_row_with_otp = Register.objects.filter(otp__isnull=False).first()
        if first_row_with_otp:
            return first_row_with_otp.otp
        else:
            return None  
    except Exception as e:
        print(f"Error occurred while retrieving the first row with OTP: {e}")
        return None  
def get_last_row_login():
    try:
        last_row = LOTP.objects.last()
        return last_row
    except LOTP.DoesNotExist:
        return None
def verify_otp(request):
    if request.method == 'POST':
        otp_entered=''
        if request.method == 'POST':

            otp_entered+=(request.POST.get('otp1',''))
            otp_entered+=(request.POST.get('otp2',''))
            otp_entered+=(request.POST.get('otp3',''))
            otp_entered+=(request.POST.get('otp4',''))
            otp_entered+=(request.POST.get('otp5',''))
            otp_entered+=(request.POST.get('otp6',''))

            stored_otp = get_last_row().otp;

            print(stored_otp,otp_entered)
           
            if otp_entered == stored_otp:
           
                return HttpResponse("OTP Verified Successfully!")
            else:
                return HttpResponse("Invalid OTP. Please try again.")
        else:
            return HttpResponse("User not found.")
    else:
        return HttpResponse("Method not allowed.")

global N
N = 4

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print (board[i][j],end=' ')
		print()
          

def isSafe(board, row, col):
	for i in range(col):
		if board[row][i] == 1:
			return False
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True

def solveNQUtil(board, col):
	if col >= N:
		return True
	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1
			if solveNQUtil(board, col + 1) == True:
				return True
			board[i][col] = 0
	return False
def solveNQ():
	board = [ [0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
			]
	if solveNQUtil(board, 0) == False:
		print ("Solution does not exist")
		return False
	printSolution(board)
	return True
def signin1(request):
    if request.method == 'POST':
        signin_username = request.POST.get('signin_username') 
        signin_password = request.POST.get('signin_password')

        try:
            user = Register.objects.get(username=signin_username)
        except Register.DoesNotExist:
           
            return render(request, 'Mahesh.html', {'signin_error': 'Invalid username or password'})
     
        if user.check_password(signin_password):
           
            login(request, user)
            return redirect('home')  
        else:
           
            return render(request, 'Mahesh.html', {'signin_error': 'Invalid username or password'})

    else:
        return render(request, 'Mahesh.html')
    

def signin(request):
    if request.method == 'POST':
        #form = SignInForm(request.POST)
        signin_username = request.POST.get('signin_username') 
        signin_password = request.POST.get('signin_password')
        try:
            user = Register.objects.get(username=signin_username)
        except Register.DoesNotExist:
            return render(request, 'Mahesh.html', {'signin_error': 'Invalid username or password'})
        if user.password == signin_password:
            #email = form.cleaned_data['email']
            otp = generate_otp4()
            print(otp)
            send_mail(
                 'Validate Form',  
                    f'Your OTP is: {otp}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False
            )
            otp_log = LOTP.objects.create(otpL=otp)
            return render(request,'LOGIN_OTP.html')
        else:
            return render(request, 'Mahesh.html', {'signin_error': 'Invalid username or password'})
    else:
        return render(request, 'Mahesh.html')
    
def lvf(request):
     if request.method == 'POST':
          otp_entered=''
          if request.method == 'POST':

            otp_entered+=(request.POST.get('otp1',''))
            otp_entered+=(request.POST.get('otp2',''))
            otp_entered+=(request.POST.get('otp3',''))
            otp_entered+=(request.POST.get('otp4',''))

            stored_otp = get_last_row_login().otpL;

            print(stored_otp,otp_entered)
           
            if otp_entered == stored_otp:
                messages.success(request, "OTP Verified Successfully.")
                return HttpResponse('<h1>Login Successs<h1>')
            else:
                return render(request,'Mahesh.html')