def read(path="coords.txt"):
    out_coords = []
    with open(path, 'r', encoding="utf-8") as file:
        coords = file.read().split(",")

    for i in range (0, len(coords), 2):
        out_coords.append([coords[i], coords[i+1]])
    return out_coords
    