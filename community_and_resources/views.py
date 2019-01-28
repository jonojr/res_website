from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import RST, Points


def index(request):
    return render(request, 'community_overview.html')


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
        {'rst': rst, 'CH':CH, 'DCH':DCH, 'RSA':RSA,}
    )


def bio(request, RST_pk):
    person = get_object_or_404(RST, pk=RST_pk)
    return render(request, 'bio_page.html', {'person': person})


def total_points(request):
    all_points = Points.objects.all()
    first = 0
    second = 0
    third = 0
    fourth = 0
    print('Gathering points')
    for points in all_points:
        first += points.first_floor
        second += points.second_floor
        third += points.third_floor
        fourth += points.fourth_floor
    print(first, second, third, fourth)
    return JsonResponse(
        {
            'first': first,
            'second': second,
            'third': third,
            'fourth': fourth,
         }
    )


def point_results(request):
    data = serializers.serialize("json", Points.objects.all())
    return JsonResponse(data, safe=False)


def point_detail(request):
    return render(request, 'points_details.html')
