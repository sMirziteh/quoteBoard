from django.conf.urls import url
from ..quote_app import views

urlpatterns = [
    url(r'^quotes$', views.quoteHome),
    url(r'^addlike$', views.addlike),
    url(r'^user/(?P<poster_id>\d+)$', views.showUserPage),
    url(r'^myaccount/(?P<user_id>\d+)$', views.myAccount),
    url(r'^editUser$', views.editUser),
    url(r'^createQuote$', views.createQuote),
    url(r'^deleteQuote/(?P<quote_id>\d+)$', views.deleteQuote),

]