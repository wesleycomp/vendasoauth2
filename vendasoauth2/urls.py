"""vendasoauth2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

#modificado auhorization code
import oauth2_provider.views as oauth2_views # para editar a chamada das opçoes de oauth2 comentadas abaixo
from estoque.views import *
from estoque.urls import router
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings #chama as configuraçõs do arquivo settings
####################### OAUTH 2 modificado para auhorization code ###################################

"""

oauth2_endpoint_views = [
    path('authorize/', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    path('token/', oauth2_views.TokenView.as_view(), name="token"),
    path('revoke-token/', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]


if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        path('applications/', oauth2_views.ApplicationList.as_view(), name="list"),
        path('applications/register/', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        path('applications/<pk>/', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        path('applications/<pk>/delete/', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        path('applications/<pk>/update/', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

#################### OAuth2 Token Management endpoints ###############################
    oauth2_endpoint_views += [
        path('authorized-tokens/', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        path('authorized-tokens/<pk>/delete/', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]
"""



urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/register', registrarUsuarioView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout', views.LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
