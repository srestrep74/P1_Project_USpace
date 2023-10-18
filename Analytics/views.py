from django.db.models import Sum, F
from django.db.models.functions import Coalesce
from django.shortcuts import render
from datetime import timedelta, datetime  
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
from .filters import OccupiedSpaceFilter
from io import BytesIO
from collections import defaultdict
from Analytics.models import OcuppiedSpace
from Admins.models import Space
import base64
import matplotlib.pyplot as plt


def occupancy(total, occupied):
    total_places = total
    occupied_places = occupied
    occupancy_percentage = (occupied_places / total_places) * 100
    labels = ['Ocupado', 'Disponible']
    sizes = [occupancy_percentage, 100 - occupancy_percentage]
    colors = ['lightcoral', 'lightskyblue']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def occupation_by_year(dat):
    date = str(dat)
    date = datetime.strptime(date, "%Y-%m-%d")
    occupation_month_restaurants = [0]*12
    occupation_month_sports = [0]*12
    occupation_month_relax = [0]*12
    start_time = datetime(year=date.year, month=1, day = 1)
    end_time = datetime(year=date.year, month=12, day = 30)

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time, 
        space_id__classification = 0
    )

    for ocuppied in occupied_spaces:
        occupation_month_sports[int(ocuppied.occupied_at.month)-1] += 1 

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time, 
        space_id__classification = 1
    )
    for ocuppied in occupied_spaces:
        occupation_month_restaurants[int(ocuppied.occupied_at.month)-1] += 1 


    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time, 
        space_id__classification = 2
    )
     
    for ocuppied in occupied_spaces:
        occupation_month_relax[int(ocuppied.occupied_at.month)-1] += 1 

    colors = {
        "Restaurantes": "blue",
        "Zonas de Descanso": "purple",
        "Zonas Deportivas": "green"
    }

    months_labels = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

    fig, ax = plt.subplots()

    ax.plot(months_labels, occupation_month_restaurants, marker='o', linestyle='-', color=colors["Restaurantes"], label='Restaurantes')

    ax.plot(months_labels, occupation_month_relax, marker='o', linestyle='-', color=colors["Zonas de Descanso"], label='Zonas de Descanso')

    ax.plot(months_labels, occupation_month_sports, marker='o', linestyle='-', color=colors["Zonas Deportivas"], label='Zonas Deportivas')

    ax.set_xlabel("Meses")
    ax.set_ylabel("Ocupación")
    ax.set_title("Ocupación por Mes y Categoría")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.savefig('media/occupation_by_month.png')
    buffer.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def occupancy_by_months(dat):
    date = str(dat)
    date = datetime.strptime(date, "%Y-%m-%d")
    start_time = datetime(year=date.year, month=date.month, day = 1)
    if date.month == 4 or date.month == 6 or date.month == 9 or date.month == 11:
        delta = 30
        div = [8,15,23,30]
    elif date.month == 2:
        delta = 28
        div = [7,14,21,28]
    else:
        delta = 31
        div = [7,15,23,31]

    weeks_restaurants = [0]*4
    weeks_sports = [0]*4
    weeks_relax = [0]*4
    end_time = start_time + timedelta(days=delta)

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time, 
        space_id__classification = 0
    )

    for space in occupied_spaces:
        day = space.occupied_at.day
        if day <= div[0]:
            weeks_sports[0] += 1 
        elif day <= div[1]:
            weeks_sports[1] +=1
        elif day <= div[2]:
            weeks_sports[2] +=1
        else:
            weeks_sports[3] +=1

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time, 
        space_id__classification = 1
    )
    
    for space in occupied_spaces:
        day = space.occupied_at.day
        if day <= div[0]:
            weeks_restaurants[0] += 1 
        elif day <= div[1]:
            weeks_restaurants[1] +=1
        elif day <= div[2]:
            weeks_restaurants[2] +=1
        else:
            weeks_restaurants[3] +=1

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time, 
        space_id__classification = 2
    )
    
    for space in occupied_spaces:
        day = space.occupied_at.day
        if day <= div[0]:
            weeks_relax[0] += 1 
        elif day <= div[1]:
            weeks_relax[1] +=1
        elif day <= div[2]:
            weeks_relax[2] +=1
        else:
            weeks_relax[3] +=1

    colors = {
        "Restaurantes": "blue",
        "Zonas de Descanso": "purple",
        "Zonas Deportivas": "green"
    }

    fig, ax = plt.subplots()

    weeks_labels = ["Semana 1", "Semana 2" ,"Semana 3" ,"Semana 4"]

    ax.plot(weeks_labels, weeks_restaurants, marker='o', linestyle='-', color=colors["Restaurantes"], label='Restaurantes')

    ax.plot(weeks_labels, weeks_relax, marker='o', linestyle='-', color=colors["Zonas de Descanso"], label='Zonas de Descanso')

    ax.plot(weeks_labels, weeks_sports, marker='o', linestyle='-', color=colors["Zonas Deportivas"], label='Zonas Deportivas')

    ax.set_xlabel("Semanas")
    ax.set_ylabel("Ocupación")
    ax.set_title("Ocupación por Semana y Categoría")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')      
    plt.savefig('media/occupation_by_week.png')

    buffer.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64
        
    
