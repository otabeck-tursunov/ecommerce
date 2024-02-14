from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="Ecommerce REST API for Web",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="otabecktursunov@gmail.com"),
        license=openapi.License(name="Codial Team"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('order/', include('orderApp.urls')),
    path('user/', include('userApp.urls')),

    # SimpleJWT Token
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

    # Swagger docs
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Media
