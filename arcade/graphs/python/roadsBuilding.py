
def roadsBuilding(cities, roads):
    city_set = set()
    for c in range(0, cities):
        city_set.add(c)

    city_connected = {}
    for r in roads:
        city_connected[str(r[0])+ '-' + str(r[1])] = True
        city_connected[str(r[1])+ '-' + str(r[0])] = True

    result_arr = []
    for c in range(0, cities):
        current = c
        for j in range(0, cities):
            token = str(current) + '-' + str(j)
            if j != c: 
                if token not in city_connected:
                    result_arr.append([current, j])
                    city_connected[str(current) + '-'+ str(j)] = True
                    city_connected[str(j)+ '-' + str(current) ]= True
    return result_arr
