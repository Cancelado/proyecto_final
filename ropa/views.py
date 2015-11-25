# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from ropa.models import Ropa
from ropa.models import Color
from ropa.models import TipoPrenda
from ropa.models import TipoTela
from ropa.forms import RopaForm
from ropa.forms import ColorForm
from ropa.forms import TipoPrendaForm
from ropa.forms import TipoTelaForm

"""Ropa"""
def listar(request):
	ropa = Ropa.objects.all()
	return render(request, 'ropa/lista.html', {'ropa':ropa})

def nuevo(request):
	if request.method == "POST":
		form = RopaForm(request.POST)
		print request.POST
		if form.is_valid():
			ropa = form.save()
			ropa.save()
			return redirect('ropa.views.listar')
	else:
		form = RopaForm
	return render(request,'ropa/ropa_nueva.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminar(request, pk):
	ropa = get_object_or_404(Ropa, pk=pk)
	ropa.delete()
	return redirect('listar')

def eliminar_post(request):
	ropa = Ropa.objects.get(id=request.POST.get('idEliminar'))
	ropa.delete()
	return redirect('listar')

def editar(request, pk):
	ropa = get_object_or_404(Ropa, pk=pk)
	if request.method == "POST":
		form = RopaForm(request.POST, instance=ropa)
		#print request.POST
		if form.is_valid():
			ropa = form.save()
			ropa.save()
			return redirect('listar')
	else:
		form = RopaForm(instance=ropa)
	return render(request,'ropa/ropa_nueva.html',{'form':form, 'etiqueta':'Actualizar'})

def editar_post(request):
	if request.POST.get('idEditar'):
		ropa = Ropa.objects.get(id=request.POST.get('idEditar'))
		form = RopaForm(instance=ropa)
	else:
		ropa = Ropa.objects.get(id=request.POST.get('id'))
		form = RopaForm(request.POST,instance=ropa)
		if form.is_valid():
			ropa = form.save()
			ropa.save()
			return redirect('listar')
	return render(request,'ropa/ropa_nueva.html',{'form':form, 'id' : ropa.id,'etiqueta':'Actualizar'})

"""Color"""
"""TipoPrenda"""
"""TipoTela"""