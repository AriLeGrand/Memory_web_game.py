from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def login(request):
    return render(request, 'LLR/login.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'LLR/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request,'Myapp/home.html')
        else:
            messages.success(request, ('Invalid username or password'))
            return render(request, 'LLR/login.html') 
        
    else:
        return render(request, 'LLR/login.html')
            


# from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from .forms import LoginForm
# from .forms import LogoutForm


# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # Handle registration logic here
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             confirm_password = form.cleaned_data['confirm_password']
#             # Add your registration logic using username, email, and password
#             return redirect('success_page')  # Replace 'success_page' with your desired success page
#     else:
#         form = RegisterForm()

#     return render(request, 'login.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # Handle authentication logic here
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             # Add your authentication logic using username, email, and password
#             return redirect('success_page')  # Replace 'success_page' with your desired success page
#     else:
#         form = LoginForm()

#     return render(request, 'register.html', {'form': form})


# def log_out_views(request): 
#     logout(request) #redirect to the desired page after logout  
#     return redirect('home')