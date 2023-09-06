from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Coalesce
from django.shortcuts import render
from datetime import timedelta, datetime, time
from .filters import OccupiedSpaceFilter
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from collections import defaultdict
from django.http import HttpResponse
from Analytics.models import OcuppiedSpace
from Admins.models import Space


def occupancy(total, occupied):

    total_places = total
    occupied_places = occupied

    occupancy_percentage = (occupied_places / total_places) * 100

    
    labels = ['Ocupado', 'Disponible']
    sizes = [occupancy_percentage, 100 - occupancy_percentage]
    colors = ['lightcoral', 'lightskyblue']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Ensure the chart is a circle.

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def occupation_by_hours(dat):

    date = str(dat)
    date = datetime.strptime(date, "%Y-%m-%d")
    occupation_hours= [0]*24

    start_time = datetime(year=date.year, month=date.month, day=date.day, hour=5, minute=0, second=0)

    end_time = start_time + timedelta(hours=19)

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time
    )


    print(occupied_spaces.count())

    for space in occupied_spaces:
        first_hour = int(space.occupied_at.hour)
        last_hour = int(space.unoccupied_at.hour)

        while first_hour <=last_hour:
            occupation_hours[first_hour] =occupation_hours[first_hour] +1
            first_hour += 1

    occupation_hours = occupation_hours[5:25]
    print(occupation_hours)

    start_time = datetime.strptime('05:00 AM', '%I:%M %p').time()
    counter = 0

    hours_am_pm = []

    current_time = start_time

    while counter < 19:
        time_am_pm = current_time.strftime("%I:%M %p")
        
        hours_am_pm.append(time_am_pm)
        current_time = (datetime.combine(datetime.today(), current_time) + timedelta(hours=1)).time()
        counter+=1

    plt.figure(figsize=(10, 6))
    plt.bar(hours_am_pm, occupation_hours, color='blue')
    plt.xlabel('Hora del Día (AM-PM)')
    plt.ylabel('Cantidad de espacios ocupados')
    plt.title('Ocupación por Hora del Día')
    plt.xticks(rotation=45) 
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64

    


def current_occupation():
    occupied_space_count = Space.objects.all()
    sports = occupied_space_count.filter(
        classification=0,
        availability=1,
    ).count()

    restaurants = occupied_space_count.filter(
        classification=1,
        availability=1,
    ).count()

    relax = occupied_space_count.filter(
        classification=2,
        availability=1,
    ).count()

    return (sports, restaurants, relax)

def most_used_space(type_space, start_time, end_time, top=5):
    most_used_space_ids = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        unoccupied_at__lte=end_time
    ).values('space_id').annotate(
        total_hours=Coalesce(Sum(F('unoccupied_at') - F('occupied_at')), timedelta(seconds=0))
    ).order_by('-total_hours')[:top]

    most_used_spaces = Space.objects.filter(id__in=[item['space_id'] for item in most_used_space_ids], classification=type_space).order_by('id')

    space_hours = defaultdict(float)

    for item in most_used_space_ids:
        space_id = item['space_id']
        total_hours = item['total_hours'].total_seconds() / 3600  # Convertir a horas
        space_hours[space_id] = total_hours

    space_names = [space.name for space in most_used_spaces]
    hours = [space_hours[space.id] for space in most_used_spaces]

    plt.figure(figsize=(10, 6))
    plt.bar(space_names, hours)
    plt.xlabel('Espacios')
    plt.ylabel('Horas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def info(request):

    spaces = OcuppiedSpace.objects.all()
    
    myFilter = OccupiedSpaceFilter(request.GET, queryset=spaces)

    spaces = myFilter.qs

    space_frequencies = spaces.count()


    if request.method == 'POST':
        user_date = request.POST.get('date', None)

        if user_date is not None:
            start_date = user_date.replace('/', '-')
            
        else:
            start_date = datetime.now().date()
    else:
        start_date = datetime.now().date()


    
    end_date = (datetime.now()  + timedelta(days=1)).date()


    currents = current_occupation()
    context = {
        'current_occupation_sports':currents[0],
        'current_occupation_restaurants':currents[1],
        'current_occupation_relax':currents[2],
        'most_used_sports': most_used_space(0, start_date, end_date),
        'most_used_restaurants':most_used_space(1, start_date, end_date),
        'most_used_relax': most_used_space(2, start_date, end_date),
        'filter': myFilter,
        'spaces': space_frequencies,
        'current_graph_sports': occupancy(20,currents[0]),
        'current_graph_restaurants': occupancy(500, currents[1]),
        'current_graph_relax': occupancy(80, currents[2]),
        'occupation_by_hours' : occupation_by_hours(start_date)
    }
    return render(request, 'data.html', context)
