from google.cloud import vision
import cv2
import io
import browserhistory as bh
import libs.Constants

# user = bh.get_username()
API_KEY = libs.Constants.GC_API_KEY


def get_image_results(image_path):
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as inference_image:
        content = inference_image.read()

    image = vision.Image(content=content)

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

        return results
