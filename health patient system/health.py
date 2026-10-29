# PROG221 - health - patient system
# student : Symon James - 905006238
# DPG compliant + task 1,2,3

class patient:
    total_patients = 0

    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        patient.total_patients += 1

    def display_info(self): # instance method 
        return f"[patient] ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}"

    def update_record(self, new_diagnosis): # method require in task 1
        self.diagnosis = new_diagnosis
    
    @staticmethod # static method - complusory
    def is_valid_age(age):
        return 0 < age < 120

    @classmethod # complusory task 3
    def get_total_patients(cls):
        return cls.total_patients

class doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def display_info(self):
        return f"[Doctor] ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}"

# data structure - dictonary - task 3
hospital_db = {}

def add_patient(patient):
    hospital_db[patient.patient_id] = patient

def display_all():
    for p in hospital_db. values():
        print(p.display_info())

# object creation and interaction
p1 = patient(101, "Mohamed Sesay", 30, "malaria")
p2 = patient(102, "Fatima ConteH", 25, "typhoid")
p3 = patient(103, "Neymar Junior", 40, "checkup")
d1 = doctor (1, "Dr. Kamara", "General")

add_patient(p1)
add_patient(p2)
add_patient(p3)

display_all()

print(f"total patients: {patient.get_total_patients()}")
print(f"doctor: {d1.display_info()}")