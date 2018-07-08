from django.contrib.auth import login, authenticate
from django.contrib.auth import (login as auth_login,  authenticate)
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from home.models import Parts
from .models import Profile
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView,ListView,DetailView, CreateView

from django.shortcuts import render, redirect
from django.conf import settings
from django.db import transaction
from .utils import unique_slug_generator
from .forms import LoginForm, SignUpForm, UpdateUpForm,User
from .models import Profile
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        print("Outside form is valid")
        print(form)
        print("form printerd")
        if form.is_valid():
            print("Inside Valid")
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)

            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.fullname = form.cleaned_data.get('fullname')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.postalcode = form.cleaned_data.get('postalcode')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.mobilenumber = form.cleaned_data.get('mobilenumber')
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                return redirect('home')# Redirect to a success page.
    else:
        form = SignUpForm()
    # return render_to_response('signup.html', {'form': form },  RequestContext(request))
    return render(request, 'signup.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST or None)
#         print("asdasd lo login")

#         if form.is_valid():
#             instance = form.save(commit=False)
#             print("asdasd")
#             instance.refresh_from_db()  # load the profile instance created by the signal
#             instance.profile.fullname = form.cleaned_data.get('fullname')
#             form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             if user:
# 	            login(request, user)
# 	            return redirect('home')
#             else:
#             	print('User authentication problem')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form-signup': form})

def display_profile(request):
    template_name = 'profile.html'
    # queryset = Profile.objects.filter(user_id=request.user.id)  # filter(catergory__iexact='SWEET')
    return render(request, template_name, {})


# class DisplayProfile(DetailView):
#
#     template_name = 'profile.html'
#
#     def get_queryset(self):
#     #     print(self.kwargs)
#     #     queryset = Profile.objects.filter(id=self.request.user.id)  # filter(catergory__iexact='SWEET')
#     #     return queryset


@login_required
# @transaction.atomic
def update_profile(request):

    if request.method == 'POST':

        user_form = UpdateUpForm(request.POST, instance=request.user)
        user = User.objects.get(id=request.user.id)
        user_profile = Profile.objects.get(user=request.user)
        print('user form is')
        print(user_form)
        if user_form.is_valid():
            user_profile.fullname = user_form.cleaned_data.get('fullname')
            user_profile.postalcode = user_form.cleaned_data.get('postalcode')
            user_profile.city = user_form.cleaned_data.get('city')
            user_profile.address = user_form.cleaned_data.get('address')
            user_profile.country = user_form.cleaned_data.get('country')
            user_profile.mobilenumber = user_form.cleaned_data.get('mobilenumber')
            user.email = user_form.cleaned_data.get('email')
            user.username = user_form.cleaned_data.get('username')
            print(user.username)
            print(user_form.cleaned_data.get('username'))
            if User.objects.filter(username=user_form.cleaned_data.get('username')).exists():
                messages.error("Username already exists")
                # raise forms.ValidationError(u'Username "%s" is not available.' % newusername)
            else:
                if User.objects.filter(username=user_form.cleaned_data.get('email')).exists():
                    messages.error("Username already exists")
                else:
                    user.username = user_form.cleaned_data.get('username')
                    user.email = user_form.cleaned_data.get('email')
                    user.save()
                    user_profile.save()
                    messages.success(request, 'Your profile was successfully updated!')

            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'editProfile.html', {'form':user_form})


    else:
        template_name = 'editProfile.html'
        user_profile = Profile.objects.get(user=request.user)
        context = {'user': user_profile}
        print(context)
        return render(request, template_name, context)

class MyLoginView(LoginView):
    success_url = 'index.html'
    form_class = LoginForm()
    template_name = 'login.html'





def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('home')# Redirect to a success page.
    return render_to_response('login.html', {'login_form': form },  RequestContext(request))


def user_parts(request):
    # if request.method == 'POST':
        # if request.POST.get("delete"):
        #     queryset = Parts.objects.get(id=).delete()
        #     return redirect('home')

    # else:
    template_name = 'userposts.html'
    parts = Parts.objects.filter(owner=request.user)
    context = {'parts': parts}
    print(context)
    return render(request, template_name, context)

def user_profile(request):

    template_name = 'profile.html'

    user_profile = Profile.objects.get(user=request.user)
    context = {'user': user_profile}
    print(context)

    return render(request, template_name, context)


def logout_view(request):

    logout(request)
    print('logout successfull')
    return redirect('login')


def delte_user_part(request,id):

    template_name = 'userposts.html'
    part = Parts.objects.get(id=id)
    print("Insde delete")
    print(part)

    try:
        if request.method == 'POST':
            part.delete()
            messages.success(request, "Successfully deleted")

    except Exception as e:
        messages.warning(request, "Exception in deleted")

    parts = Parts.objects.filter(owner=request.user)
    context = {'parts': parts}
    print(context)
    return redirect('posted')