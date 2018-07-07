from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView, CreateView
from django.http import HttpResponse

from home.models import Parts
from core.models import User
from django.db.models import Q

from .models import Notification
from django.shortcuts import render, redirect


@login_required(login_url='/login/')
def get_notifications(request):

    template_name = 'notifications.html'
    notif_object = Notification.objects.filter(seller_id__icontains=request.user.id)
    context = {"notifications": notif_object}
    print(context)
    return render(request, template_name, context)


@login_required(login_url='/login/')
def reply_select(request, id):
    print(id)
    template_name = 'reply.html'

    parts = Parts.objects.filter(owner=User.objects.get(id=id))
    context = {'parts': parts}
    return render(request, template_name, context)