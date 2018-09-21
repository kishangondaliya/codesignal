def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    res = []
    for i,j in zip(cost_per_minute, cost_per_mile):
        res.append((ride_time * i) + (ride_distance* j))
    return res
