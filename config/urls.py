from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('login/', LoginView.as_view(template_name='pages/login.html')),
	path('logout/', LogoutView.as_view(next_page='/')),
    path('', include('baybal.urls')),
]
