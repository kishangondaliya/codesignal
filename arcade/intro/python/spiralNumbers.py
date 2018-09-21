def spiralNumbers(n):
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    matrix = [[0 for i in range(n)] for i in range(n)]
    current_pos = (0,0)
    current_dir = 0
    for i in range(1, n * n + 1):
        matrix[current_pos[0]][current_pos[1]] = i
        next_pos = current_pos[0] + direction[current_dir][0], current_pos[1] + direction[current_dir][1] 
        if next_pos[0] >= n or next_pos[0] < 0 or next_pos[1] >= n or next_pos[1] < 0 or matrix[next_pos[0]][next_pos[1]] != 0:
            current_dir = (current_dir + 1) % 4
            next_pos = current_pos[0] + direction[current_dir][0], current_pos[1] + direction[current_dir][1] 
        current_pos = next_pos
    return matrix
