from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import time

score_th =0.7

def authenticate_the_client(endpoint, key):
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    return client

def describe_image(client, image_url):
    '''
    Describe images with human-readable language with the confidence score.
    '''
    res = client.describe_image(image_url)
    
    #print("des,\t-1,\t{}".format(res.request_id))
#    cnt =0
    s='Image Description:\n'
    for caption in res.captions:
        if caption.confidence > score_th:
#            cnt +=1
#            s += "des,\t{:d},\t{:20s},\t{:.2f}%\n".format(cnt, caption.text, caption.confidence * 100)
            s += "{:20s}\t(confidence: {:.2f}%)\n".format(caption.text, caption.confidence * 100)
    return s

def categorize_image(client, image_url):
    '''
    Categorize an Image with a confidence score.
    https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/concept-categorizing-images
    '''
    res = client.analyze_image(image_url , ["categories"])

    #print("cat,\t-1,\t{},".format(res.request_id))
    cnt=0
    s=''
    for category in res.categories:
        if category.score > score_th:
            cnt +=1
            s += "cat,\t{:d},\t{:20s},\t{:.2f}%\n".format(cnt, category.name, category.score * 100)
    return s

def detect_color_image(client, image_url):
    '''
    Detects the different aspects of its color scheme in a remote image.
    '''
    res = client.analyze_image(image_url, ["color"])

    #print("clr,\t-1,\t{}".format(res.request_id))
    s=''
    #s += "clr,\t{:d},\t{:20b},\t{}\n".format(1, res.color.is_bw_img, 'Is black and white')
    s += "clr,\t{:d},\t{:20s},\t{}\n".format(2, res.color.accent_color, 'Accent color')
    s += "clr,\t{:d},\t{:20s},\t{}\n".format(3, res.color.dominant_color_background, 'Dominant background color')
    s += "clr,\t{:d},\t{:20s},\t{}\n".format(4, res.color.dominant_color_foreground, 'Dominant foreground color')
    #cnt = 4
    #for dom_color in res.color.dominant_colors:
    #    cnt +=1
    #    s += "clr,\t{:d},\t{:20s},\t{}\n".format(cnt, dom_color, 'Dominant colors')
    return s

def get_landmark_image(client,image_url):
    res = client.analyze_image_by_domain("landmarks", image_url)
    
    #print("lnd,\t-1,\t{},".format(res.request_id))
    cnt=0
    s=''
    for landmark in res.result["landmarks"]:
        if landmark.confidence > score_th:
            cnt +=1
            s += "tag,\t{:d},\t{:20s},\t{:.2f}%\n".format(cnt, landmark.name, landmark.confidence * 100)
    return s


def tag_image(client, image_url):
    '''
    Tag an Image for each thing in the image.
    '''
    res = client.tag_image(image_url)

    #print("tag,\t-1,\t{},".format(res.request_id))
    cnt=0
    s =''
    for tag in res.tags:
        if tag.confidence > score_th:
            cnt +=1
            s += "tag,\t{:d},\t{:20s},\t{:.2f}%\n".format(cnt, tag.name, tag.confidence * 100)
    return s

def extract_text_image(client, image_url):
    '''
    Extract handwritten text in an image
    from Microsoft's tutorial
    '''
    res = client.read(image_url,  raw=True)

    #print("txt,\t-1,\t,")

    # Grab the ID from the URL
    operation_id = res.headers["Operation-Location"].split("/")[-1]

    # Call the "GET" API every 1 second and wait for it to retrieve the results 
    while True:
        get_handw_text_results = client.get_read_result(operation_id)
        if get_handw_text_results.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

#    cnt =0
    s='Exctracted text:\n'
    # Print the detected text, line by line
    if get_handw_text_results.status == OperationStatusCodes.succeeded:
        for text_result in get_handw_text_results.analyze_result.read_results:
            for line in text_result.lines:
#                cnt +=1
#                s += "txt,\t{:d},\t{:20s},\n".format(cnt, line.text )
                s += "{:20s},\n".format(line.text )
                #print(line.bounding_box)
    return s



