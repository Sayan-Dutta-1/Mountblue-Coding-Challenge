def is_valid_integer(input_str):
    if not input_str.isdigit():
        return False
    return True

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def connected_clusters(matrix):
    n = len(matrix)
    parent = [i for i in range(n)]
    rank = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                union(parent, rank, i, j)

    clusters = set()
    for i in range(n):
        clusters.add(find(parent, i))

    return len(clusters)

def process_input():
    while True:
        try:
            matinput_row_str = input()
            if not matinput_row_str:
                break

            matinput_row, matinput_col = map(int, matinput_row_str.split())
            matrix = []
            for _ in range(matinput_row):
                row_str = input()
                row = list(map(int, row_str.split()))
                if len(row) != matinput_col:
                    raise ValueError("Invalid input: Row length mismatch")

                matrix.append(row)

            clusters = connected_clusters(matrix)
            print(clusters)
        except ValueError as e:
            print("Invalid input:", e)

if __name__ == "__main__":
    process_input()

