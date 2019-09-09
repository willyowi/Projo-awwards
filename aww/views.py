from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from aww.models import *
from aww.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration.html', {'form': form})

@login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"

    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    context ={"profiles":profiles,"projects":projects,"reviews":reviews,"message":message}

    return render(request,'index.html',context)

@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    
    users = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()

    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)


    projects = Project.get_profile_pic(profile.id)
    return render(request, 'registration/profile.html', {'title':title,'profile':profile,"projects":projects, 'profile_info':profile_info,"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):

    profile = User.objects.get(username=request.user)
    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            # return HttpResponseRedirect(reverse('profile', username=request.user))

            return redirect('profile', username=request.user)
    else:
        form = ProfileForm()

    return render(request, 'registration/update_profile.html', {'form':form, 'profile_info':profile_info})

@login_required(login_url='/accounts/login')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
            # messages.success(request, "Image uploaded!")
			return redirect('index')
	else:
			form = ProjectForm()
            # context= {"form":form}
	return render(request, 'project.html',{"form":form})

@login_required(login_url='/accounts/login')
def project_details(request,id):
    project = Project.objects.get(id = id)
    reviews = Review.objects.order_by('-timestamp')

    context={"project":project,"reviews":reviews}
    return render(request, 'project_details.html',context)

@login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    proj = Project.project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # reviews = form.save(commit=False)
            # reviews.project = project
            # reviews.user = current_user
            # reviews.save()

            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Review()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (review.design + review.usability + review.content)/3
            review.save()
            # return redirect('index')
            return HttpResponseRedirect(reverse('projectdetails', args=(project.id,)))
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {"user":current_user,"project":proj,"form":form})

def review_list(request):
    latest_review_list = Review.objects.order_by('-timestamp')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

def search_projects(request):
    # profile = Profile.get_profile()

    # if 'caption' in request.GET and request.GET["caption"]:
    if 'title' in request.GET and request.GET["title"]:

        search_term = request.GET.get("title")
        found_projects = Project.search_by_title(search_term)
        message = f"{search_term}"
        print(search_term)

        context = {"found_projects":found_projects,"message":message}

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        # context={"message":message}
        return render(request, 'search.html',{"message":message})


class ProjectList(APIView):
    def get(self, request, format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

    def put(self,request, pk, format=None):
        merch = self.get_project(pk)
        serializers = MerchSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)


    def put(self, request, pk, format = None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        else:
            return Response(serializers.errors,
                            status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
