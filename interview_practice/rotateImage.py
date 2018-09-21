def rotateImage(a):
    arr = a
    layer = len(arr) - 1
    print("Original layer", layer)
    max_offset = len(arr) - 1
    print("Max_offset:", max_offset)
    for l in range(layer - 1):
        # print("Layer:", l)
        # print("new layer=============")
        # print("max_off", max_offset)
        for j in range(max_offset):

            #top
            tmp = arr[l][l + j]
            # print("top:", tmp)

            #right
            right = arr[l + j][max_offset+l]
            # print("right:", right)
            arr[l + j][max_offset+l] = tmp

            #down
            down = arr[max_offset+l][max_offset - j+l]
            # print("down:",down)
            arr[max_offset+l][max_offset-j+l] = right

            # left
            left = arr[max_offset -j +l][l]
            # print("left", left)
            arr[max_offset -j+l][l] = down

            #top
            arr[l][l + j] = left



            # print(np.matrix(arr))

        max_offset -= 2
    return arr
