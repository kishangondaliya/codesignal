def fancyRide(l, fares):
    max_fare = 20
    cars = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    arr = [l * e for e in fares]
    class_ = 0
    for i, e in enumerate(arr):
        if e <= max_fare:
            class_ = i
    return cars[class_]
