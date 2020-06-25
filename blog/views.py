from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category
from blog.forms import ContactUsForm, PostForm

from django.views import View
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

class CategoryList(View):

    def get(self, request, id=None):
        posts = Post.objects.filter(status='P')
        if id:
            cat = Category.objects.get(id=id)
            posts = Post.objects.filter(category = cat)
            return render(request, 'blog/stories.html',context={'posts':posts, 'categories':Category.objects.all()})
        categories = Category.objects.all()
        context = {'posts':posts, 'categories':categories}
        return render(request, 'blog/stories.html',context )


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status='P')
    context_object_name = 'posts'
    template_name = 'blog/stories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class PostDetailView(LoginRequiredMixin,generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status='P')
    template_name = 'blog/blog-post.html'
    context_object_name = 'post'
    login_url = reverse_lazy('login')
    

def contact_us_form_view(request):
    if request.method == 'GET':
        form = ContactUsForm()
        return render(request, 'blog/contact-us.html', context={'form':form})
        
    else:
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            return render(request, 'blog/thankyou.html')
        else:
            print(form.errors)
            return render(request, 'blog/contact-us.html', context={'form':form})
            
class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    permission_required = 'blog.add_post'
    login_url = reverse_lazy('login')
    model = Post
    form_class = PostForm
    template_name = 'blog/post.html'

    def form_valid(self, form):
        print(form.__dict__)
        form.instance.author = self.request.user
        return super().form_valid(form)
 

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    permission_required = 'blog.change_post'
    login_url = reverse_lazy('login')
    model = Post
    form_class = PostForm
    template_name = 'blog/update.html'

    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)

    def test_func(self, *args, **kwargs):
        # print(self.request.GET)
        # print(print(self.kwargs.get('slug')))

        post = Post.objects.get(slug=self.kwargs.get('slug'))
        if post.author == self.request.user:
            return True
        else:
            return False
        
        


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'blog.change_post'
    login_url = reverse_lazy('login')
    model = Post
    form_class = PostForm
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('home')


# def post_update_form_view(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == 'GET':
#         form = PostForm(instance=post)
#         return render(request, 'blog/post.html', context={'form':form})
#     else:
#         print(request.POST)
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return render(request, 'blog/thankyou.html')
#         else:
#             print(form.errors)
#             return render(request, 'blog/post.html', context={'form':form})

# def post_delete_form_view(request, id):
#     post = Post.objects.get(id=id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('home')
#     return render(request, 'blog/delete.html' , context={'post':post})