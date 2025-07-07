from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from django.http import JsonResponse # type: ignore
import requests # type: ignore
from dotenv import load_dotenv # type: ignore
import json # type: ignore
import os # type: ignore
import genshinstats as gs # type: ignore
load_dotenv()

@csrf_exempt
def get_stats(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            uid = data.get('uid')
            ltcookie = os.getenv('API_COOKIE')
            ltuid = os.getenv('LTUID')
            gs.set_cookie(ltuid=ltuid, ltoken=ltcookie)
            player_stats = gs.get_user_stats(uid)
            num_characters = len(player_stats['characters'])
            achievements = player_stats['achievements']
            world_level = player_stats['world_level']
            ar = player_stats['adventure_rank']
            return JsonResponse({
                'name': player_stats['nickname'],
                'world_level': world_level,
                'achievements': achievements,
                'num_characters': num_characters,
                'adventure_rank': ar,
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=405)
