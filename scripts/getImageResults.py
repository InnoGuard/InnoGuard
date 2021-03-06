from google.cloud import vision
from google.cloud.vision import types
import cv2
import io
import browserhistory as bh
import libs.Constants


# user = bh.get_username()
# API_KEY = libs.Constants.GC_API_KEY - don't need this?
__file__ = libs.Constants.FILE_PATH


def get_image_results():
    
    image_path = input("\nPlease enter the path to the image you wish to test: ") 
    print("Path entered: ", image_path) 

    client = vision.ImageAnnotatorClient()
    img = cv2.imread(image_path)
    img_bytes = cv2.imencode('.jpg', img)[1].tostring() # Encode Image into Bytes

    image = types.Image(content=img_bytes)

    response = client.safe_search_detection(image=image)

    if response.error.message:
        raise Exception(response.error.message)

    else:

        safety = response.safe_search_annotation

        results = {
            'adult: {}'.format(
                libs.Constants.likelihood_name[safety.adult]),
            'medical: {}'.format(
                libs.Constants.likelihood_name[safety.medical]),
            'spoofed: {}'.format(
                libs.Constants.likelihood_name[safety.spoof]),
            'violence: {}'.format(
                libs.Constants.likelihood_name[safety.violence]),
            'racy: {}'.format(
                libs.Constants.likelihood_name[safety.racy]),
        }

        return results # To put into front-end

r = get_image_results() # front-end to upload images for testing
print("\nGoogle Vision API Image Results: ")
print(r,"\n")
