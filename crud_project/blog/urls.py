from django.conf.urls import url
from. import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    url(r'^$',views.post_main, name="post_main"),
    
    url(r'^login$',auth_views.LoginView.as_view(), name="login"),   
    url(r'^logout$',auth_views.LogoutView.as_view(), name="logout"),  
    url(r'^post_login_done$',views.post_login_done, name="post_login_done"),
    url(r'^signup$', views.CreateUserView.as_view(), name = 'signup'),  
    url(r'^signup/done$', views.RegisteredView.as_view(), name = 'create_user_done'),
    url(r'^permission_denied$', views.permission_denied, name = 'permission_denied'),  
    
    

    url(r'^index/$',views.post_index, name="post_index"),

    url(r'^(?P<post_id>\d+)/$',views.post_detail, name="post_detail"),

    url(r'^new/$',views.post_new, name="post_new"),

    url(r'^(?P<post_id>\d+)/edit/$',views.post_edit, name="post_edit"),

    url(r'^(?P<post_id>\d+)/delete$',views.post_delete, name="post_delete"),


    #댓글 써줄거
    url(r'^(?P<post_id>\d+)/Comment/$',views.comment_new, name="comment_new"),
    url(r'^(?P<post_id>\d+)/Comment/(?P<comment_id>\d+)/delete/$',views.comment_delete, name="comment_delete"),
]