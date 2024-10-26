from django.urls import path
from myapp import views
urlpatterns = [
        path('insert/',views.insert,name='insert_data'),
        path('update/',views.update,name='update_data'),
        path('',views.main,name='main'),
        # path('index',views.index,name='index'),
        # path('show',views.show,name='show')
        
]