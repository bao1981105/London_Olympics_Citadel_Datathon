import math
from heapq import heappush, heappop

olympics_locations_dict = {'earls court': [51.492483, -0.199686],
        'eton dorney': [51.493908, -0.663455],
        'excel': [51.507218, 0.030504],
        'greenwich park': [51.476958, 0.001483],
        'hadleigh farm': [51.552378, 0.597948],
        'horse guards parade': [51.504798, -0.12838],
        'hyde park': [51.508196, -0.165699],
        'lee valley white water centre': [51.688963, -0.017208],
        "lord's": [51.529934, -0.172178],
        'north greenwich arena': [51.503126, 0.003191],
        'olympic park': [51.54343, -0.016627],
        'royal artillery barracks': [51.487557, 0.059606],
        'the mall': [51.504581, -0.13436],
        'wembley arena': [51.558196, -0.282597],
        'wembley stadium': [51.556067, -0.279519],
        'wimbledon': [51.419528, -0.220417]}

def aerialDist(lat1,lon1,lat2,lon2):

  r = 6371e3
  theta1 = lat1 * math.pi/180
  theta2 = lat2 * math.pi/180

  delta = (lon2 - lon1) * math.pi/180
  d = math.acos(math.sin(theta1) * math.sin(theta2)  + math.cos(theta1) * math.cos(theta2) * math.cos(delta)) * r
  
  return round(d/1000,2)


def findKNN(venue_coords, k):
  heap = []
  latitude, longitude = venue_coords

  for venue in olympics_locations_dict.keys():
    venue_lat = olympics_locations_dict[venue][0]
    venue_long = olympics_locations_dict[venue][1]
    distance = aerialDist(latitude, longitude, venue_lat, venue_long)

    if len(heap) == k:
      if -distance >= heap[0][0]:
        heappop(heap)
        heappush(heap, (-distance, [venue_lat, venue_long]))
    else:
      heappush(heap, (-distance, [venue_lat, venue_long]))
  
  return [-distance for distance, coords in heap]


def getOlympicDistance(row, k):
  latitude = row['Latitude']
  longitude = row['Longitude']

  NN = findKNN([latitude, longitude], k)

  return sum(NN) / k
