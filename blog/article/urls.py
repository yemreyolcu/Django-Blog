from django.urls import path
from . import views
app_name = "article"
urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('post/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
    #path('delete/<int:id>',views.detail,name="delete"),
    # path('create/',views.index,name="create"),

]