"""prihome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import serve
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from core.forms import CustomAuthenticationForm
from home.views import (
    # PartCreateView,
    create_parts,
    display_buy_part,
    PartsDetailsView,

)
from core.views import (
    signup,
    update_profile,
    login_view,
    user_parts,
    user_profile,
    logout_view,
    delte_user_part,
    # display_profile,
    # DisplayProfile,
)
from notif.views import (
    get_notifications,
    reply_select,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$',signup, name='signup'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html',
    #     'authentication_form': CustomAuthenticationForm}, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^login/$', LoginView.as_view(template_name='login.html'),name='login'),
    # url(r'^signup/$', TemplateView.as_view(template_name='signup.html'),name='signup'),
    # url(r'^login/$', login_view, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^view3/$', TemplateView.as_view(template_name='view3.html')),
    # url(r'^profile/$',update_profile, name='profile'),
    url(r'^$', TemplateView.as_view(template_name='index.html'),name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^post/$', create_parts),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^details/$', TemplateView.as_view(template_name='details.html')),
    url(r'^posted/$', user_parts,name='posted'),
    url(r'^edit/$', TemplateView.as_view(template_name='editProfile.html')),
    url(r'^profile/$', user_profile),
    url(r'^notifications/$', get_notifications),
    url(r'^reply/(?P<id>[\d]+)$', reply_select),
    url(r'^imgsearch/$', TemplateView.as_view(template_name='searchByImage.html')),
    url(r'^part/(?P<slug>[\w-]+)/$', display_buy_part),
    url(r'^delete/(?P<id>[\d]+)/$', delte_user_part),
    url(r'^logout/$', logout_view),

    # url(r'^media/(?P<path>.*)$', serve, {
        # 'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

