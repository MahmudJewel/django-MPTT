from django.shortcuts import render, redirect 
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import DeleteView

from django.views import View
from django.http import HttpResponse

from second.models import Tag, Descriptions
from second.forms import Descriptions_Form

class home_view(View):

	def get(self, request):
		tag = Tag.objects.all()
		descriptions = Descriptions.objects.all()
		descriptions_Form = Descriptions_Form()
		getid = request.GET.get("docid")
		obj = ''
		# print('ok id', getid)
		if getid is not None:
			getid = int(getid)
			obj=Descriptions.objects.get(id=getid)
			# print("instance:", aa)
			descriptions_Form = Descriptions_Form(instance=obj)
		context = {
			'tag':tag,
			"descriptions_Form": descriptions_Form,
			"descriptions" : descriptions,
			'getid':getid,
			'obj' : obj,
			# 'categories' : categories,
		}
		return render(request, 'home.html', context)
	
	def post(self, request):
		descriptions_Form = Descriptions_Form(request.POST)
		getid = request.POST.get("inpt")
		# print("instance of Id:", getid)
		if getid is not None:
			aa=Descriptions.objects.get(id=getid)
			# print("instance of post:", aa)
			descriptions_Form = Descriptions_Form(request.POST, request.FILES,instance=aa)
		if descriptions_Form.is_valid():
			descriptions_Form.save()
			print(f"Successfully saved")
			return redirect('/')
		print(f"Does not saved")
		return redirect('/')

class delete_Descriptions(DeleteView):
    model = Descriptions
    template_name = 'delete.html' #
    success_url =reverse_lazy('home')