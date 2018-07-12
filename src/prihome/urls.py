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
# from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from core.forms import CustomAuthenticationForm
from home.views import (
    # PartCreateView,
    create_parts,
    display_buy_part,
    PartsDetailsView,
    get_all_products,
    update_part,
    filter_section,
    search,
    search_results,
    no_search_section,
    register_post,
    create_contact,



)
from core.views import (
    signup,
    update_profile,
    user_parts,
    user_profile,
    logout_view,
    delte_user_part,
    MyLoginView,
    activate,
    change_password,

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
    # url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^login/$', MyLoginView.as_view(template_name='login.html'), name='login'),
    url(r'^view3/$', TemplateView.as_view(template_name='activated.html')),
    url(r'^update/(?P<slug>[\w-]+)/$', update_part),
    url(r'^$', get_all_products, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^post/$', create_parts,name='post'),
    url(r'^contact/$', create_contact,name='contact'),
    url(r'^details/$', TemplateView.as_view(template_name='details.html')),
    url(r'^posted/$', user_parts,name='posted'),
    url(r'^edit/$', update_profile),
    url(r'^profile/$', user_profile,name='profile'),
    url(r'^notifications/$', get_notifications),
    url(r'^reply/(?P<id>[\d]+)$', reply_select),
    url(r'^imgsearch/$', TemplateView.as_view(template_name='searchByImage.html')),
    url(r'^part/(?P<slug>[\w-]+)/$', display_buy_part),
    url(r'^delete/(?P<id>[\d]+)/$', delte_user_part),
    url(r'^logout/$', logout_view),
    url(r'^/$', get_all_products),
    url(r'^filter/$',filter_section, name='filter_section'),
    url(r'^search/$',search, name='search'),
    url(r'^search_results/$', search_results, name='search_results'),
    url(r'^no_search_result/$', no_search_section, name='no_search_result'),
    url(r'^register_post/$',register_post, name='register_post'),
    url(r'^password/$',change_password, name='change_password'),
    url(r'^activated/$',TemplateView.as_view(template_name= 'activated.html'), name='activated'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    # url(r'^media/(?P<path>.*)$', serve, {
        # 'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

