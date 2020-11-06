from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django_pydenticon.views import image as pydenticon_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image'),
    # re_path('', TemplateView.as_view(template_name='root.html'), name='root'),  # 모든 경우에 매칭되는 URL
    path('', login_required(TemplateView.as_view(template_name='root.html')), name='root'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
