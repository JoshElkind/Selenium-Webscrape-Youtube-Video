from googleapiclient.discovery import build
import re
from datetime import timedelta


def ConvertToAllTime(total_seconds):
    seconds_left1 = total_seconds
    list_time1 = []
    sorted_list = []
    taged_list = []
    list_time1.append(seconds_left1)
    if seconds_left1/60 >= 1:
        list_time1[0] = seconds_left1 % 60
        remain = seconds_left1 % 60
        even_division = seconds_left1 - remain
        even_divide_complete = even_division/60
        list_time1.append(even_divide_complete)

        if list_time1[1]/60 >= 1:
            remain_hours = list_time1[1]%60
            even_division2 = list_time1[1] - remain_hours
            list_time1.append(even_division2/60)
            list_time1[1] = remain_hours
        
        else:
            pass

        if len(list_time1) == 2:
            sorted_list.append(int(list_time1[1]))
            sorted_list.append(int(list_time1[0]))

        else:
            sorted_list.append(int(list_time1[2]))
            sorted_list.append(int(list_time1[1]))
            sorted_list.append(int(list_time1[0]))

        if len(sorted_list) == 2:
            if sorted_list[0] > 1:
                tag = str(sorted_list[0]) + " minutes"
                taged_list.append(tag)
            else:
                tag = str(sorted_list[0]) + " minute"
                taged_list.append(tag)

            if sorted_list[1] > 1:
                tag = str(sorted_list[1]) + " seconds"
                taged_list.append(tag)

            elif sorted_list[1] == 0:
                pass
            else:
                tag = str(sorted_list[1]) + " second"
                taged_list.append(tag)

            if len(taged_list) == 1:
                print("The playlist will end in " + taged_list[0] + ".")
            else:
                print("The playlist will end in " + taged_list[0] + " and " + taged_list[1] + "." )
        
        else:

            if sorted_list[0] > 1:
                tag = str(sorted_list[0]) + " hours"
                taged_list.append(tag)
            
            elif sorted_list[0] == 0:
                pass

            else:
                tag = str(sorted_list[0]) + " hour"
                taged_list.append(tag)

            if sorted_list[1] > 1:
                tag = str(sorted_list[1]) + " minutes"
                taged_list.append(tag)
            else:
                tag = str(sorted_list[1]) + " minute"
                taged_list.append(tag)

            if sorted_list[2] > 1:
                tag = str(sorted_list[2]) + " seconds"
                taged_list.append(tag)

            elif sorted_list[2] == 0:
                pass
            else:
                tag = str(sorted_list[2]) + " second"
                taged_list.append(tag)

            if len(taged_list) == 1:
                print("The playlist will end in " + taged_list[0] + ".")
            
            elif len(taged_list) == 2:
                print("The playlist will end in " + taged_list[0] + " and " + taged_list[1] + ".")

            else:
                print("The playlist will end in " + taged_list[0] + ", " + taged_list[1] + " and " + taged_list[2] + ".")


    else:
        print('There are ' + seconds_left1 + ' seconds left in the playlist.')

total_seconds = 0

api_key = "AIzaSyDXX4qalTWg8L9-Fj74Xb_KLdhuRhQH1JY"

youtube = build('youtube', 'v3', developerKey=api_key)

'''request_find_channel = youtube.channels().list(
    part='contentDetails' , forUsername='schafer5')

response = request_find_channel.execute()
id_channel = response['items'][0]['id']
return(id_channel)

request_cl_found = youtube.playlists().list(
    part='contentDetails, snippet', channelId=id_channel)

cl_found = request_cl_found.execute()

return(cl_found)'''

h_pa = re.compile(r'(\d+)H')
min_pa = re.compile(r'(\d+)M')
sec_pa = re.compile(r'(\d+)S')

nextPageToken = None
while True:

    request_playlist_found = youtube.playlistItems().list(
    part='contentDetails', playlistId='PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p', maxResults=50, pageToken=nextPageToken)

    play_found = request_playlist_found.execute()
    vid_ids = []
    for items in play_found['items']:
        viv_id = items['contentDetails']['videoId']
        vid_ids.append(viv_id)


    vid_request = youtube.videos().list(

        part="contentDetails",
        id=','.join(vid_ids)

    )

    vid_response = vid_request.execute()
   


    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = h_pa.search(duration)
        minutes = min_pa.search(duration)
        seconds = sec_pa.search(duration)
        
        # if x else 0 is a teranery conditional. if part says if it has a value and else says if it doesn't have a value.
        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1))  if seconds else 0

        video_seconds = timedelta(
            hours = hours,
            minutes = minutes,
            seconds = seconds
        ).total_seconds()

        total_seconds += video_seconds
        

    nextPageToken = play_found.get('nextPageToken')

    if not nextPageToken:
        break

ConvertToAllTime(total_seconds)



###We do this loop because the playlist can have many pages of videos
###For every round of the loop, at the end, it references the nextpage (nextPageToken)
###This way, at the end of the loop we can check if the nextpagetoken changes
###If the nextpagetoken changes, we continue with the loop and add total seconds of videos in that page again
###If it doesn't change, then we know there aren't any new pages that we need to proccess and we end the loop



