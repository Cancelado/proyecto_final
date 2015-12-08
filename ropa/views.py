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
	print (ropa)
	ropa.delete()
	return redirect('listar')


def editar(request, pk):
	if request.method == "POST":
		ropa = Ropa.objects.get(id=request.POST['id'])
		form = RopaForm(request.POST, instance=ropa)
		#print request.POST
		if form.is_valid():
			ropa = form.save()
			ropa.save()
			return redirect('listar')
	else:
		form = RopaForm(instance=ropa)
	return render(request,'ropa/ropa_nueva.html',{'form':form, 'etiqueta':'Actualizar'})


"""Color"""
def listarColor(request):
	color = Color.objects.all()
	return render(request, 'color/listaColor.html', {'color':color})

def nuevoColor(request):
	if request.method == "POST":
		form = ColorForm(request.POST)
		print request.POST
		if form.is_valid():
			color = form.save()
			color.save()
			return redirect('color.views.listaColor')
	else:
		form = ColorForm
	return render(request,'color/nuevoColor.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarColor(request, pk):
	color = get_object_or_404(Color, pk=pk)
	color.delete()
	return redirect('color/listaColor.html')

def eliminar_post_color(request):
	color = Color.objects.get(id=request.POST.get('idEliminar'))
	color.delete()
	return redirect('color/listaColor.html')

def editarColor(request, pk):
	color = get_object_or_404(Color, pk=pk)
	if request.method == "POST":
		form = ColorForm(request.POST, instance=color)
		#print request.POST
		if form.is_valid():
			color = form.save()
			color.save()
			return redirect('color/listaColor.html')
	else:
		form = ColorForm(instance=color)
	return render(request,'color/nuevoColor.html',{'form':form, 'etiqueta':'Actualizar'})


"""TipoPrenda"""
def listarTipoPrenda(request):
	tipoPrenda = TipoPrenda.objects.all()
	return render(request, 'tipoPrenda/listaTipoPrenda.html', {'tipoPrenda':tipoPrenda})

def nuevoTipoPrenda(request):
	if request.method == "POST":
		form = TipoPrendaForm(request.POST)
		print request.POST
		if form.is_valid():
			tipoPrenda = form.save()
			tipoPrenda.save()
			return redirect('listaTipoPrenda.html')
	else:
		form = TipoPrendaForm
	return render(request,'tipoPrenda/nuevoTipoPrenda.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarTipoPrenda(request, pk):
	tipoPrenda = get_object_or_404(TipoPrenda, pk=pk)
	tipoPrenda.delete()
	return redirect('tipoPrenda/listaTipoPrenda.html')

def eliminar_post_TipoPrenda(request):
	tipoPrenda = TipoPrenda.objects.get(id=request.POST.get('idEliminar'))
	tipoPrenda.delete()
	return redirect('tipoPrenda/listaTipoPrenda.html')

def editarTipoPrenda(request, pk):
	tipoPrenda = get_object_or_404(TipoPrenda, pk=pk)
	if request.method == "POST":
		form = TipoPrendaForm(request.POST, instance=tipoPrenda)
		#print request.POST
		if form.is_valid():
			tipoPrenda = form.save()
			tipoPrenda.save()
			return redirect('tipoPrenda/listaTipoPrenda.html')
	else:
		form = TipoPrendaForm(instance=tipoPrenda)
	return render(request,'tipoPrenda/tipoPrenda.html',{'form':form, 'etiqueta':'Actualizar'})


"""TipoTela"""
def listarTipoTela(request):
	tipoTela = TipoTela.objects.all()
	return render(request, 'tipoTela/listaTipoTela.html', {'tipoTela':tipoTela})

def nuevoTipoTela(request):
	if request.method == "POST":
		form = TipoTelaForm(request.POST)
		print request.POST
		if form.is_valid():
			tipoTela = form.save()
			tipoTela.save()
			return redirect('tipoTela/listaTipoTela.html')
	else:
		form = TipoTelaForm
	return render(request,'tipoTela/nuevoTipoTela.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarTipoTela(request, pk):
	tipoTela = get_object_or_404(TipoTela, pk=pk)
	tipoTela.delete()
	return redirect('tipoTela/listaTipoTela.html')

def editarTipoTela(request, pk):
	tipoTela = get_object_or_404(TipoTela, pk=pk)
	if request.method == "POST":
		form = TipoTelaForm(request.POST, instance=tipoTela)
		#print request.POST
		if form.is_valid():
			tipoTela = form.save()
			tipoTela.save()
			return redirect('tipoTela/listaTipoTela.html')
	else:
		form = TipoTelaForm(instance=tipoTela)
	return render(request,'tipoTela/TipoTela.html',{'form':form, 'etiqueta':'Actualizar'})
