from django.shortcuts import render, get_object_or_404
from .models import Entry, Comment
from django.shortcuts import HttpResponseRedirect

def index(request):
    entries = Entry.objects.all()
    return render(request, 'index.html', {'entries': entries})

def entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, pk = entry_id)
    comments = entry.comment_set.all()

    if request.method == 'POST':
        body = request.POST.get('body')

        if body:
            Comment.objects.create(entry = entry, body = body)
        return HttpResponseRedirect(request.path)

    return render(request, 'entries/entry_detail.html', {'entry': entry, 'comments': comments})