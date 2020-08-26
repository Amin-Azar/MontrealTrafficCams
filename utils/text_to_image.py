import sys
from PIL import Image, ImageDraw, ImageFont

def save_image(txt, name, path='./reports/'):
    
    img = Image.new('RGB', (360, 240), color = (50, 50, 50)) 
    d = ImageDraw.Draw(img)
    d.text((10,10), txt, fill=(255,255,200))
    
    img.save(path+name+'.jpg')
