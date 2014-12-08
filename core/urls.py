from django.conf.urls import patterns, include, url
from api.v1.core.views import AuthUser
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', HomePageView.as_view()),
    url(r'^api/', include('api.url')),
    url(r'^auth-user/?$', AuthUser.as_view()),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^import-users/', 'api.v1.core.views.import_users_from_ldap'),
    url(r'^test-ldap/', 'api.v1.core.views.test_connection'),
)