from django.conf.urls import include, url
from django.contrib import admin
from eav_app import views
from eav_app.views import *
from rest_framework.routers import DefaultRouter


# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'dynamic.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),

#     url(r'^experiment/$', views.ExperimentList.as_view(),name='experiment-list'),

# 	url(r'^experiment/(?P<pk>\w+)/$', views.ExperimentDetail.as_view(),name='experiment-detail'),

#     url(r'^values/$', views.ValuesList.as_view(),name='values-list'),

# 	url(r'^values/(?P<pk>[0-9]+)/$', views.ValuesDetail.as_view(),name='values-detail'),

#     url(r'^attribute/$', views.AttributeList.as_view(),name='attribute-list'),

# 	url(r'^attribute/(?P<pk>\w+)/$', views.AttributeDetail.as_view(),name='attribute-detail'),

#     url(r'^data/$', views.RawDataList.as_view(),name='data-list'),


# ]

router = DefaultRouter()
router.register(r'researcher', ResearcherViewSet)
router.register(r'data', DataViewSet)
router.register(r'type', DataTypeViewSet)
router.register(r'method', MethodViewSet)

urlpatterns = router.urls