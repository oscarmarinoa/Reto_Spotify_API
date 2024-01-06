# Importamos las librerias necesarias.
import json
import pandas as pd

# Diccionario de datos.
dict_taylor = {'disc_number': [], 'duration_ms': [], 'explicit': [], 'track_number': [],
               'track_popularity': [], 'track_id': [], 'track_name': [],
               'audio_features.danceability': [], 'audio_features.energy': [],
               'audio_features.key': [], 'audio_features.loudness': [],
               'audio_features.mode': [], 'audio_features.speechiness': [],
               'audio_features.acousticness': [], 'audio_features.instrumentalness': [],
               'audio_features.liveness': [], 'audio_features.valence': [],
               'audio_features.tempo': [], 'audio_features.id': [],
               'audio_features.time_signature': [], 'artist_id': [],
               'artist_name': [], 'artist_popularity': [], 'album_id': [],
               'album_name': [], 'album_release_date': [], 'album_total_tracks': []}

# Funciones para el procesamiento de subdiccionarios en el archivo taylor_swift_spotify.json

def process_subdicts_internos(data_disc):
    for sub_dict in  data_disc.keys():
        if isinstance(data_disc[sub_dict], (dict, list)):
            process_subdicts_internos(data_disc[sub_dict])
        else:
            try:
                dict_taylor[sub_dict].append(data_disc[sub_dict])
            except:
                auxiliar = 'audio_features.' + sub_dict
                dict_taylor[auxiliar].append(data_disc[sub_dict])


def process_subdict_track(data_track, value_4, value_5, value_6, value_7):
    for dict_no_in_track in range(len(data_track)):
        dict_taylor['artist_id'].append(value_1)
        dict_taylor['artist_name'].append(value_2)
        dict_taylor['artist_popularity'].append(value_3)
        dict_taylor['album_id'].append(value_4)
        dict_taylor['album_name'].append(value_5)
        dict_taylor['album_release_date'].append(value_6)
        dict_taylor['album_total_tracks'].append(value_7)
    
        process_subdicts_internos(data_track[dict_no_in_track])

# Código principal
def run():
    
    f = open(r'taylor_swift_spotify.json')
    data = json.load(f)
    
    
    for caracteristica in data.keys():
        if caracteristica == 'artist_id': 
            global value_1 
            value_1 = data[caracteristica]
        elif caracteristica == 'artist_name': 
            global value_2 
            value_2 = data[caracteristica]
        elif caracteristica == 'artist_popularity': 
            global value_3 
            value_3 = data[caracteristica]
        
        if isinstance(data[caracteristica], (dict, list)):
            for dict_no_x in range(len(data[caracteristica])):
                for sub_dict in data[caracteristica][dict_no_x].keys():
                    if      sub_dict == 'album_id': value_4 = data[caracteristica][dict_no_x][sub_dict]
                    elif    sub_dict == 'album_name': value_5 = data[caracteristica][dict_no_x][sub_dict]
                    elif    sub_dict == 'album_release_date': value_6 = data[caracteristica][dict_no_x][sub_dict]
                    elif    sub_dict == 'album_total_tracks': value_7 = data[caracteristica][dict_no_x][sub_dict]
                    
                    if isinstance(data[caracteristica][dict_no_x][sub_dict], (dict, list)):
                        process_subdict_track(data[caracteristica][dict_no_x][sub_dict], value_4, value_5, value_6, value_7)
                        
    df = pd.DataFrame(dict_taylor)
    df.to_csv('Dataset_om.csv', index=False)


if __name__ == "__main__":
    run()