from faker import Faker
import random

# Crear instancia de Faker en español
fake = Faker('es_ES')

# Lista de carreras universitarias típicas
carreras = [
    "Ingeniería Informática",
    "Medicina", 
    "Derecho",
    "Administración de Empresas",
    "Psicología",
    "Arquitectura",
    "Biología",
    "Periodismo"
]

print("🎓 UNIVERSIDAD FICTICIA - DATOS DE ESTUDIANTES")
print("=" * 50)

# Generar 8 estudiantes universitarios
for i in range(8):
    nombre = fake.first_name()
    apellido = fake.last_name()
    carrera = random.choice(carreras)
    email_universitario = f"{nombre.lower()}.{apellido.lower()}@universidad.edu"
    matricula = fake.random_number(digits=8, fix_len=True)
    promedio = round(random.uniform(6.0, 10.0), 2)
    semestre = random.randint(1, 10)
    
    print(f"Estudiante {i+1}:")
    print(f"👤 {nombre} {apellido}")
    print(f"🎯 Carrera: {carrera}")
    print(f"📧 Email: {email_universitario}")
    print(f"🔢 Matrícula: {matricula}")
    print(f"⭐ Promedio: {promedio}")
    print(f"📚 Semestre: {semestre}")
    print(f"🏠 Dirección: {fake.address().replace('\n', ', ')}")
    print("-" * 50)