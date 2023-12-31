# Diccionario de datos:
Explicación detallada del contenido de los datos y su formato. 

##### Dataset:
 | **Característica** | **Descripción** | **Formato** | **Observación** |
 | --- | --- | --- | --- |
 | **_ disc_number _**| 
 | **_duration_ms_** | The duration of the track in milliseconds. | integer | |
 | **_explicit_** |
 | **_track_number_** |
 | **_track_popularity_** |
 | **_track_id_** | The Spotify ID for the track. | string | | 
 | **_track_name_** |
 | **_audio_features.danceability_** | how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. | number [float] | Range: 0 - 1 |
 | **_audio_features.energy_** | Represents a perceptual measure of intensity and activity. | number [float] | Range: 0 - 1 |
 | **_audio_features.key_** | The key the track is in. If no key was detected, the value is -1.| integer | Range: -1 - 11 |
 | **_audio_features.loudness_** | The overall loudness of a track in decibels (dB). | number [float] | Values typically range: between -60 and 0 db.|
 | **_audio_features.mode_** | indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.   
 | **_audio_features.speechiness_** | Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. | number [float] | |
 | **_audio_features.acousticness_** | A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. | number [float] | Range: 0 - 1 |
 | **_audio_features.instrumentalness_** | Predicts whether a track contains no vocals. | The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. | number [float] | Range: 0 - 1 |
 | **_audio_features.liveness_** | Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. | number [float] | |
 | **_audio_features.valence_** | A measure describing the musical positiveness conveyed by a track. | number [float] | Range: 0 - 1 |
 | **_audio_features.tempo_** | The overall estimated tempo of a track in beats per minute (BPM). | number [float] | |
 | **_audio_features.id_** |
 | **_audio_features.time_signature_** | An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). | integer | Range: 3 - 7 |
 | **_artist_id_** |
 | **_artist_name_** |
 | **_artist_popularity_** |
 | **_album_id_** |
 | **_album_name_** |
 | **_album_release_date_** |
 | **_album_total_track_**s |