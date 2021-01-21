from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry

# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
	model=Entry
	template_name='index.html'
	#template_name='entries/index.html'
	context_object_name="blog_entries"
	ordering=['-entry_date']
	#this is a add page(previous,next) validation
	paginate_by=3

class EntryView(LoginRequiredMixin,DetailView):
	model=Entry
	template_name='entry_detail.html'

class CreateEntryView(LoginRequiredMixin,CreateView):
	model=Entry
	template_name='create_entry.html'
	fields=['entry_title','entry_text']

	def form_valid(self,form):
		form.instance.entry_author=self.request.user
		return super().form_valid(form)