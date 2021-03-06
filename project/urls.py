from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path, include
from django.conf import settings

urlpatterns = [
    path('', lambda r: render(r, 'intro.html')),
    path('sl-admin/', admin.site.urls),
    path('accounts', include('accounts.urls')),
    path('board', include(('board.urls', 'board'), namespace='board')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug-toolbar url 설정
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
