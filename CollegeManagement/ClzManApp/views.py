from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.views import View
from .forms import OurForm
from .models import Book
from django.db.models import Q
# Create your views here.
def home(request):
     return render(request, 'home.html')
def academic(request):
     return render(request, 'academic.html')
def contact(request):
     return render(request, 'contact.html')
	 
def about(request):
     return render(request, 'about.html')
def search(request):
     return render(request, 'search.html')

	 
# For upload,download,search pdf file

def admissionform(request):
	context = {}
	return render(request, 'admissionform.html', context)

def upload_file(request):
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personal:list')
        
    else:
        form = OurForm()
    return render(request, "uploadfile.html", {"form":form})
    

def list_file(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET['q']    
    
    
    book = get_data_queryset(query)
    context['books'] = book
    return render(request, "filelist.html", context)

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        books = Book.objects.filter(Q(title__icontains=q) | Q(name__icontains=q))
        
        for book in books:
            queryset.append(book)
    
    return list(set(queryset))