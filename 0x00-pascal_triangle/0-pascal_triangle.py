def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [1]

    for i in range(1,n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i]) + triangle[j]

        row.append(1)
    
    return triangle