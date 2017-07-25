from django.test import TestCase

# Create your tests here.
def blog_search(request):
    search_for = request.GET['search_for']

    if search_for:
        result = []
        blog_list = get_list_or_404(Blog)
        category_list = get_list_or_404(Category)
        for blog in blog_list:
            if re.findall(search_for,blog.title):
                result.append(blog)
        tag_list = Tag.objects.all().order_by('name')
        ctx = {
            'blog_list':result,
            'categoty_list':category_list
            'tag_list':tag_list
        }
        return render(request,'blogapp/search.html',ctx)
    else:
        return redirect('blog:index')
