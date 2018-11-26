from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.utils.translation import gettext as _

from blog.models import Post, Tag
from base.forms import CustomUserCreationForm, CustomUserChangeForm


def home(request):
    items = Post.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    
    return render(request, 'base/home.html',{'items':items, 'title':'Home'})

def about(request):
    return render(request, 'base/about.html', {'title':_('About')})

def tag(request, slug=None):
    _tag = get_object_or_404(Tag, slug=slug)
    items = Post.objects.filter(tags__slug=slug)
    title = 'Items tagged with "%s"' % _tag
    return render(request, 'base/tag.html', {'items':items,
                                             'tag':_tag,
                                             'title':title})

class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile(request):
    return render(request, 'base/profile.html', {'title':'Profile'})

class UserChange(LoginRequiredMixin, generic.UpdateView):
    modele = User
    form_class = CustomUserChangeForm
    template_name = 'registration/user_change.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return self.request.user





























