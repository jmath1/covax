from django.shortcuts import render, get_object_or_404
from core.models import VaccineLocation, Vote
from datetime import datetime, timedelta
def home(request):
    locations = VaccineLocation.objects.all()

    return render(request, 'index.html', {"locations": locations})

def location(request, location_id):

    def sum_scores_by_time(time_in_days):
        target_date = datetime.now() - timedelta(days=time_in_days)
        votes = Vote.objects.filter(
            location=VaccineLocation.objects.get(id=location_id),
            created_date=target_date
        )
        sum_of_votes = sum([x.score for x in votes])
        return sum_of_votes
    
    location = get_object_or_404(VaccineLocation, pk=location_id)
    
    votes_today = sum_scores_by_time(1)
    votes_this_week = sum_scores_by_time(7)
    votes_this_month = sum_scores_by_time(30)
    votes_all_time = sum_scores_by_time(3650)

    context = {
        "location": location,
        "votes_today": votes_today,
        "votes_this_week": votes_this_week,
        "votes_this_month": votes_this_month,
        "votes_all_time": votes_all_time,
    }
    return render(request, 'location.html', context=context)