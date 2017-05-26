"""firstpick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from fpickapp import views
from django.conf import settings
from django.conf.urls.static import static

from fpickcart import views as cartviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.home,name="home"),

    url(r'^laptopcatalog/$',views.laptop_catalog,name="laptopcatalog"),
    url(r'^desktopcatalog/$',views.desktop_catalog,name="desktopcatalog"),

    url(r'^add/to/cart/(?P<modeltype>\w+)/(?P<itemid>\d+)/$', cartviews.add_to_cart, name='addtocart'),

    url(r'^computer/detail/(?P<pk>\d+)/$', views.computer_detail, name='computerdetail'),

    url(r'^cart/view/$', cartviews.view_cart, name='viewcart'),  

    url(r'^create/user/$',views.create_user,name="createuser"),
    url(r'^login/$',views.login_page,name="logingin"),
    url(r'^logout/$',views.logout_page,name="logingout"),
    url(r'^comp/peripherials/(?P<topic>\w+)/$',views.computer_peripherials,name='computerperipherials'),
    url(r'^comp/peripherials/filter/brand/(?P<bname>\w+)/$',views.computer_by_brand,name='computerbybrand'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
