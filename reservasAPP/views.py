from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .forms import ReservaForm
from reservasAPP.models import Reserva
from reservasAPP.serializers import ReservaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib import messages
# Create your views here.

def landingPage(request):
    return render(request, 'landingPage.html')

def reservasView(request):
    reservas = Reserva.objects.all()
    data = {'reservas':list(reservas.values())}
    return render(request, 'reservas.html', data)



def agregar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.estado = 'RESERVADO'
            reserva.save()
            messages.success(request, 'La reserva se ha agregado exitosamente.')
            return redirect('reservas')
    else:
        form = ReservaForm()
        form.fields['estado'].initial = 'RESERVADO'
        form.fields['estado'].widget.attrs['readonly'] = True
        form.fields['estado'].widget.attrs['disabled'] = True
    
    return render(request, 'Reservar.html', {'form': form})




def editarReserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservaEdit.html', {'form': form})

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
    
@api_view(['GET', 'POST'])
def reservasList(request):
    if request.method == 'GET':
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
def reservasDetail(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
