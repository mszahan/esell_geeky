
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from esell.forms import LoginForm
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='homeview'), #replace it with real home, present home will be shipped to esell/
    path('', include("esell.urls")),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='esell/login.html', 
    authentication_form=LoginForm), name='login'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)