from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment

# Create your views here.
def frontpage(request):
    posts = Post.objects.all()

    return render(request , 'post/frontpage.html', {
        'posts' : posts
    })

def post_detail(request, slug):
    post = get_object_or_404(Post , slug = slug)
    if request.method == "POST":
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')

        if name and comment :
            comment = Comment.objects.create(
                post = post,
                name = name,
                comment = comment
            )

            return redirect('post_detail', slug = post.slug)
    return render (request, 'post/details.html', {
        'post':post
    })

def category_detail (request, pk):
    category = get_object_or_404(category, pk=pk)
    return render(request, 'post/category.html', {
        'category' : category
    })

