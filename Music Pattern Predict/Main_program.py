import numpy as np
import pandas as pd

dataset=pd.read_csv('Cleaned_Input.csv')
Cols = list(dataset.columns)
X=dataset.iloc[:,1:].values
y=dataset.iloc[:,0:1].values

#Songs is the old songs in the history of the person that we use to classify this new song(indices) 
#data is the list of songs(not the name of songs, the coefficients)
#artist is the artist of the song coz the artist shall not depend on the history right
#The artist is a number, representing the column of the artist in the data
#Song_Names is the list of song names(As the user searches via names)
def get_coorrds(Name_of_new_Song, Songs, data, artist, Song_Names, timestamp):
	new_song, narr = np.zeros([1,len(data[0])]), np.array([Name_of_new_Song], dtype=str)
	for i in range(4):
		#List all the values for a particular emotion
		L = [data[j][i] for j in Songs]
		new_song[0,i] = sum(L)/len(L)

	#making the index of artist 1
  
	new_song[0,artist], new_song[0,timestamp]=1,1

	#append the new song to the data
  
	data = np.concatenate((data, new_song))
	#Since the user searches for a new song by name
  
	Song_Names = np.append(Song_Names, narr)
	return new_song


#this function is to update the data
def update(X, song1, s2):
    alpha= 0.01
    s1 = np.where(X==song1)
    for i in range(0, 4): 
        X[s2][i] = X[s2][i] + alpha*(X[s2][i] - X[s1][i])

# this function calculates the k nearest neighbors of 'point' which is a n-tuple and playlist is a list of tuples 
def getKnearest(point, playlist, dist_fn, k):
	distances = [(dist_fn(playlist[j], point), j) for j in range(0,len(playlist))]
	distances = sorted(distances, reverse=False)
	KNN_indices_distances = distances[:k]
	return KNN_indices_distances

#eazy to compute and was making more sense xD
def Euc_dis(point1, point2):
	dis = 0
	for i in range(len(point2)):
		dis += abs(point2[i]-point1[i])
	return dis


def driver(playlist, point, k):
	nearest_list = getKnearest(point,playlist,Euc_dis,k)
	nearest_indices = list(map(lambda x: x[1],nearest_list))
	return nearest_indices

def suggest(X,y,point,j):
    next_songs=driver(X,point,60)
    
    for i in range(60):
      if next_songs[i] not in played and next_songs[i] not in skipped:
        suggestion = next_songs[i]
        break
    print("Would you like to play this song next ?")
    print("1: ",y[suggestion])
    print("2:   Skip")
    print("3:   Search")
    print("4:   Exit")
    print("5:   Introduce New Song")
    
    return suggestion   
def search():
    print("Select the Song")
    for i in range(60):
        print(i+1,y[i])
search()   
number_of_suggestions = 0
number_of_skipped = 0 
played = []
skipped = []    
x=int(input())
t=0
prev_song=[X[x-1]]
l=suggest(X,y,prev_song[len(prev_song)-1],t)
number_of_suggestions += 1
played.append(x-1)
while(len(prev_song)<5):
    
    x=int(input())
    if(x==1):
        prev_song.append(X[l])
        played.append(l)
        t=0
        l=suggest(X,y,prev_song[len(prev_song)-1],t)
        number_of_suggestions +=1
    if(x==2):
        t=t+1
        skipped.append(l)
        number_of_skipped += 1
        update(X, prev_song[len(prev_song)-1], l)
        l=suggest(X,y,prev_song[len(prev_song)-1],t)
        number_of_suggestions += 1
      
    if(x==3):
        search()
    if(x==4):
      break
    if(x==5):
      Name_of_New_Song = str(input("Enter name of new song"))
      artist = 'Artist_' + str(input("enter name of artist"))
      timestmp = 'Timestamp_'+str(input("TimeStamp of song"))
      artist_ind = Cols.index(artist)-1
      time_ind = Cols.index(timestmp)-1
      get_coorrds(Name_of_New_Song, played, X, artist_ind, y, time_ind)
      print("Song Added")

        
while(x!=4):
  k = len(prev_song)

  point=prev_song[k-1]*0.5+ prev_song[k-2]*0.25+ prev_song[k-3]*0.15+ prev_song[k-4]*0.05+ prev_song[k-5]*0.05
  l=suggest(X,y,point,t)
  number_of_suggestions +=1
  x=int(input())
  if(x==1):
      prev_song.append(X[l])
      played.append(l)
      if len(played)>10:
        played.remove(played[0])
      t=0
  if(x==2):
      skipped.append(l)
      number_of_skipped += 1
      update(X, prev_song[len(prev_song)-1], l)
      t=t+1
  if(x==3):
      search()
  if(x==5):
      Name_of_New_Song = str(input("Enter name of new song"))
      artist = 'Artist_' + str(input("enter name of artist"))
      timestmp = 'Timestamp_'+str(input("TimeStamp of song"))
      artist_ind = Cols.index(artist)-1
      time_ind = Cols.index(timestmp)-1
      get_coorrds(Name_of_New_Song, played, X, artist_ind, y, time_ind)
      print("Song Added")

                      
print("The accuracy of the model was", 1.0 - float(number_of_skipped/number_of_suggestions))              
                
        
    
