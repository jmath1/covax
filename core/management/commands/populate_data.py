from django.core.management.base import BaseCommand, CommandError
from core.populate_data import fake_vaccine_location, fake_vote, fake_appointment
from core.models import Appointment, Vote, VaccineLocation
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--votes', type=int)
        parser.add_argument('--locations', type=int)
        parser.add_argument('--appointments', type=int)

    def handle(self, *args, **options):
        locations = options.get("locations")
        votes = options.get("votes")
        appointments = options.get("appointments")
        if not locations and not votes_per_location and not appointments:
            print("You must use a --votes, --locations, or --appointments flag followed by an integer")
        
        if locations:
            for x in range(1,locations + 1):
                vaccine_location_data = fake_vaccine_location()
                loc = VaccineLocation(**vaccine_location_data)
                loc.save()
                print(f"Created {loc}")

        if votes:
            for x in range(1, votes + 1):
                vote_data = fake_vote()
                vote = Vote(**vote_data).save()
                print(f"Created {vote}")

        if appointments:
            for x in range(1, appointments + 1):
                appointment_data = fake_appointment()
                appointment = Appointment(**appointment_data).save()
                print(f"Created {appointment}")
