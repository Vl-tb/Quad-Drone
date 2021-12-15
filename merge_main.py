from sort import sortImages
from merge import merge


def main():
    path = "/Users/vladprotsenko/Documents/POC/Drone"

    photos = sortImages(path + "/photos")
    merge(photos, path)

main()