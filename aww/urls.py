from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^upload/$',views.new_project,name='add_project'),
    url(r'^review/(?P<project_id>\d+)', views.review_project, name='review'),
    url(r'^searched/', views.search_projects, name='search'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^profile/update/', views.update_profile, name='update_profile'),
    url(r'^project_details/(?P<id>\d+)', views.project_details, name='projectdetails'),

    # API VIEWS
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    # url(r'^api/project/$', views.ProjectList.as_view()),
    # url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),






]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
