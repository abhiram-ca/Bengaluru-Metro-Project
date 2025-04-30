import numpy as np
import heapq

stationsg = [
    "Madavara", "Chikkabidarakallu", "Manjunathanagara", "Nagasandra",
    "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya",
    "Goraguntepalya", "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi",
    "Rajajinagara", "Mahakavi Kuvempu Road", "Srirampura", "Mantri Square Sampige Road",
    "Nadaprabhu Kempegowda Station, Majestic", "Chikkapete", "Krishna Rajendra Market",
    "National College", "Lalbagh", "South End Circle", "Jayanagara",
    "Rashtreeya Vidyalaya Road", "Banashankari", "Jayaprakash Nagara", "Yelachenahalli",
    "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute"
]

stationsp = [
    "Whitefield", "Hopefarm Channasandra", "Kadugodi Tree Park", "Pattanduru Agrahara",
    "Sri Sathya Sai Hospital", "Nallurhalli", "Kundalahalli", "Seetharamapalya",
    "Hoodi", "Garudacharapalya", "Singayyanapalya", "Krishnarajapura (K.R.Pura)",
    "Benniganahalli", "Baiyappanahalli", "Swami Vivekananda Road", "Indiranagar",
    "Halasuru", "Trinity", "Mahatma Gandhi Road", "Cubbon Park",
    "Dr. BR. Ambedkar Station, Vidhana Soudha", "Sir M. Visveshwaraya Station, Central College",
    "Krantivira Sangolli Rayanna Railway Station", "Magadi Road",
    "Sri Balagangadharanatha Swamiji Station, Hosahalli", "Vijayanagara", "Attiguppe",
    "Deepanjali Nagara", "Mysuru Road", "Pantharapalya - Nayandahalli", "Rajarajeshwari Nagara",
    "Jnana Bharathi", "Pattanagere", "Kengeri Bus Terminal", "Kengeri", "Challaghatta"
]

stations = stationsg + stationsp
num_stations = len(stations)


interchange_points = {"Nadaprabhu Kempegowda Station, Majestic"}
ud = 1

def bngroute(sou,dest):
    adj_matrix = np.full((num_stations, num_stations), np.inf)
    np.fill_diagonal(adj_matrix, 0)

    for i in range(len(stationsg) - 1):
        adj_matrix[i, i + 1] = ud
        adj_matrix[i + 1, i] = ud
    
    for i in range(len(stationsp) - 1):
        adj_matrix[len(stationsg) + i, len(stationsg) + i + 1] = ud
        adj_matrix[len(stationsg) + i + 1, len(stationsg) + i] = ud

   
    majestic_index = stations.index("Nadaprabhu Kempegowda Station, Majestic")
    
    adj_matrix[majestic_index, stations.index("Mantri Square Sampige Road")] = ud
    adj_matrix[stations.index("Mantri Square Sampige Road"), majestic_index] = ud
    
    adj_matrix[majestic_index, stations.index("Chikkapete")] = ud
    adj_matrix[stations.index("Chikkapete"), majestic_index] = ud
    
    adj_matrix[majestic_index, stations.index("Sir M. Visveshwaraya Station, Central College")] = ud
    adj_matrix[stations.index("Sir M. Visveshwaraya Station, Central College"), majestic_index] = ud
    
    adj_matrix[majestic_index, stations.index("Krantivira Sangolli Rayanna Railway Station")] = ud
    adj_matrix[stations.index("Krantivira Sangolli Rayanna Railway Station"), majestic_index] = ud
    
    def dijkstra(adj_matrix, start_idx):
        num_nodes = len(adj_matrix)
        distances = [np.inf] * num_nodes
        previous_nodes = [None] * num_nodes
        distances[start_idx] = 0
        pq = [(0, start_idx)]  
    
        while pq:
            current_dist, current_node = heapq.heappop(pq)
    
            if current_dist > distances[current_node]:
                continue
    
            for neighbor, weight in enumerate(adj_matrix[current_node]):
                if weight < np.inf:
                    distance = current_dist + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous_nodes[neighbor] = current_node
                        heapq.heappush(pq, (distance, neighbor))
    
        paths = [[] for _ in range(num_nodes)]
        for target in range(num_nodes):
            if distances[target] < np.inf:
                current_node = target
                while current_node is not None:
                    paths[target].insert(0, stations[current_node])
                    current_node = previous_nodes[current_node]
    
        return distances, paths
    

    start_station = stations[sou-1]
    end_station = stations[dest-1]
    
    start_idx = sou-1
    end_idx = dest-1
    
    distances, paths = dijkstra(adj_matrix, start_idx)
    path = paths[end_idx]
    s = f"Time Taken from {start_station} to {end_station}: {distances[end_idx]} minutes"
    s1=""
    filtered_path = [station for station in path if station in interchange_points]
    if not (((start_station in stationsg) and (end_station in stationsg)) or ((start_station in stationsp) and (end_station in stationsp))) and (start_station != "Nadaprabhu Kempegowda Station, Majestic" and end_station != "Nadaprabhu Kempegowda Station, Majestic"):
        s1 += "\n"+"Interchange Stations "
        for station in filtered_path:
            s1 += f" -> {station}"
    return [s,s1]
