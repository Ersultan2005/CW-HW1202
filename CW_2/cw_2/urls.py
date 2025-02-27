from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('post.urls')),
    #
    path('', RedirectView.as_view(url='/posts/', permanent=False)),
]
