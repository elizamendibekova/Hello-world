from django.shortcuts import reverse
from django.views import generic
from django.utils import timezone
from .models import Post, UserPost
from django.contrib.auth.forms import UserCreationForm

class IndexView(generic.ListView):
    template_name = 'BlogApp/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.all().order_by('pub_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'BlogApp/detail.html'
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class CreatePostView(generic.edit.CreateView):
    fields = ['title', 'body']
    template_name = 'BlogApp/create_post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

    def get_success_url(self):
        return reverse('BlogApp:index')

class UpdateQuestionView(generic.edit.UpdateView):
    template_name = "BlogApp/update_question.html"
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('BlogApp:index')

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class DeleteQuestionView(generic.edit.DeleteView):
    template_name = "BlogApp/confirm_delete_post.html"

    def get_success_url(self):
        return reverse('BlogApp:index')

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

class RegisterView(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = "/войти/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)

class LoginView(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "registration/login.html"

    def form_valid(self, form):
        form.save()
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)