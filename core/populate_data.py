from faker import Faker, providers
from core.models import VaccineLocation
from django.contrib.auth.models import User
faker = Faker()

def fake_vaccine_location():
    def make_clinic_names():
        my_names = []
        for x in range(0,30):
            my_names.append(f"{faker.first_name()}'s Clinic")
        return set(my_names)

    city = faker.city()
    state = faker.state_abbr()
    zip_code = faker.zipcode()
    address = faker.address()
    clinic_name = faker.random_choices(elements=make_clinic_names())[0]
    phone_number = faker.phone_number()
    register_link = faker.url()

    return {
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "address": address,
        "clinic_name": clinic_name,
        "phone_number": phone_number,
        "register_link": register_link
    }

def fake_vote():
    vote_choices = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5,)
    try:
        location = faker.random_choices(elements=set(VaccineLocation.objects.all()))[0]
    except:
        print("Locations must be made first")
        return
    score = faker.random_choices(elements=vote_choices)[0]
    created_date = faker.date_between(start_date='-30d', end_date='today')
    try:
        voted_by = faker.random_choices(elements=set(User.objects.all()))[0]
    except:
        print("Users must be made first")
        return
    return {
        "location": location,
        "score": score,
        "created_date": created_date,
        "voted_by": voted_by
    }

def fake_appointment():

    def get_appointment_status(appointment_finished_date):
        if appointment_finished_date:
            return 'Complete'
        else:
            status_choices = (
                'Pending',
                'Missed',
            )
            return faker.random_choices(elements=status_choices)[0]

    def get_appointment_finished():
        finished_choices = (
            None, faker.date_between(start_date='-7d',  end_date='today')
        )
        return faker.random_choices(elements=finished_choices)[0]
        
    ages = set([x for x in range(15,100)])
    try:
        location = faker.random_choices(elements=set(VaccineLocation.objects.all()))[0]
    except:
        print("Locations must be made first")
        return

    appointment_reasons = {
        "high risk",
        "medical staff",
        "other"
    }
    appointment_made_date = faker.date_between(start_date='-7d',  end_date='today')
    appointment_finished_date = get_appointment_finished()
    status = get_appointment_status(appointment_finished_date)
    reason = faker.random_choices(elements=appointment_reasons)[0]
    age = faker.random_choices(elements=ages)[0]

    return {
        "appointment_made_date": appointment_made_date,
        "appointment_finished_date": appointment_finished_date,
        "location": location,
        "status": status,
        "reason": reason,
        "age": age,
    }