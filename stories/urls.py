from django.urls import path

from . import views

urlpatterns = [

	path('<int:story_id>/', views.story, name='story'),
	path('', views.home, name='home'),
	path('addstory/', views.addstory, name='addstory'),
	path('addstory/<int:story_id>/', views.addstory, name='addstory'),
	path('editstory/<int:story_id>/', views.editstory, name='editstory'),
]