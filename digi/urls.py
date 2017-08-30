from django.conf.urls import url
from . import views
urlpatterns = [
#url(r'^$', views.index, name='page1'),
url(r'^index$',views.index,name='index'),
url(r'^page1$',views.page1,name='page1'),
url(r'^login_page_wt_project/page2$',views.page2,name='page2'),
#url(r'^page3$',views.page3,name='page3'),
#url(r'^page4$',views.page4,name='page4'),
#url(r'^page23$',views.page23,name='page23'),
#url(r'^page24$',views.page24,name='page24'),
#url(r'^page5$',views.page5,name='page5'),
url(r'^login_page_wt_project/teacher_or_student',views.page1,name="teacher_or_student"),
url(r'^register_prof',views.UserFormView.as_view(),name='register_prof')
#url(r'^login$',views.login,name='login')
]