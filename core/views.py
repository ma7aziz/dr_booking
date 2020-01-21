from django.shortcuts import render,get_object_or_404, redirect
from .models import Doctor, Reservation
from .choices import SPECIALITY_CHOICES, TIME_CHOICE
import datetime

def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'doctors':doctors, 'speciality': SPECIALITY_CHOICES})


def search(request):
    queryset_list = Doctor.objects.all()
    reserved = Reservation.objects.all()
   
    if request.method == 'POST':
        print(request.POST)
        if 'name' in request.POST:
            name = request.POST['name']
            if name:
                queryset_list =queryset_list.filter(name__icontains=name)
        if 'speciality' in request.POST:
            speciality = request.POST['speciality']
            if speciality:
                queryset_list=queryset_list.filter(speciality__iexact= speciality)
        
        if 'city' in request.POST:
            city = request.POST['city']
            if city:
                queryset_list= queryset_list.filter(city__iexact=city)

        return render(request,'search.html', {'doctors':queryset_list,
                                                'reserved':reserved, 
                                                'time':TIME_CHOICE})
    
    else:
        return render(request, 'search.html', {'doctors':queryset_list, 'time':TIME_CHOICE} )



def details(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'details.html', {'doctor':doctor,'time':TIME_CHOICE})

def book(request, doctor_id ):
    if request.method == 'POST':

        doctor_id= request.POST['doctor']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time= request.POST['time']
        # get doctor
        dr = Doctor.objects.get(id=doctor_id)
        # validate dr and time 
        reservation = Reservation.objects.all()
        reserved =reservation.filter(doctor=dr, date=date, time=time)
        if reserved:
            return render(request,'details.html', {'doctor':dr, 'message':'Sorry! this time is already booked','time':TIME_CHOICE})


        else:
            reserved.filter(email=email, date=date)
            if reserved:
                return render(request,'details.html', {'doctor':dr, 'message':'Your Booking is already registered','time':TIME_CHOICE })
            else:
                
                booking= Reservation(doctor=dr, name=name, email=email, phone=phone, date=date, time=time)
                booking.save()
        return render(request, 'confirmation.html', {'booking':booking, 'doctor':dr})
    else:
        
        doctor = get_object_or_404(Doctor, pk=doctor_id)
        return render(request, 'booking.html', {'doctor':doctor,'time':TIME_CHOICE,})




# , {'message': 'You have already booked an appointment before'}