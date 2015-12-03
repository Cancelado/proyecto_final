# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm

def listarU(request):
	users = Usuario.objects.all()
	return render(request, 'usuarios/lista.html', {'usuarios':users})

def nuevoU(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		print request.POST
		if form.is_valid():
			user = form.save()
			user.save()
			return redirect('usuarios.views.listarU')
	else:
		form = UsuarioForm
	return render(request,'usuarios/usuario_nuevo.html',{'form':form, 'etiqueta':'Nuevo'})

def eliminarU(request, pk):
	user = get_object_or_404(Usuario, pk = pk)
	#user = Usuario.objects.get(pk = pk)
	user.delete()
	return redirect('listarU')

def editarU(request, pk):
	user = get_object_or_404(Usuario, pk = pk)
	if request.method == "POST":
		form = UsuarioForm(request.POST, instance = user)
		print request.POST
		if form.is_valid():
			user = form.save()
			user.save()
			return redirect('listarU')
	else:
		form = UsuarioForm (instance=user)
	return render(request,'usuarios/usuario_nuevo.html',{'form':form, 'etiqueta':'Actualizar'})