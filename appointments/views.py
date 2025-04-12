from django.shortcuts import render, redirect
from .models import Doctor, Appointment
from django.utils import timezone
from .forms import AppointmentForm

# View to show available doctors and book an appointment
def home(request):
    doctors = Doctor.objects.all()
    return render(request, 'home.html', {'doctors': doctors})

# View to book an appointment
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = request.user.patient
            appointment.save()
            return redirect('appointment_success')
    
    form = AppointmentForm()
    return render(request, 'book_appointment.html', {'doctor': doctor, 'form': form})

# View to show appointment success
def appointment_success(request):
    return render(request, 'appointment_success.html')
