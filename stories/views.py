from django.shortcuts import render, get_object_or_404, redirect
from . models import Stories
from django.contrib.auth.decorators import login_required, permission_required
from .forms import Addstory
from django.utils import timezone
import uuid
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def home(request):
	
	stories = Stories.objects.filter(parent__isnull=True).order_by('pub_date')
	paginator = Paginator(stories, 9)
	page = request.GET.get('page')
	story = paginator.get_page(page)

	return render(request, 'stories/home.html', {'stories':stories, 'story':story})


@login_required
def story(request, story_id):
	story_detail = get_object_or_404(Stories, pk=story_id)
	temp_instance = story_detail.body
	instance = temp_instance.split("\r\n\r\n")
	paginator = Paginator(instance, 8)
	page = request.GET.get('page')
	story = paginator.get_page(page)
	child_stories = Stories.objects.filter(parent__exact=story_id)
	if request.method == 'GET':
		return render(request, 'stories/story.html', {'story_detail':story_detail, 'story':story, 'child_stories':child_stories})

@login_required
@permission_required('stories.add_stories', login_url='home')
def addstory(request, story_id=None):
	story_item = Stories()
	if request.method == 'POST':
		form = Addstory(request.POST, request.FILES)
		if form.is_valid():
			story_item.title = request.POST['title']
			story_item.body = request.POST['body']
			story_item.pub_date = timezone.datetime.now()
			story_item.image = form.cleaned_data['image']
			story_item.author = request.user
			parent = request.POST['parent']
			if parent:
				parentobject = Stories.objects.get(id=parent)
				story_item.parent = parentobject
				story_item.family_uuid = parentobject.family_uuid
			else:
				story_item.parent = None
				story_item.family_uuid = uuid.uuid4()
			story_item.save()
			messages.success(request, 'Story added successfully')
			return redirect('story', story_item.id)
	else:
		data = {'parent':story_id}
		form = Addstory(data)
		return render(request, 'stories/addstory.html', {'form':form})

@login_required
@permission_required('stories.add_stories', login_url='home')
def editstory(request, story_id):

	storyy = Stories.objects.get(pk=story_id)
	if storyy.author == request.user:
		if request.method == 'POST':
			form = Addstory(request.POST, request.FILES, instance=storyy)
			if form.is_valid():
				parent = request.POST['parent']
				if parent:
					parentobject = Stories.objects.get(id=parent)
					print(parentobject.family_uuid)
					storyy.family_uuid = parentobject.family_uuid
				else:
					storyy.family_uuid = uuid.uuid4()

				storyy.save()
				messages.success(request, 'Story edited successfully')
				return redirect('story', story_id)
			
		else:
			form = Addstory(instance=storyy)
			return render(request, 'stories/editstory.html', {'form':form})
	else:
		messages.error(request, 'Only the author can edit this story')
	
		return redirect('story', story_id)
	
	