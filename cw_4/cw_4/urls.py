from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # По условию GET / -> редирект на /threads
    path('', RedirectView.as_view(pattern_name='thread_list', permanent=False)),
    path('', include('post.urls')),  # подключаем urls из приложения `post`
]

# Подключение статики (для загрузки и отображения файлов)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
