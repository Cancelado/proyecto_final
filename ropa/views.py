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
	#pass
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
def listarColor(request):
	color = Color.objects.all()
	return render(request, 'color/lista.html', {'color':color})

def nuevoColor(request):
	if request.method == "POST":
		form = ColorForm(request.POST)
		print request.POST
		if form.is_valid():
			color = form.save()
			color.save()
			return redirect('color.views.listar')
	else:
		form = ColorForm
	return render(request,'color/nuevoColor.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarColor(request, pk):
	color = get_object_or_404(Color, pk=pk)
	color.delete()
	return redirect('listar')

def eliminar_post_color(request):
	color = Color.objects.get(id=request.POST.get('idEliminar'))
	color.delete()
	return redirect('listar')

def editarColor(request, pk):
	color = get_object_or_404(Color, pk=pk)
	if request.method == "POST":
		form = ColorForm(request.POST, instance=color)
		#print request.POST
		if form.is_valid():
			color = form.save()
			color.save()
			return redirect('listar')
	else:
		form = ColorForm(instance=color)
	return render(request,'color/nuevoColor.html',{'form':form, 'etiqueta':'Actualizar'})

def editar_post_color(request):
	if request.POST.get('idEditar'):
		color = Color.objects.get(id=request.POST.get('idEditar'))
		form = ColorForm(instance=color)
	else:
		color = Color.objects.get(id=request.POST.get('id'))
		form = ColorForm(request.POST,instance=color)
		if form.is_valid():
			color = form.save()
			color.save()
			return redirect('listar')
	return render(request,'color/nuevoColor.html',{'form':form, 'id' : color.id,'etiqueta':'Actualizar'})

"""TipoPrenda"""
def listarTipoPrenda(request):
	tipoPrenda = TipoPrenda.objects.all()
	return render(request, 'tipoPrenda/lista.html', {'tipoPrenda':tipoPrenda})

def nuevoTipoPrenda(request):
	if request.method == "POST":
		form = TipoPrendaForm(request.POST)
		print request.POST
		if form.is_valid():
			tipoPrenda = form.save()
			tipoPrenda.save()
			return redirect('tipoPrenda.views.listar')
	else:
		form = TipoPrendaForm
	return render(request,'tipoPrenda/tipoPrenda.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarTipoPrenda(request, pk):
	tipoPrenda = get_object_or_404(TipoPrenda, pk=pk)
	tipoPrenda.delete()
	return redirect('listar')

def eliminar_post_TipoPrenda(request):
	tipoPrenda = TipoPrenda.objects.get(id=request.POST.get('idEliminar'))
	tipoPrenda.delete()
	return redirect('listar')

def editarTipoPrenda(request, pk):
	tipoPrenda = get_object_or_404(TipoPrenda, pk=pk)
	if request.method == "POST":
		form = TipoPrendaForm(request.POST, instance=tipoPrenda)
		#print request.POST
		if form.is_valid():
			tipoPrenda = form.save()
			tipoPrenda.save()
			return redirect('listar')
	else:
		form = TipoPrendaForm(instance=tipoPrenda)
	return render(request,'tipoPrenda/tipoPrenda.html',{'form':form, 'etiqueta':'Actualizar'})

def editar_post_TipoPrenda(request):
	if request.POST.get('idEditar'):
		tipoPrenda = TipoPrenda.objects.get(id=request.POST.get('idEditar'))
		form = TipoPrendaForm(instance=tipoPrenda)
	else:
		tipoPrenda = TipoPrenda.objects.get(id=request.POST.get('id'))
		form = TipoPrendaForm(request.POST,instance=tipoPrenda)
		if form.is_valid():
			tipoPrenda = form.save()
			tipoPrenda.save()
			return redirect('listar')
	return render(request,'tipoPrenda/tipoPrenda.html',{'form':form, 'id' : tipoPrenda.id,'etiqueta':'Actualizar'})

"""TipoTela"""
def listarTipoTela(request):
	tipoTela = TipoTela.objects.all()
	return render(request, 'tipoTela/tipoTela.html', {'tipoTela':tipoTela})

def nuevoTipoTela(request):
	if request.method == "POST":
		form = TipoTelaForm(request.POST)
		print request.POST
		if form.is_valid():
			tipoTela = form.save()
			tipoTela.save()
			return redirect('tipoTela.views.listar')
	else:
		form = TipoTelaForm
	return render(request,'tipoTela/tipoTela.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarTipoTela(request, pk):
	tipoTela = get_object_or_404(TipoTela, pk=pk)
	tipoTela.delete()
	return redirect('listar')

def eliminar_post_TipoTela(request):
	tipoTela = TipoTela.objects.get(id=request.POST.get('idEliminar'))
	tipoTela.delete()
	return redirect('listar')

def editarTipoTela(request, pk):
	tipoTela = get_object_or_404(TipoTela, pk=pk)
	if request.method == "POST":
		form = TipoTelaForm(request.POST, instance=tipoTela)
		#print request.POST
		if form.is_valid():
			tipoTela = form.save()
			tipoTela.save()
			return redirect('listar')
	else:
		form = TipoTelaForm(instance=tipoTela)
	return render(request,'tipoTela/TipoTela.html',{'form':form, 'etiqueta':'Actualizar'})

def editar_post_TipoTela(request):
	if request.POST.get('idEditar'):
		tipoTela = TipoTela.objects.get(id=request.POST.get('idEditar'))
		form = TipoTelaForm(instance=tipoTela)
	else:
		tipoTela = TipoTela.objects.get(id=request.POST.get('id'))
		form = TipoTelaForm(request.POST,instance=tipoTela)
		if form.is_valid():
			tipoTela = form.save()
			tipoTela.save()
			return redirect('listar')

	return render(request,'tipoTela/tipoTela.html',{'form':form, 'id' : tipoTela.id,'etiqueta':'Actualizar'})

	return render(request,'tipoTela/tipoTela.html',{'form':form, 'id' : tipoTela.id,'etiqueta':'Actualizar'})

