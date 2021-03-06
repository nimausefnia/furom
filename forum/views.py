from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import ThreadForm,ReplyForm
from .models import Thread,Reply
from django.contrib.auth.decorators import login_required

def index(request):
    form = ThreadForm()

    threads = Thread.objects.all()

    context = {'form' : form, 'threads' : threads}
    return render(request, 'forum/index.html', context)

def thread(request, thread_id):
      thread = Thread.objects.get(pk=thread_id)
      if request.method=='POST':
            form=ReplyForm(request.POST)
           
            reply= form.save(commit=False)
            reply.thread=thread
            reply.user=request.user
            reply.save()

            return redirect('thread',thread_id=thread_id)
            


      else:
         form=ReplyForm()

     
    
      payam=Reply.objects.all().order_by('date_created')

      context = {'thread' : thread,'form':form,'payam':payam}
      return render(request, 'forum/thread.html', context)

@require_POST
def new_thread(request):
    form = ThreadForm(request.POST)
    thread = form.save()

    return redirect('thread')