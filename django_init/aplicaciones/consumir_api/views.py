from django.shortcuts import render
import requests

def inicio(request):
    return render(request, 'inicio.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        character = []
        offset = 10
        print(searched)
        if searched:
            url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + str(searched).replace(' ', '+')
            character += requests.get(url).json()
            if len(character) == 10:
                while (len(character) >= 10):
                    url2 = url + '&offset=' + str(offset)
                    new_char = requests.get(url2).json()
                    if len(new_char) < 10:
                        character += new_char
                        break
                    else:
                        character += new_char
                        offset += 10
        else:
            url = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?'
            character += requests.get(url).json()
            if len(character) == 10:
                while (len(character) >= 10):
                    url2 = url + '&offset=' + str(offset)
                    new_char = requests.get(url2).json()
                    if len(new_char) < 10:
                        character += new_char
                        break
                    else:
                        character += new_char
                        offset += 10
        return render(request, 'search.html', {'character': character})


def seasons_bb(request):
    season = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    cantidad_season = 0
    numero_season = []
    seasons_actuales = []
    for x in season:
        if x['season'] in numero_season:
            pass
        else:
            cantidad_season += 1
            numero_season.append(x['season'])
            variables_aux = {'season': 'Temporada ' + x['season'], 'value': x['season']}
            seasons_actuales.append(variables_aux) 
    print(seasons_actuales)
    return render(request, 'seasons_bb.html', {'seasons_actuales':seasons_actuales})

def seasons_bcs(request):
    
    season = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    cantidad_season = 0
    numero_season = []
    seasons_actuales = []
    for x in season:
        if x['season'] in numero_season:
            pass
        else:
            cantidad_season += 1
            numero_season.append(x['season'])
            variables_aux = {'season': 'Temporada ' + x['season'], 'value': x['season']}
            seasons_actuales.append(variables_aux) 
    print(seasons_actuales)
    return render(request, 'seasons_bcs.html', {'seasons_actuales':seasons_actuales})

def episodes_breaking_bad(request, id):
    season = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    season_one = []
    for x in season:
        episode = {}
        if x['season'] == str(id):
            episode['episode_id'] = x['episode_id']
            episode['episode'] = x['episode']
            episode['title'] = x['title']
            season_one.append(episode)
    temporada = 'Temporada ' + str(id)
    print(season_one)
    return render(request, 'episodes_breaking_bad.html', {'season_one':season_one, 'temporada': temporada})

def episodes_better_call_soul(request, id):
    season = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    season_one = []
    for x in season:
        episode = {}
        if x['season'] == str(id):
            episode['episode_id'] = x['episode_id']
            episode['episode'] = x['episode']
            episode['title'] = x['title']
            season_one.append(episode)
    temporada = 'Temporada ' + str(id)
    print(season_one)
    return render(request, 'episodes_better_call_saul.html', {'season_one':season_one, 'temporada': temporada})

def episodes(request, episode_id):
    url = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/' + str(episode_id)
    episode = requests.get(url).json()

    return render(request, 'detalle_episode.html', {'episode': episode})
    
def characters(request, character):
    nombre_char = character.replace(' ','+')
    url1 = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=' + nombre_char
    detalle_char = requests.get(url1).json()
    print(nombre_char)
    list_temp = detalle_char[0]['appearance']
    season = []
    for x in list_temp:
        dic_aux = {}
        dic_aux['season'] = 'Temporada ' + str(x)
        dic_aux['id_season'] = x
        season.append(dic_aux)
    detalle_char[0]['appearance'] = season
    list_temp_bcs = detalle_char[0]['better_call_saul_appearance']
    season_bcs = []
    for s in list_temp_bcs:
        dic_aux = {}
        dic_aux['season_bcs'] = 'Temporada ' + str(s)
        dic_aux['id_season'] = s
        season_bcs.append(dic_aux)
    detalle_char[0]['better_call_saul_appearance'] = season_bcs
    url2 = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=' + nombre_char
    quotes = requests.get(url2).json()
    if quotes == []:
        quotes = [{'quote_id': 0, 'quote': 'El personaje no tiene citas'}]
    detalle_char[0]['quotes'] = quotes
    return render(request, 'characters.html', {'detalle_char':detalle_char})