from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subject, Topic
from .forms import SubjectForm, TopicForm, LoginForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:dashboard')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'dashboard/login.html', context)

def subjects(request):
    subject_qs = Subject.objects.all().prefetch_related("topics")
    contexts = {
        "subjects": subject_qs
    }
    return render(request, "posts/subjects.html", contexts)

def dashboard(request):
    if request.user.is_authenticated:
        subject_list = Subject.objects.all()
        return render(request, "dashboard/home.html", {"subjects":subject_list})
    else:
        return redirect("posts:login")




def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:subjects')
    else:
        form = SubjectForm()
    context = {'form': form}
    return render(request, 'posts/create_subject.html', context)

def subject_details(request, pk):
    subject = Subject.objects.get(pk=pk)
    return render(request, "posts/subject_details.html", {"subject": subject})

def edit_subject(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
        if request.method == 'POST':
            form = SubjectForm(request.POST, instance=subject)
            if form.is_valid():
                form.save()
                return redirect('posts:subjects')
        else:
            form = SubjectForm(instance=subject)
        context = {"subject":subject, 'form': form}
        return render(request, 'posts/edit_subject.html', context)
    except Subject.DoesNotExist:
        return HttpResponse("Id raqam xato kiritlgan !")
    except Exception as e:
        return HttpResponse(e.args)
    
def delete_subject(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return redirect('posts:subjects')
    except Subject.DoesNotExist:
        return HttpResponse("Id raqam xato kiritlgan !")
    except Exception as e:
        return HttpResponse(e.args)
    


def create_topic(request, subject_pk):
    try:
        if request.method == 'POST':
            form = TopicForm(request.POST)
            if form.is_valid():
                topic_kwargs = {
                    "subject_id": subject_pk,
                    "title": form.cleaned_data['title'],
                    "body": form.cleaned_data['body']
                }
                Topic.objects.create(**topic_kwargs)
                return redirect('posts:subjects')
        else:
            form = TopicForm(initial={'subject': subject_pk})
            return render(request, 'posts/create_topic.html', {"subject_id": subject_pk, "form": form})
    except Exception as e:
        # Implement proper error handling here
        print(f"Error creating topic: {e}")
        return render(request, 'posts/create_topic.html',{'error': 'An error occurred while creating the topic.'})

def retrieve_topic(request, subject_pk, topic_pk):
    try:
        topic = Topic.objects.get(id=topic_pk)
        return render(request, "posts/topic_details.html", {"topic":topic})
    
    except Topic.DoesNotExist:
        return HttpResponse("Id raqam xato kiritlgan !")
    except Exception as e:
        return HttpResponse(e.args)
    
def edit_topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        if request.method == 'POST':
            form = TopicForm(request.POST, instance=topic)
            if form.is_valid():
                form.save()
                return redirect('posts:subjects')
        else:
            form = TopicForm(instance=topic)
        context = {"topic":topic, 'form': form}
        return render(request, 'posts/edit_topic.html', context)
    except Topic.DoesNotExist:
        return HttpResponse("Id raqam xato kiritlgan !")
    except Exception as e:
        return HttpResponse(e.args)

def delete_topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
        topic.delete()
        return redirect('posts:subjects')
    except Topic.DoesNotExist:
        return HttpResponse("Id raqam xato kiritlgan !")
    except Exception as e:
        return HttpResponse(e.args)
