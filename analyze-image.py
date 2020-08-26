from utils.cv_functions import *
from utils.input_data import get_inpu_data
from utils.sys_check import get_env_variables
from utils.text_to_image import save_image
import os
import requests

'''
Computer Vision API (v3.0)
https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-ga/operations/5d986960601faab4bf452005
'''

endpoint, key = get_env_variables()
computervision_client = authenticate_the_client(endpoint, key)
remote_image_urls = get_inpu_data()

# Apps
cvc = computervision_client

for i,img in enumerate(remote_image_urls):

    name = os.path.basename(img).split('.')[0]
    print('Image,\t'+ str(i)+ ',\t' + str(name)+',')

    # Download the image 
    response = requests.get(img)
    file = open("images/"+os.path.basename(img), "wb")
    file.write(response.content)
    file.close()
    try:

        # Analyze and save the image
        s=''
        #for f in [describe_image, extract_text_image]: # categorize_image, tag_image, detect_color_image, get_landmark_image, extract_text_image]:
        #    s_tmp = f(cvc, img)
        #    if s_tmp:
        #        s += s_tmp
        #print(s)
        #save_image(s, name)
    except:
        pass
        


