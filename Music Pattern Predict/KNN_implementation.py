# this function calculates the k nearest neighbors of 'point' which is a n-tuple and playlist is a list of tuples 
def getKnearest(point, playlist, dist_fn, k):
	distances = [(dist_fn(playlist[i], point), i) for i in len(playlist)]
	distances = sorted(distances, reverse=False)
	KNN_indices_distances = distances[:k]
	return KNN_indices_distances

#eazy to compute and was making more sense xD
def Euc_dis(point1, point2):
	dis = 0
	for i in length(point2):
		dis += abs(point2[i]-point1[i])
	return dis


def driver(playlist, point, k):
	nearest_list = getKnearest(point,playlist,Euc_dis,k)
	nearest_indices = map(lambda x: x[1],nearest_list)
	return nearest_indices