def occupation_by_day(dat):
    date = str(dat)
    date = datetime.strptime(date, "%Y-%m-%d")
    occupation_hours_sports = [0]*24
    occupation_hours_restaurants = [0]*24
    occupation_hours_relax = [0]*24
    start_time = datetime(year=date.year, month=date.month, day=date.day, hour=5, minute=0, second=0)
    end_time = start_time + timedelta(hours=19)

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time,
        space_id__classification = 0
    )

    for space in occupied_spaces:
        first_hour = int(space.occupied_at.hour)
        last_hour = int(space.unoccupied_at.hour)
        while first_hour <=last_hour:
            occupation_hours_sports[first_hour] =occupation_hours_sports[first_hour] +1
            first_hour += 1

    occupation_hours_sports = occupation_hours_sports[5:25]


    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time,
        space_id__classification = 1
    )

    for space in occupied_spaces:
        first_hour = int(space.occupied_at.hour)
        last_hour = int(space.unoccupied_at.hour)
        while first_hour <=last_hour:
            occupation_hours_restaurants[first_hour] =occupation_hours_restaurants[first_hour] +1
            first_hour += 1

    occupation_hours_restaurants = occupation_hours_restaurants[5:25]

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time,
        space_id__classification = 2
    )

    for space in occupied_spaces:
        first_hour = int(space.occupied_at.hour)
        last_hour = int(space.unoccupied_at.hour)
        while first_hour <=last_hour:
            occupation_hours_relax[first_hour] =occupation_hours_relax[first_hour] +1
            first_hour += 1
    occupation_hours_relax = occupation_hours_relax[5:25]

    hours = []
    for i in range(5,24):
        hours.append(str(i))

    colors = {
        "Restaurantes": "blue",
        "Zonas de Descanso": "purple",
        "Zonas Deportivas": "green"
    }

    fig, ax = plt.subplots()
    ax.plot(hours, occupation_hours_restaurants, marker='o', linestyle='-', color=colors["Restaurantes"], label='Restaurantes')
    ax.plot(hours, occupation_hours_relax, marker='o', linestyle='-', color=colors["Zonas de Descanso"], label='Zonas de Descanso')
    ax.plot(hours, occupation_hours_sports, marker='o', linestyle='-', color=colors["Zonas Deportivas"], label='Zonas Deportivas')
    ax.set_xlabel("Horas")
    ax.set_ylabel("Ocupación")
    ax.set_title("Ocupación por día y Categoría")

    buffer = BytesIO()
    plt.savefig(buffer, format='png') 
    plt.savefig("media/occupation_by_day")

    buffer.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64

        
