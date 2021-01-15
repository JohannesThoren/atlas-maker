from PIL import Image
import glob


files = glob.glob("[!_]*.png")

if (len(files) % 2) != 0:
    files.append("_PlaceHolder.png")

files.sort()
print(files)

images = [Image.open(im) for im in files]


widths, heights = zip(*(i.size for i in images))


total_width = int(sum(widths) / 2)
max_height = max(heights) * 2

new_im = Image.new('RGBA', (total_width, max_height))

x_off = 0
y_off = 0

for im in images:
    if x_off == total_width:
        y_off += int(max_height / 2)
        x_off = 0

    print(f"x_off: {x_off}, y_off: {y_off}")
    new_im.paste(im, (x_off, y_off))

    x_off += im.size[0]


new_im.save("atlas.png")