from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from post.models import Stream, Post, Tag, Likes,Follow
from post.forms import NewPostForm

from comment.models import Comment
from comment.forms import CommentForm


from django.contrib.auth.decorators import login_required

from django.urls import reverse
from authy.models import Profile



# Create your views here.
@login_required
def index(request):
	user = request.user
	posts = Stream.objects.filter(user=user)
	profile = Profile.objects.get(user=user)
	MLP = Post.objects.all().order_by('-likes')[:5]



	group_ids = []

	for post in posts:
		group_ids.append(post.post_id)
		
	post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
	post_count = Post.objects.filter(id__in=group_ids).count()

	template = loader.get_template('index.html')

	context = {
	'post_items': post_items,
	'profile':profile,
	'post_count':post_count,
	"MLP":MLP

	}

	return HttpResponse(template.render(context, request))

def PostDetails(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	user = request.user
	profile = Profile.objects.get(user=user)
	MLP = Post.objects.all().order_by('-likes')[:5]
	favorited = False

	posts_count = Post.objects.filter(user=user).count()
	following_count = Follow.objects.filter(follower=user).count()
	followers_count = Follow.objects.filter(following=user).count()
	follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

	#comment
	comments = Comment.objects.filter(post=post).order_by('date')
	
	if request.user.is_authenticated:
		profile = Profile.objects.get(user=user)
		#For the color of the favorite button

		if profile.favorites.filter(id=post_id).exists():
			favorited = True

	#Comments Form
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user = user
			comment.save()
			return HttpResponseRedirect(reverse('postdetails', args=[post_id]))
	else:
		form = CommentForm()


	template = loader.get_template('post_detail.html')

	context = {
		'post':post,
		'favorited':favorited,
		'profile':profile,
		'form':form,
		'comments':comments,
		'posts_count':posts_count,
		'following_count':following_count,
		'followers_count':followers_count,
		'follow_status':follow_status,
		"MLP":MLP

	}

	return HttpResponse(template.render(context, request))


@login_required
def NewPost(request):
	user = request.user.id
	tags_objs = []
	MLP = Post.objects.all().order_by('-likes')[:3]

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			picture = form.cleaned_data.get('image')
			caption = form.cleaned_data.get('caption')
			tags_form = form.cleaned_data.get('tags')
			title1 = form.cleaned_data.get('title')

			tags_list = list(tags_form.split(','))

			for tag in tags_list:
				t, created = Tag.objects.get_or_create(title=tag)
				tags_objs.append(t)

			p, created = Post.objects.get_or_create(picture=picture, caption=caption,title=title1, user_id=user)
			p.tags.set(tags_objs)
			p.save()
			return redirect('index')
	else:
		form = NewPostForm()

	context = {
		'form':form,
		"MLP":MLP
	}

	return render(request, 'create-post.html', context)
def tags(request, tag_slug):
	tag = get_object_or_404(Tag, slug=tag_slug)
	posts = Post.objects.filter(tags=tag).order_by('-posted')

	template = loader.get_template('tag.html')

	context = {
		'posts':posts,
		'tag':tag,
	}

	return HttpResponse(template.render(context, request))



@login_required
def like(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	current_likes = post.likes
	liked = Likes.objects.filter(user=user, post=post).count()

	if not liked:
		like = Likes.objects.create(user=user, post=post)
		#like.save()
		current_likes = current_likes + 1

	else:
		Likes.objects.filter(user=user, post=post).delete()
		current_likes = current_likes - 1

	post.likes = current_likes
	post.save()

	return HttpResponseRedirect(reverse('postdetails', args=[post_id]))

@login_required
def favorite(request, post_id):
	user = request.user
	post = Post.objects.get(id=post_id)
	profile = Profile.objects.get(user=user)

	if profile.favorites.filter(id=post_id).exists():
		profile.favorites.remove(post)

	else:
		profile.favorites.add(post)

	return HttpResponseRedirect(reverse('postdetails', args=[post_id]))

@login_required
def PostDelet(request,post_id):
	user = request.user
	obj = get_object_or_404(Post, id = post_id) 
	obj.delete() 
	return redirect('index')


	return HttpResponseRedirect(reverse('postdelet', args=[post_id]))



def Allusers(request):
	profile = Profile.objects.all().order_by('-user') 
	user = request.user
	MLP = Post.objects.all().order_by('-likes')[:3]



	context = {
	"profile":profile,
	"MLP":MLP
	}

	return render(request,'allusers.html',context)


def MLP(request):
	MlP = Post.objects.all().order_by('-likes')[:3]

