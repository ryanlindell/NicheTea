from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

print(os.listdir())

stageImages = []
for stageFiles in os.listdir():
    if stageFiles.endswith(".png"):
        stageImages.append(stageFiles)

print(stageImages)

for img in stageImages:

    #desired d 1100 x 730

    imgFile = Image.open(img)
    imgFile = imgFile.resize((1100, 730), Image.ANTIALIAS)


    #savImg = savImg.filter(ImageFilter.GaussianBlur(radius = 1))

    imgFile.save(img, "PNG")
    