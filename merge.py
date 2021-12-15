from PIL import Image

def merge(tpl, prj_path):

    path = prj_path + "/photos/"
    array = tpl[0]
    num_rows = tpl[1]
    num_cols = int(len(array)/num_rows)
    columns = []

    for i in range(len(array)):
        array[i] = Image.open(path + array[i])

    for i in range(num_cols):
        for _ in range(num_rows-1):
            merged = mergeHeight(array[0], array[1])
            array.pop(0)
            array.pop(0)
            array.insert(0, merged)
        columns.append(array.pop(0))
    
    for i in range(num_cols-1):
        merged = mergeWidth(columns[i], columns[i+1])
        columns.pop(0)
        columns.pop(0)
        columns.insert(0, merged)

    saveMergedImage(columns, prj_path)


def mergeWidth(im1, im2):
    background = Image.new('RGB', (im1.width + im2.width, im1.height))
    background.paste(im1, (0, 0))
    background.paste(im2, (im1.width, 0))
    return background


def mergeHeight(im1, im2):
    background = Image.new('RGB', (im1.width, im1.height + im2.height))
    background.paste(im1, (0, 0))
    background.paste(im2, (0, im1.height))
    return background

def saveMergedImage(item: list, path):
    item[0].save(path + "/merged/out.jpg")
    