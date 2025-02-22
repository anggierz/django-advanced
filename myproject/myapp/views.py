from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer




#Implementar al menos un viewset: Este viewset es solo para usuarios admin ya que el viewset proporciona todos los endpoints
# y por seguridad no quiero permitir a otros usuarios crear y eliminar doctores.

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def destroy(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            doctor.delete()
            return Response({"message": "Doctor deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        except Doctor.DoesNotExist:
            return Response( {"message": "Doctor does not exist"},  status=status.HTTP_404_NOT_FOUND)
    
    
#Implementar al menos 4 vistas genéricas distintas para cada modelo

#Solo los administradores pueden crear doctores
class DoctorCreate(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAdminUser]

#Los usuarios autenticados o read only pueden obtener la lista de doctores. No hace falta registrarse en la clínica
#para consultar los doctores y sus especialidades
class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

#Los usuarios autenticados o con permisos read only pueden ver un doctor en concreto
class DoctorRetrieve(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
# Solo los administradores pueden eliminar doctores 
class DoctorDestroy(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAdminUser]



#Los usuarios autenticados pueden crear citas
class AppointmentCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

#Solo los administradores pueden listar todas las citas
class AppointmentList(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAdminUser]
    

#Los usuarios autenticados pueden actualizar citas. La idea es que actualicen una cita suya
class AppointmentUpdate(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
   
# Solo los administradores pueden eliminar citas
class AppointmentDestroy(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAdminUser]


#API VIEW personalizada: Listar todas las citas de un doctor en específico. Une el modelo Doctor con Appointment. Solo utilizable
# por administradores
@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def doctor_appointments(request, pk: int):
    appointments = Appointment.objects.filter(doctor_id=pk)
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)
