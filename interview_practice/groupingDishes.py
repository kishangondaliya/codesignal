def groupingDishes(dishes):
    my_dic = {}
    for dish in dishes:
        main_dish = dish[0]
        dish = dish[1:]
        for i, v in enumerate(dish):
            if v in my_dic:
                my_dic[v] = my_dic[v] + [main_dish]
            else:
                my_dic[v] = [main_dish]
    #filter
    filter_dic = {}
    for k, v in my_dic.items():
        if len(v) > 1:
            filter_dic[k] = v
    #print(filter_dic)
    new = sorted(filter_dic.items())
    arr = []
    for i in new:
        arr.append([i[0],*sorted(i[1])])
    
    return arr
