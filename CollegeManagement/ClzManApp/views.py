from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
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
# For download
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	
	}

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('pdffile.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('pdffile.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "admissionform_%s.pdf" %("1")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def admissionform(request):
	context = {}
	return render(request, 'admissionform.html', context)