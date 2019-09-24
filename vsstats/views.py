import datetime

from django.contrib.auth import get_user
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Source
from . import stats


def index(request):
    sources = Source.objects.all().order_by('source_type', 'name')

    return render(request, 'vsstats/index.html', context={
        'sources': sources
    })


@login_required
def sources(request, source_id):
    source = Source.objects.get(pk=source_id)
    return render(request, 'vsstats/sources.html', context={
        'name': source.name
    })


def api_stats(request, source_id):
    user = get_user(request)
    if user is None or user.is_anonymous:
        return JsonResponse({'error': 'AUTH_REQUIRED'}, status=401)

    data = request.GET
    if 'begin' in data and 'end' in data:
        begin = datetime.date.fromisoformat(data['begin'])
        end = datetime.date.fromisoformat(data['end'])
    else:
        today = datetime.date.today()
        begin = datetime.date(today.year, today.month, 1)
        end = datetime.date.today() + datetime.timedelta(days=1)

    source = Source.objects.get(pk=source_id)
    if source.source_type == Source.TYPES[0][0]:
        data = stats.stats_api(source.url, begin, end)
    elif source.source_type == Source.TYPES[1][0]:
        data = stats.stats_tg(source.url, begin, end)
    else:
        raise JsonResponse({'error': 'Not found'}, status=404)

    return JsonResponse({
        'id': source.id,
        'name': source.name,
        'type': source.source_type,
        'stats': data,
        'begin': begin,
        'end': end
    })
