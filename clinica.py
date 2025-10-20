from faker import Faker
import random

fake = Faker('es_ES')

# Especialidades médicas
especialidades = ["Medicina General", "Pediatría", "Cardiología", "Dermatología", "Oftalmología"]

print("SISTEMA DE GESTIÓN CLÍNICA")
print("=" * 50)

for i in range(4):
    # Datos personales
    nombre = fake.first_name()
    apellido = fake.last_name()
    
    # Datos médicos
    edad = fake.random_int(1, 90)
    peso = f"{fake.random_int(45, 120)} kg"
    altura = f"1.{fake.random_int(50, 95)} m"
    especialidad = random.choice(especialidades)
    seguro_medico = fake.random_element(["Sí", "No"])
    
    print(f"\n  PACIENTE {i+1}:")
    print(f"    {nombre} {apellido}")
    print(f"    {edad} años |  {altura} |  {peso}")
    print(f"    Especialidad: {especialidad}")
    print(f"    Seguro médico: {seguro_medico}")
    print(f"    Contacto: {fake.phone_number()}")
    print(f"    Dirección: {fake.address().replace(chr(10), ', ')}")