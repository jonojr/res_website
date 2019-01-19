from django.shortcuts import get_object_or_404, render
from .models import RST


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