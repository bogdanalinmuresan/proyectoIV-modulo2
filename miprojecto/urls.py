from django.conf.urls import url
from django.conf.urls import patterns, include


#from .views import RegistrarUsuario, RedirigirUsuario

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')), # ADD THIS NEW TUPLE!
)
