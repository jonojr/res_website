from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import RST, Points


def login(request):
    return redirect('/login/google-oauth2/')

@login_required
def index(request):
    return render(request, 'community_overview.html')

@login_required
def community(request):
    return render(request, 'community.html')


def resources(request):
    rst = RST.objects.order_by('wing').filter(position__exact='RA')
    try:
        CH = RST.objects.get(position='CH')
    except RST.DoesNotExist:
        CH = None
    try:
        DCH = RST.objects.get(position='DCH')
    except RST.DoesNotExist:
        DCH = None
    try:
        RSA = RST.objects.get(position='RSA')
    except RST.DoesNotExist:
        RSA = None

    return render(
        request,
        'resources.html',
        {'rst': rst, 'CH': CH, 'DCH': DCH, 'RSA': RSA, }
    )


def bio(request, RST_pk):
    person = get_object_or_404(RST, pk=RST_pk)
    return render(request, 'bio_page.html', {'person': person})


def total_points(request):
    all_points = Points.objects.all()
    first_east = 0
    first_west = 0
    second_east = 0
    second_west = 0
    third_east = 0
    third_west = 0
    fourth_east = 0
    fourth_west = 0

    print('Gathering points')
    for points in all_points:
        first_east += points.first_east
        first_west += points.first_west
        second_east += points.second_east
        second_west += points.second_west
        third_east += points.third_east
        third_west += points.third_west
        fourth_east += points.fourth_east
        fourth_west += points.fourth_west

    return JsonResponse(
        {
            'FirstE': first_east,
            'FirstW': first_west,
            'SecondE': second_east,
            'SecondW': second_west,
            'ThirdE':third_east,
            'ThirdW':third_west,
            'FourthE':fourth_east,
            'FourthW':fourth_west,
         }
    )


def point_results(request):
    all_points = Points.objects.all()
    lables = ['Move In']
    first_east = [0]
    first_west = [0]
    second_east = [0]
    second_west = [0]
    third_east = [0]
    third_west = [0]
    fourth_east = [0]
    fourth_west = [0]

    for point in all_points:
        lables.append(point.event_name)
        first_east.append(first_east[-1] + point.first_east)
        first_west.append(first_west[-1] + point.first_west)

        second_east.append(second_east[-1] + point.second_east)
        second_west.append(second_west[-1] + point.second_west)

        second_east.append(second_east[-1] + point.second_east)
        second_west.append(second_west[-1] + point.second_west)

        third_east.append(third_east[-1] + point.third_east)
        third_west.append(third_west[-1] + point.third_west)

        fourth_east.append(fourth_east[-1] + point.fourth_east)
        fourth_west.append(fourth_west[-1] + point.fourth_west)

    data = {'labels': lables, 'first_east': first_east, 'first_west': first_west, 'second_east': second_east, 'second_west': second_west, 'third_east': third_east, 'third_west': third_west, 'fourth_east': fourth_east, 'fourth_west': fourth_west,}
    return JsonResponse(data)


def point_detail(request):
    return render(request, 'points_details.html')
