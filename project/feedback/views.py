from django.shortcuts import render, get_object_or_404

from feedback.models import Feedback
from feedback.forms import FeedbackForm


# Create your views here.
def feedback(request):
    items = Feedback.objects.all()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html',{'items':items,
                                                     'form':form,
                                                     'title':'Feedback',})

def feedback_item(request, slug=None):
    _item = get_object_or_404(Feedback, slug=slug)
    return render(request, 'feedback/feedback_item.html',{'title':_item})