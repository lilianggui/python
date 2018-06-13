import os

from PIL import Image, ImageFont, ImageDraw


path = r'C:\Users\Lange\Desktop\python\001\allPicture'
for root, dirs, files in os.walk(path):
    for i in range(len(files)):
        fn = files[i]
        im = Image.open(root + '\\' + fn)
        draw = ImageDraw.Draw(im)
        newfont = ImageFont.truetype('simkai.ttf', 80)
        draw.text((im.size[0] - 50*len(str(i)), 3), str(i+1), (255, 0, 0), font=newfont)
        targetPath = os.path.join(path, '..', 'target')
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        im.save(os.path.join(targetPath, fn))
print('finished!')


