from django.shortcuts import render, redirect

def get_home(request):
    if request.user.is_authenticated:
        return redirect('searchpage')
    else:
        return redirect('login')
