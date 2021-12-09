from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.product.views import category_product, product_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('home/', include('apps.home.urls')),
    path('', include('apps.home.urls')),
    path('product/', include('apps.product.urls')),
    path('category/<int:id>/<slug:slug>', category_product, name='category_product'),
    path('category/<int:id>/<slug:slug>', product_detail  , name='category_product'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)