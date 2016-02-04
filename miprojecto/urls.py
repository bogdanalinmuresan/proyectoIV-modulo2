from django.conf.urls import url, patterns, include
#from app.api import UsuarioResource

#usuario_resource=UsuarioResource()

urlpatterns = patterns('',
    #url(r'', include('app.urls')), # ADD THIS NEW TUPLE!
    url(r'^app/', include('app.urls')), # ADD THIS NEW TUPLE!
    #url(r'^api/',include(usuario_resource.urls)),
)
