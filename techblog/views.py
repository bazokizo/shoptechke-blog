from django.shortcuts import render
from techblog.models import Post, Category
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.db.models import Count
from django.db.models import Q

# Create your views here.
def index(request):
	#post filters to be displayed
	all_posts = Post.objects.all()
	recent_posts = Post.objects.all()[:3]
	all_categories = Category.objects.all().annotate(posts_count=Count('post'))

	page = request.GET.get('page', 1)
	
	paginator = Paginator(all_posts, 2)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context={
		'all_posts': all_posts,
		'recent_posts': recent_posts,
		'posts': posts,
		'all_categories': all_categories,
		
		
	}
	return render(request, 'index.html', context=context)

class PostDetailView(generic.DetailView):
	model=Post

class CategoryDetailView(generic.DetailView):
	model = Category

class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
    	query = self.request.GET.get('q')
    	object_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(category__name__icontains=query) )
    	return object_list