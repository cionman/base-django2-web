from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path, include
from django.conf import settings

urlpatterns = [
    path('', lambda r: render(r, 'intro.html')),
    path('sl-admin/', admin.site.urls),
]

# Debug-toolbar url 설정
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
