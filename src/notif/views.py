from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView, CreateView
from django.http import HttpResponse
from django.contrib import messages
from home.models import Parts
from core.models import User
from .forms import ReplyForm
from django.db.models import Q

from .models import Notification
from django.shortcuts import render, redirect


@login_required(login_url='/login/')
def get_notifications(request):

    template_name = 'notifications.html'
    notif_object = Notification.objects.filter(seller_id=request.user.id).filter(is_valid='True')
    context = {"notifications": notif_object}
    print(context)
    return render(request, template_name, context)


@login_required(login_url='/login/')
def reply_select(request, id):
    print(id)
    template_name = 'reply.html'

    if request.method == 'POST':
        context = {}

        errors = None

        if request.POST.get('accept'):
            print('accept valid')
            form = ReplyForm(request.POST, request.FILES)

            if form.is_valid():
                if request.user.is_authenticated():
                    instance = form.save(commit=False)
                    instance.save()
                    part = Parts.objects.get(id=request.POST.get('part_id'))
                    notif = Notification.objects.get(id=id)
                    part.is_available = 'False'
                    notif.is_valid='False'
                    notif.save()
                    part.save()
                    print('success save valid')
                    messages.success(request, 'Request accepted')
                    return redirect('home')
            if form.errors:
                errors = form.errors
                print(errors)
                print(form.errors)
                print(form)
                context = {"form": form, "errors": errors
                       }

        else:
            notif = Notification.objects.get(id=id)
            notif.is_valid = 'False'
            notif.save()
            messages.success(request, 'Request Declined')
            return redirect('home')


    else:
        notif = Notification.objects.get(id=id)
        parts = Parts.objects.filter(owner=User.objects.get(id=notif.buyer_id)).filter(is_available='True')
        context = {'parts': parts,'notif':notif}

    return render(request, template_name, context)


