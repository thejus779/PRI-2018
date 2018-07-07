from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView, CreateView
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from .models import Image
from .forms import ImageForm
from .forms import PostPartCreateForm
from .models import Parts
from django.shortcuts import render, redirect
from notif.forms import BuyRequest
from core.models import Profile
from notif.models import Notification

@login_required(login_url='/login/')
def create_parts(request):
    form = PostPartCreateForm(request.POST,request.FILES)
    errors = None
    print(form)
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            # custoize and signals
            #  pre save
            instance.owner = request.user
            instance.save()
            # file = form.cleaned_data['image']
            # post save
            return redirect('home')
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors

    template_name = 'post.html'
    context = {"form": form, "errors":errors
               }

    return render(request,template_name,context)


# class PartCreateView(LoginRequiredMixin, CreateView):
#     form_class = PostPartCreateForm
#     login_url = '/login/'
#     template_name = 'post.html'
#     success_url = 'home'
#
#     def form_valid(self, form):
#         print('Form is valid')
#         instance = form.save(commit=False)
#         instance.owner = self.request.user
#
#         return super(PartCreateView, self).form_valid(form)


def showimage(request):
    lastimage = Image.objects.last()

    imagefile = lastimage.imagefile

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    return render(request, 'Blog/images.html', context)


class PartsDetailsView(DetailView):


    # template_name = 'details.html'
    queryset = Parts.objects.all()
    print("")
    # filter(catergory__iexact='SWEET')
    # def get_context_data(self, **kwargs):
    #     print("test is success")


def display_buy_part(request,slug):

    if request.method == 'POST':
        if request.POST.get("login"):
            return redirect('login')

        else:
            form = BuyRequest(request.POST, request.FILES)
            errors = None
            print(form)
            if form.is_valid():
                print("Form action working")
                if request.user.is_authenticated():
                    instance = form.save(commit=False)
                    # custoize and signals
                    #  pre save
                    instance.owner = request.user
                    instance.save()
                    # file = form.cleaned_data['image']
                    # post save
                    print("INSIDE FORM")
                    return redirect('home')
            if form.errors:
                print("ERROR  IS ")
                errors = form.errors
            #
            print(errors)
            template_name = 'details.html'
            queryset = Parts.objects.get(slug__iexact=slug)
            if request.user.is_authenticated():
                profile = Profile.objects.get(user_id=request.user.id)
            else:
                profile = {""}
            context = {"form": form, "errors": errors, "part": queryset
                , "profile": profile}
            # print(context)
            # print(slug)
            return render(request, template_name, context)
    else:
        template_name = 'details.html'
        queryset = Parts.objects.get(slug__iexact=slug)
        if request.user.is_authenticated():
            profile = Profile.objects.get(user_id=request.user.id)
        else:
            profile = {""}
        context = {"part": queryset
            , "profile": profile}
        print(context)
        print(slug)
        return render(request, template_name, context)
