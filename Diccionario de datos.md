# Diccionario de datos:
Explicación detallada del contenido de los datos y su formato. 

##### Dataset:
 | **Característica** | **Descripción** | **Formato** | **Observación** |
 | --- | --- | --- | --- |
 | **_disc_number_**| The disc number (usually 1 unless the album consists of more than one disc). | integer | <sub>N/A</sub> |
 | **_duration_ms_** | The duration of the track in milliseconds. | integer | |
 | **_explicit_** | Whether or not the track has explicit lyrics ( true = yes it does; false = no it does not OR unknown). | boolean | <sub>N/A</sub> |
 | **_track_number_** | The number of the track. If an album has several discs, the track number is the number on the specified disc. | integer | <sub>N/A</sub> |
 | **_track_popularity_** | The popularity of the track. The value will be between 0 and 100, with 100 being the most popular. | integer | <sub>N/A</sub> |
 | **_track_id_** | The Spotify ID for the track. | string | <sub>N/A</sub> | 
 | **_track_name_** | The name of the track. | string | <sub>N/A</sub> |
 | **_audio_features.danceability_** | how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. | number [float] | Range: 0 - 1 |
 | **_audio_features.energy_** | Represents a perceptual measure of intensity and activity. | number [float] | Range: 0 - 1 |
 | **_audio_features.key_** | The key the track is in. If no key was detected, the value is -1.| integer | Range: -1 - 11 |
 | **_audio_features.loudness_** | The overall loudness of a track in decibels (dB). | number [float] | Values typically range: between -60 and 0 db.|
 | **_audio_features.mode_** | indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. | integer | <sub>N/A</sub> |
 | **_audio_features.speechiness_** | Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. | number [float] | <sub>N/A</sub> |
 | **_audio_features.acousticness_** | A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. | number [float] | Range: 0 - 1 |
 | **_audio_features.instrumentalness_** | Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. | number [float] | Range: 0 - 1 |
 | **_audio_features.liveness_** | Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. | number [float] | <sub>N/A</sub> |
 | **_audio_features.valence_** | A measure describing the musical positiveness conveyed by a track. | number [float] | Range: 0 - 1 |
 | **_audio_features.tempo_** | The overall estimated tempo of a track in beats per minute (BPM). | number [float] | <sub>N/A</sub> |
 | **_audio_features.id_** | The Spotify ID for the track. | string | <sub>N/A</sub> |
 | **_audio_features.time_signature_** | An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). | integer | Range: 3 - 7 |
 | **_artist_id_** | The Spotify ID for the artist. | string | <sub>N/A</sub> |
 | **_artist_name_** | The name of the artist. | string | <sub>N/A</sub> |
 | **_artist_popularity_** | The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. | integer | Range: 0 - 100 |
 | **_album_id_** | The Spotify ID for the album. | string | <sub>N/A</sub> |
 | **_album_name_** | The name of the album. In case of an album takedown, the value may be an empty string. | string | <sub>N/A</sub> |
 | **_album_release_date_** | The precision with which release_date value is known. | string | <sub>N/A</sub> |
 | **_album_total_track_** | The number of tracks in the album. | integer | <sub>N/A</sub> | 

  * <sub>N/A: No aplica</sub>