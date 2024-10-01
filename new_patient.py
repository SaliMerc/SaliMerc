#patient registry
import datetime
def personal_info():
    global patient_name
    patient_name=input('Name of the patient: ')
    phone_number=input('Phone number: ')
    email_address=input('Email adress: ').lower()
    patient_gender=input('Gender of the patient:')
    birth_year=input('Birth year of the patient (dd/mm/YYYY): ')
    birthYear=datetime.datetime.strptime(birth_year,'%d/%m/%Y').date()
    current_date=datetime.date.today()
    age=(current_date-birthYear)/365
    print(f'The patient is {age.days} years old')
    medication_status=input('Is the patient under any medication? ')
    if medication_status=='yes':
        input("Patient's medication: ")
    weight=float(input('Weight of the patient (kg): '))
    height=float(input('Height of the patient: '))
    bmi=weight/(height)**2
    print(f'The BMI of the patient is {bmi}')
    if bmi>23:
        print('The patient is overweight')
    elif bmi<18:
        print('The patient is underweight')
    else:
        print('The patient has normal weight')
    if patient_gender.lower()=='female':
        hpv=input('Has the patient been screened for cervical cancer? ')
        if hpv.lower()=='yes':
            print('Patient to proceed with the current appointment')
        else:
            print('Patient to be screened for cervical cancer first')
    elif patient_gender.lower()=='male':
        pros=input('Has the patient been screened for prostate cancer? ')
        if pros.lower()=='yes':
            print('Patient to proceed with the currrent appontment')
        else:
            print('Patient to be screened for prostate cancer first')
    else:
        print('If patient is transgender, they should be screened for both cervical and prostate cancer')  


personal_info()
def hospital_details():
    print(f'The patient name is: {patient_name}')
    section_to_visit=input('The section to visit: ')
    doctors={
        'gynacology':'Carol Mwangi',
        'Pedeatrics':'Henry Otieno',
        'urology':'Fidel Brandon',
        'obsetrics':'Katty Mwende',
        'dermatology':'Nancy Chebet',
        'general checkup':'Felix Joshua'        
        }
    if section_to_visit.lower()=='gynacology':
        print(patient_name.upper()+' '+'to be attended to by doctor'+' '+doctors['gynacology'].upper())
    elif section_to_visit.lower()=='pedeatrics':
        print(patient_name.upper()+' '+'to be attended to by doctor'+' '+doctors['pedeatrics'].upper())
    elif section_to_visit.lower()=='urology':
        print(patient_name.upper()+' '+'to be attended to by doctor'+' '+doctors['urology'].upper())
    elif section_to_visit.lower()=='obsetrics':
        print(patient_name.upper()+' '+'to be attended to by doctor'+' '+doctors['obsetrics'].upper())
    elif section_to_visit.lower()=='dermatology':
        print(patient_name.upper()+' '+'to be attended to by doctor'+' '+doctors['dermatology'].upper())
    else:
        print(patient_name.upper()+' '+'to be attended to by doctor'+' '+doctors['general chackup'].upper())
    
    

hospital_details()
import pyttsx3 as speech
engine=speech.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def say(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


say('Please wait, you will be attended to shortly. Thank you')