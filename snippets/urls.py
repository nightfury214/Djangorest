from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework import renderers, permissions
from snippets.views import api_root, SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API documentation usin swagger 2.0",
        terms_of_service="https://www.example.com/terms",
        contact=openapi.Contact(email="contract@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
urlpatterns = [
    path("", views.api_root),

    # re_path(r'^snippets/$', scheme_view.with_ui('snippets', cache_timeout=0), snippet_list, name='snippet-list'),
    # re_path(r'^snippets/<int:pk>/$', scheme_view.with_ui('snippets', cache_timeout=0), snippet_detail, name='snippet-detail'),
    # re_path(r'^snippets/<int:pk>/highlight/$',
    #     scheme_view.with_ui('snippets', cache_timeout=0), 
    #     snippet_highlight,
    #     name="snippet-highlight",
    #     ),
    # re_path(r'^users/$',scheme_view.with_ui('users', cache_timeout=0), user_list, name='user-list'),
    # re_path(r'^users/<int:pk>/$', scheme_view.with_ui('users', cache_timeout=0), user_detail, name='user-detail'),

    # path("snippets/", snippet_list, name='snippet-list'),
    # path("snippets/<int:pk>/", snippet_detail, name='snippet-detail'),
    # path("snippets/<int:pk>/highlight/", 
    #     snippet_highlight,
    #     name="snippet-highlight",
    #     ),
    # path("users/",user_list, name='user-list'),
    # path("users/<int:pk>/", user_detail, name='user-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]