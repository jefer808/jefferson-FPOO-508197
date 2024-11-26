class MedicalQuote:  # Cambiado de MedicalAppointment a MedicalQuote
    def __init__(self, date, doctor, patient):
        self.date = date
        self.doctor = doctor
        self.patient = patient

    def get_info(self):
        return f"Cita médica: {self.date}, Doctor: {self.doctor.name}, Paciente: {self.patient.name}"


SPECIALTIES = {
    1: "Cardiología",
    2: "Neurología",
    3: "Pediatría",
    4: "Ginecología"
}

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = SPECIALTIES.get(specialty)  
        self.quotes = []  

    def assign_quote(self, patient, date):  
        quote = MedicalQuote(date, self, patient)  
        self.quotes.append(quote) 
        patient.add_to_history(quote) 

    def get_info(self):
        return f"Doctor: {self.name}, Especialidad: {self.specialty}"


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []

    def add_to_history(self, quote): 
        self.medical_history.append(quote)

    def list_history(self):
        return [quote.get_info() for quote in self.medical_history]  


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def list_doctors(self):
        return [doctor.get_info() for doctor in self.doctors]  # Mostrar información del doctor

    def list_patients(self):
        return [patient.name for patient in self.patients]

    def list_quotes(self):  
        quotes_info = []
        for doctor in self.doctors:
            for quote in doctor.quotes:  
                quotes_info.append(quote.get_info())
        return quotes_info


# Ejemplo de uso
if __name__ == "__main__":
    hospital = Hospital("Hospital Central")

    # Añadir doctores
    doctor1 = Doctor("Dr. Juan Pérez", 1)  
    doctor2 = Doctor("Dra. Ana Gómez", 2)  
    doctor3 = Doctor("Dr. Carlos Castllo", 3) 
    doctor4 = Doctor("Dr. Enrique Inglesias", 4)  
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    hospital.add_doctor(doctor3)
    hospital.add_doctor(doctor4)

    # Añadir pacientes
    patient1 = Patient("Carlos López", 30)
    patient2 = Patient("María García", 25)
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Asignar citas
    doctor1.assign_quote(patient1, "2024-10-15")  
    doctor2.assign_quote(patient2, "2024-10-16")  

    
    print("Doctores:")
    for doctor_info in hospital.list_doctors():
        print(doctor_info)
    
    print("Pacientes:", hospital.list_patients())

    
    print("Citas médicas:")
    for quote in hospital.list_quotes():  
        print(quote)

    
    print("Historial clínico de Carlos López:")
    for quote in patient1.list_history(): 
        print(quote)
