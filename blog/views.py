from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import CreateUser,SigninUser,CreatePost,EditUser
from .models import Posts

 
# Create your views here.

def home(request):
    post = Posts.objects.all()
    context = {"posts": post}

    return render(request,"blog/home.html",context)


def signin(request):
    if request.method == "POST":
        form = SigninUser(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            p1 = form.cleaned_data["pass1"]
            u = authenticate(username=un,password=p1)

            if u is not None:
                login(request,u)
                return redirect("home")
            else:
                return redirect("signin")
    else:
        form = SigninUser(request.POST)
    
    context = {"form": form}
    return render(request,"blog/signin.html",context)

def register(request):
    if request.method == "POST":

        form = CreateUser(request.POST)
        if form.is_valid():
            un = form.cleaned_data["username"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            e = form.cleaned_data["email"]
            p1 = form.cleaned_data["pass1"]
            p2 = form.cleaned_data["pass2"]
            u = User.objects.create_user(un,e,p1)
            u.first_name = fname
            u.last_name = lname
            u.save()

            return redirect("signin")
    else:
        form = CreateUser(request.POST)
    
    context = {"form": form}
    return render(request,"blog/register.html",context)

def create(request):
    
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            user = request.user
            t = form.cleaned_data["title"]
            c = form.cleaned_data["content"]
            u = Posts(author = user,title=t,content=c)
            u.save()
            return redirect("home")
    else:
        form = CreatePost(request.POST)
    context = {"form" : form}
    return render(request,"blog/create.html",context)


def profile(request):
    user = request.user
    post_query = Posts.objects.filter(author=user)
    context = {"post_query": post_query}
    return render(request,"blog/profile.html",context)
   

def  edit_profile(request):
    if request.method == "POST":
        form = EditUser(request.POST)
        if form.is_valid():
            user = request.user
            un = form.cleaned_data["username"]
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            e = form.cleaned_data["email"]
            u = User.objects.get(username = user.username)
            u.first_name = fname
            u.last_name = lname
            u.email = e
            u.username = un
            u.save()
            return redirect("profile")
    else:
        form = EditUser(request.POST)
        
    context = {"form" : form}
    return render(request,"blog/edit_profile.html",context)

def signout(request):

    logout(request)

    return redirect("signin")