def occupation_by_hours(dat):
    date = str(dat)
    date = datetime.strptime(date, "%Y-%m-%d")
    occupation_hours = [0]*24
    start_time = datetime(year=date.year, month=date.month, day=date.day, hour=5, minute=0, second=0)
    end_time = start_time + timedelta(hours=19)

    occupied_spaces = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
        occupied_at__lt=end_time
    )

    for space in occupied_spaces:
        first_hour = int(space.occupied_at.hour)
        last_hour = int(space.unoccupied_at.hour)
        while first_hour <=last_hour:
            occupation_hours[first_hour] =occupation_hours[first_hour] +1
            first_hour += 1

    occupation_hours = occupation_hours[5:25]
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
    plt.savefig('media/occupation_by_hours.png')
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


def most_used_space(type_space, start_time, top=5):
    date = str(start_time)
    date = datetime.strptime(date, "%Y-%m-%d")
    most_used_space_ids = OcuppiedSpace.objects.filter(
        occupied_at__gte=start_time,
    ).values('space_id').annotate(
        total_hours=Coalesce(Sum(F('unoccupied_at') - F('occupied_at')), timedelta(seconds=0))
    ).order_by('-total_hours')[:top]

    most_used_spaces = Space.objects.filter(id__in=[item['space_id'] for item in most_used_space_ids], classification=type_space).order_by('id')
    space_hours = defaultdict(float)

    for item in most_used_space_ids:
        space_id = item['space_id']
        total_hours = item['total_hours'].total_seconds() / 3600
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
    
    if type_space == 0:
        plt.title('Espacios deportivos')
        plt.savefig(buffer, format='png')
        plt.savefig("media/most_used_sports")
    elif type_space == 1:
        plt.title('Mesas de restaurantes')
        plt.savefig(buffer, format='png')
        plt.savefig("media/most_used_restaurants")
    else:
        plt.title('Zonas de descanso')
        plt.savefig(buffer, format='png')
        plt.savefig("media/most_used_relax")

    buffer.seek(0)
    plt.close()
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def get_common_context(request):
    if request.method == 'POST':
        user_date = request.POST.get('start_date', None)
        if user_date is not None and len(user_date) > 2:
            start_date = user_date.replace('/', '-')
        else:
            start_date = datetime.now().date()

    else:
        start_date = datetime.now().date()

    spaces = OcuppiedSpace.objects.all()
    myFilter = OccupiedSpaceFilter(request.GET, queryset=spaces)

    if 'start' in request.GET and 'end' in request.GET:
        start_date1 = request.GET['start']
        end_date1 = request.GET['end']
        if len(start_date1) > 1 and len(end_date1) > 1:
            spaces = myFilter.qs
            spaces = spaces.filter(occupied_at__gte=start_date1, occupied_at__lte=end_date1)
        else:
            spaces = None

    else:
        spaces = None

    currents = current_occupation()
    common_context = {
        'current_occupation_sports': currents[0],
        'current_occupation_restaurants': currents[1],
        'current_occupation_relax': currents[2],
        'most_used_sports': most_used_space(0, start_date),
        'most_used_restaurants': most_used_space(1, start_date),
        'most_used_relax': most_used_space(2, start_date),
        'current_graph_sports': occupancy(20, currents[0]),
        'current_graph_restaurants': occupancy(500, currents[1]),
        'current_graph_relax': occupancy(80, currents[2]),
        'occupation_by_hours': occupation_by_hours(start_date),
        'occupation_by_year': occupation_by_year(start_date),
        'occupation_by_month': occupancy_by_months(start_date),
        'occupation_by_day': occupation_by_day(start_date),
        'spaces': spaces,
        'filter_date': start_date,
        'filter': myFilter,
    }
    
    return common_context


def gen_pdf(request):
    common_context = get_common_context(request)
    template = get_template('pdf_gen.html')
    html = template.render(common_context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="informe.pdf"'
        return response
    
    return HttpResponse('Error al generar el PDF: %s' % pdf.err)


def info(request):
    common_context = get_common_context(request)
    return render(request, 'data.html', common_context)