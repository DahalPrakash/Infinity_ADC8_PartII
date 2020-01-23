from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
     return render(request, 'home.html')
def students(request):
     return render(request, 'students.html')
def staff(request):
     return render(request, 'staff.html')
def contact(request):
     return render(request, 'contact.html')
def about(request):
     return render(request, 'about.html')
def search(request):
     return render(request, 'search.html')

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
          with open(file_path, 'rb') as fh:
     response = HttpResponse(fh.read(), content_type="ClzManApp/")
     response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
     return response
     raise Http40