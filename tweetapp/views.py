from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from tweetapp.forms import AddTweetForm
from tweetapp.forms import AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        
        message = request.POST["message"]
        models.Tweet.objects.create(username=request.user,message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')
    

@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweetapp:listtweet')
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



"""
def AddTweetbyForm(request):
    if request.POST:
        form = AddTweetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(username=username, message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error in form!")
            return render(request,'tweetapp/addtweetbyform.html', context={"form":form})
    else:
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetbyform.html', context={"form":form})
    

def addtweetbymodelform(request):
    if request.POST:
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(username=username, message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("error in form!")
            return render(request,'tweetapp/addtweetbymodelform.html', context={"form":form})
    else:
        form = AddTweetModelForm()
        return render(request,'tweetapp/addtweetbymodelform.html', context={"form":form})
    
"""