from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login_page, name='login'),
	url(r'^autentica/$', views.entrar),
	url(r'^registra/$', views.register),
	url(r'^logout/$', views.make_logout),
	url(r'^deletaconta/$', views.deletaconta),
	url(r'^profile/(?P<username>[\w.@+-]+)$', views.profile),
	url(r'^edit_profile/$', views.edit_profile),
	url(r'^search_users/$', views.search_users, name='search_users'),

	url(r'^postProfile/$', views.create_profile),
	url(r'^deleteProfile/$', views.delete_profile),

	#Paginas de inbox
    url(r'^inbox/$', views.my_contacts, name='my_contacts'),
    url(r'^inbox/message/(?P<pkreceptor>[0-9]+)/$', views.sala, name='sala'),
    url(r'^inbox/message/(?P<pkreceptor>[0-9]+)/send/$', views.send_message, name='send_message'),
    url(r'^deleta_conversa/$', views.deleta_conversa, name='deleta_conversa'),
]