from googleapiclient.discovery import build




api_key = "AIzaSyDXX4qalTWg8L9-Fj74Xb_KLdhuRhQH1JY"

youtube = build('youtube', 'v3', developerKey=api_key)

'''request_cat_found = youtube.videoCategories().list(
    part='snippet', id=20,)


execute_cat = request_cat_found.execute()

cat_id = int(execute_cat['items'][0]['id'])'''

length = 0

nextPageToken = None
while True:


    request_find_a_video = youtube.videos().list(
        part='statistics' , maxResults=200, videoCategoryId='1',chart='mostPopular', pageToken=nextPageToken

    
    )




    execute_video_cat = request_find_a_video.execute()

    video_count_total = 0
    like_count_total = 0
    statistics = execute_video_cat['items']
    length += len(statistics)

    for video in statistics:
        view_count = video['statistics']['viewCount']

        video_count_total += int(view_count)
        like_count = video['statistics']['likeCount']
        like_count_total += int(like_count)

    print()
    print(video_count_total)
    print(like_count_total)

    nextPageToken = execute_video_cat.get('nextPageToken')
    if nextPageToken == None:
        break



print(length)







'''request_find_channel = youtube.channels().list(
    part='contentDetails' , id=channel_id)

execute_channel = request_find_channel.execute()

channel_uploads = execute_channel["items"][0]['contentDetails']['relatedPlaylists']['uploads']

request_find_upload = youtube.playlists().list(
    part='contentDetails' , id=channel_uploads)

execute_upload = request_find_upload.execute()

cat_playlist_id = execute_upload['items'][0]['id']


request_playlist_found = youtube.playlistItems().list(
part='contentDetails', playlistId=cat_playlist_id, maxResults=4)

playlist_cat = request_playlist_found.execute()

second_video_id_using_index = playlist_cat['items'][3]['contentDetails']['videoId']




request_find_a_video = youtube.videos().list(
    part='snippet' , id=
second_video_id_using_index)

video_found = request_find_a_video.execute()

print(video_found['items'][0]['id'])'''