from django.shortcuts import render, redirect
from usuarios.forms import CustomUserCreationForm, LoginForm#, RegisterForm#, CustomUserChangeForm
from django.contrib import auth, messages
from usuarios.models import CustomUser

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    # Usuario Teste
    # Abacate2020
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form['username'].value()
            email = form['email'].value()
            password_1 = form['password1'].value()
            first_name = form['first_name'].value()
            last_name = form['last_name'].value()
            address = form['address'].value()
            user_image = form.cleaned_data.get('user_image')
            
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Usuário já existe!")
                return render(request, 'usuarios/register.html', {"form":form})
            
            user = CustomUser.objects.create(
                username=username,
                email=email,
                password=password_1,
                first_name=first_name,
                last_name=last_name,
                address = address,
                user_image = user_image
            )

            user.set_password(request.POST['password1'])
            user.save()

            messages.success(request, f"{username} agora está registrado como usuário!")
            return redirect('login')

    return render(request, 'usuarios/register.html', {"form":form})

def login(request):
    form = LoginForm()

    # print(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

            # print("USUARIO", username)
            # print("SENHA", password)

            user = auth.authenticate(
                request,
                username=username,
                password=password
            )

            # print(user)

            if user is not None:
                auth.login(request, user)
                messages.success(request, f"{username} logado com sucesso!")
                return redirect('index')
            messages.error(request, "usuário/senha estão incorretos ou usuário não existe!")
            return redirect('login')
    # print("GET")
    return render(request, 'usuarios/login.html', {"form":form})
    # return render(request, 'usuarios/login.html')