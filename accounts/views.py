from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

from django.urls import reverse_lazy
from django.views import generic

from bulletins.models import Bulletin, CommunityMembers


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def get_home(request):
    if not request.user.is_authenticated:
        redirect('login')
    return render(request, 'home.html', {})

def get_profile(request, name):
    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return render(request, 'profile_not_found.html', {'user_name':name})

    uname = u.username
    datejoined = u.date_joined
    member_of = CommunityMembers.objects.filter(members=u)
    communities = [c.community.name for c in member_of]
    total_bulletins = Bulletin.objects.filter(user_account=u).count()

    return render(request, 'profile.html', {'uname':uname,
                                            'datejoined':datejoined,
                                            'communities':communities,
                                            'total_bulletins':total_bulletins
                                            })
