from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect

from BlogSphere import settings
from .models import *
from .forms import PostForm
from django.contrib import messages
from twilio.rest import Client
import random

# Create your views here.
def HOME(request):
    global user_mobile
    user_posts = Post.objects.all()
    tags = Tag.objects.all()
    try:
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            
            return render(request, 'main/home.html',{'user':user, 'user_posts':user_posts, 'tags':tags})
        else:
            return render(request, 'main/home.html',{'user_posts':user_posts, 'tags':tags})
    except NameError as e:
        return render(request, 'main/home.html',{'user_posts':user_posts, 'tags':tags})

def SINGLE_POST(request, slug):
    global user_mobile
    tags = Tag.objects.all()
    post=Post.objects.get(slug=slug)
    user_posts = Post.objects.all()
    comments = post.comments.all()
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        print(user_id)
        print(type(user_id))
        if user_id == 'None':
            url = '/single_post/' + slug + '/'
            messages.error(request,'Login First! ')
            return HttpResponseRedirect(url)    
        user = User.objects.get(id=user_id)
        message = request.POST.get('comment')
        comment = Comment(post=post, user=user, content=message)
        comment.save()
        url = '/single_post/' + slug + '/'
        messages.success(request,'Comment uploaded successfully! ')
        return HttpResponseRedirect(url)
    else:
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            return render(request, 'main/single_post.html',{'tags':tags, 'user_posts':user_posts, 'user':user, 'post':post, 'comments':comments})
        else:
            return render(request, 'main/single_post.html',{'tags':tags, 'user_posts':user_posts, 'post':post, 'comments':comments})

def CONTACT(request):
    global user_mobile
    try:
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            return render(request, 'main/contact.html',{'user':user})
        else:
            return render(request, 'main/contact.html')
    except NameError as e:
        return render(request, 'main/contact.html')


def LOGIN(request):
    global user_mobile
    global otp
    if request.method=='POST':
        otp_code = request.POST.get('OTP')
        user_mobile = request.POST.get('mobile')
        if str(otp) == otp_code:
            user=User.objects.get(mobile=user_mobile)
            messages.success(request,'Logged in Successfully')
            request.session['user_id'] = user.id
            return HttpResponseRedirect('/')
        else:
            messages.error(request,'Invalid OTP')
            return render(request,'registration/login.html', {'user_mobile':user_mobile})
    else:
        return render(request,'registration/login.html')

def FETCH_MOBILE_LOGIN(request):
    global user_mobile
    global otp
    user_mobile=request.GET.get('mobile')
    if len(str(user_mobile))!=10:
        error = 'Enter a valid mobile number'
        return JsonResponse({'status':'error','error':error})
    try:
        user=User.objects.get(mobile=user_mobile)
        request.session[str(user_mobile)]=user_mobile
        request.session.set_expiry(0)

        if str(user_mobile) in request.session:
            mobile=request.session[str(user_mobile)]
            verified_number = "+91"+str(mobile)
            otp=random.randint(100000,999999)
            account_sid=settings.TWILIO_ACCOUNT_SID
            auth_token=settings.TWILIO_AUTH_TOKEN
            phone_number=settings.TWILIO_PHONE_NUMBER
            client=Client(account_sid,auth_token)
            msg=client.messages.create(
                    body = f"Your otp is: {otp}",
                    from_ = phone_number,
                    to = verified_number
                )
            return JsonResponse({'status':'success','message':'OTP sent to given mobile number'})
        
    except:
        error = 'No user found with this mobile number'
        return JsonResponse({'status':'error','error':error})
    

def REGISTER(request):
    global user_mobile
    global otp
    if request.method=='POST':
        otp_code = request.POST.get('OTP')
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_mobile=request.POST.get('mobile')
        if str(otp) == otp_code:
            user=User(name=user_name, email=user_email, mobile=user_mobile)
            user.save()
            messages.success(request,'Registered Successfully')
            request.session['user_id'] = user.id
            return HttpResponseRedirect('/')
        else:
            messages.error(request,'Invalid OTP')
            return render(request,'registration/register.html', {'user_name':user_name, 'user_email':user_email, 'user_mobile':user_mobile})
    else:
        return render(request,'registration/register.html')
    

def FETCH_MOBILE(request):
    global user_mobile
    global otp
    user_mobile=request.GET.get('mobile')
    users=User.objects.all()
    if len(str(user_mobile))!=10:
        error = 'Enter a valid mobile number'
        return JsonResponse({'status':'error','error':error})
    for user in users:
        if user_mobile==str(user.mobile):
            error = 'This mobile is already registered.'
            return JsonResponse({'status':'error','error':error})
    
    request.session[str(user_mobile)]=user_mobile
    request.session.set_expiry(0)

    if str(user_mobile) in request.session:
        mobile=request.session[str(user_mobile)]
        verified_number = "+91"+str(mobile)
        otp=random.randint(100000,999999)
        account_sid=settings.TWILIO_ACCOUNT_SID
        auth_token=settings.TWILIO_AUTH_TOKEN
        phone_number=settings.TWILIO_PHONE_NUMBER
        client=Client(account_sid,auth_token)
        msg=client.messages.create(
                body = f"Your otp is: {otp}",
                from_ = phone_number,
                to = verified_number
            )
        return JsonResponse({'status':'success','message':'OTP sent to given mobile number'})
    

def MY_POSTS(request):
    try:
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            user_posts = Post.objects.filter(author_id=user_id)
            return render(request, 'main/my_posts.html',{'user':user, 'posts': user_posts})
        else:
            return render(request, 'main/my_posts.html')
    except NameError as e:
        return render(request, 'main/my_posts.html')
    
def NEW_POST(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = User.objects.get(id=request.session.get('user_id'))
            post.save()
            messages.success(request, 'Blog Uploaded successfully.')
            return HttpResponseRedirect('/new_post/')
    else:
        try:
            if 'user_id' in request.session:
                user_id = request.session['user_id']
                user = User.objects.get(id=user_id)
                form = PostForm()
                return render(request, 'main/new_post.html',{'user':user, 'form': form})
            else:
                return render(request, 'main/new_post.html')
        except NameError as e:
            return render(request, 'main/new_post.html', {'form': form})

def EDIT_POST(request, id):
    try:
        if 'user_id' in request.session:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            if request.method=='POST':
                post=Post.objects.get(id=id)
                form=PostForm(request.POST,instance=post)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Post Updated successfully.')
                    return HttpResponseRedirect('/my_posts/')
            else:
                post=Post.objects.get(id=id)
                form=PostForm(instance=post)
                return render(request, 'main/update_post.html',{'user':user, 'form':form, 'post':post})
        else:
                return render(request, 'main/my_posts.html')
    except NameError as e:
        return render(request, 'main/my_posts.html')

def DELETE_POST(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return HttpResponseRedirect('/my_posts/')