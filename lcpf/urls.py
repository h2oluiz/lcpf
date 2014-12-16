from django.conf.urls import url, include
from rest_framework import routers
from consulta import views


router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'Localizar_CPF', views.Localizar_CPFViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^localizar-cpf/(?P<pk>[0-9]+)$', views.Localizar_CPF_detail),
    ]
