from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Coalesce
from django.shortcuts import render
from datetime import timedelta, datetime, time
from .filters import OccupiedSpaceFilter
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from collections import defaultdict
<<<<<<< HEAD


from Analytics.models import OcuppiedSpace
from Admins.models import Space



def occupancy(total, occupied):
    # Occupancy data
    total_places = total
    occupied_places = occupied

    # Calculate occupancy percentage
    occupancy_percentage = (occupied_places / total_places) * 100

    # Create a pie chart
=======
from django.http import HttpResponse
from Analytics.models import OcuppiedSpace
from Admins.models import Space


def occupancy(total, occupied):

    total_places = total
    occupied_places = occupied

    occupancy_percentage = (occupied_places / total_places) * 100

    
>>>>>>> juan
    labels = ['Ocupado', 'Disponible']
    sizes = [occupancy_percentage, 100 - occupancy_percentage]
    colors = ['lightcoral', 'lightskyblue']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Ensure the chart is a circle.

<<<<<<< HEAD
    # Convert the chart to a BytesIO object
=======
>>>>>>> juan
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

<<<<<<< HEAD
    # Encode the image in base64
    image_base64 = base64.b64encode(buffer.read()).decode()

    # Render the template with the image
    return image_base64


def occupation_by_hours():
    date = datetime(year = 2023, month=8, day = 28)
=======
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def occupation_by_hours(dat):

    date = str(dat)
    date = datetime.strptime(date, "%Y-%m-%d")
>>>>>>> juan

    occupation_hours = [0]*19

    current_hour = datetime(year=date.year, month=date.month, day=date.day, hour=5, minute=0, second=0)
<<<<<<< HEAD
    final_hour = time(hour=23, minute=0, second=0)
    delta = timedelta(hours=1)
    spaces = OcuppiedSpace.objects.all()
    counter = 0

    while current_hour < final_hour:
        next_hour = current_hour + delta

        ocupation = spaces.filter(
            space_id__occupied_at__date=date,
            space_id__occupied_at__time__gte=current_hour,
            space_id__occupied_at__time__lt=next_hour
=======
    delta = timedelta(hours=1)
    counter = 0

    while counter < 19:
        next_hour = current_hour + delta

        ocupation = OcuppiedSpace.objects.filter(
            occupied_at__date=date,
            occupied_at__time__gte=current_hour.time(),
            occupied_at__time__lt=next_hour.time()
>>>>>>> juan
        ).count()

        occupation_hours[counter] = ocupation
        counter +=1

        current_hour = next_hour

<<<<<<< HEAD
    return occupation_by_hours
=======

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

>>>>>>> juan

    


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

<<<<<<< HEAD
    # Crear un diccionario para almacenar las horas por espacio
=======
>>>>>>> juan
    space_hours = defaultdict(float)

    for item in most_used_space_ids:
        space_id = item['space_id']
        total_hours = item['total_hours'].total_seconds() / 3600  # Convertir a horas
        space_hours[space_id] = total_hours

<<<<<<< HEAD
    # Crear un gráfico de barras para mostrar las horas por espacio
=======
>>>>>>> juan
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

<<<<<<< HEAD
    print(occupation_by_hours())
    #Filter by each space

=======
>>>>>>> juan
    spaces = OcuppiedSpace.objects.all()
    
    myFilter = OccupiedSpaceFilter(request.GET, queryset=spaces)

    spaces = myFilter.qs

    space_frequencies = spaces.count()


<<<<<<< HEAD
    #Time
    start_date = datetime(2023, 8, 28)  # Fecha de inicio que el usuario elija
    end_date = datetime(2023, 8, 30)  # Fecha de fin que el usuario elija
=======
    if request.method == 'POST':
        user_date = request.POST.get('date', None)

        if user_date is not None:
            start_date = user_date.replace('/', '-')
            
        else:
            start_date = datetime.now().date()
    else:
        start_date = datetime.now().date()


    
    end_date = (datetime.now()  + timedelta(days=1)).date()

>>>>>>> juan

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
<<<<<<< HEAD
    }
    return render(request, 'data.html', context)
=======
        'occupation_by_hours' : occupation_by_hours(start_date)
    }
    return render(request, 'data.html', context)
>>>>>>> juan
