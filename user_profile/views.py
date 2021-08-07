from user_profile.forms import ExtendedUserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def register(request):

    if request.method=="POST":
        form=ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()

            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)


            login(request,user)
            return redirect('profile')
    else:
        form=ExtendedUserCreationForm()
    context={"form":form}
    return render(request, 'user_profile/register.html',context)


@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')