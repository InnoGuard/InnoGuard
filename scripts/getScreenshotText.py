from matplotlib import pyplot as plt
from easyocr import Reader
import pandas as pd
import argparse
import cv2
import time

class getScreenShotText:
    def __init__(self):
        self.image = None
        self.results = None
        self.reader = self._getReader()

    def _getReader(self):
        return Reader(['en'], gpu = True)

    def getScreenshotText(self, path):
        print('Processsing Image...')
        self.image = self.readImage(path)
        ts = time.time()
        self.results = self.reader.readtext(self.image)
        te = time.time()
        td = te - ts
        print(f'Completed in {td} seconds')
        return self._getText()

    def _getText(self):
        for (bbox, text, prob) in self.results:
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            all_text.append(text)
        return ' '.join(all_text)

    def getImageOverlay(self):
        for (bbox, text, prob) in self.results:
            # get the bounding box coordinates
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))

            # Remove non-ASCII characters from the text so that
            # we can draw the box surrounding the text overlaid onto the original image
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
            all_text.append(text)

            cv2.rectangle(image, tl, br, (255, 0, 0), 2)
            cv2.putText(image, text, (tl[0], tl[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        return image


    def readImage(self, path):
        self.image = cv2.imread(path)
        return self.image

    def imgshow(self, title="", image = None, size = 6):
        if image.any():
            w, h = image.shape[0], image.shape[1]
            aspect_ratio = w/h
            plt.figure(figsize=(size * aspect_ratio,size))
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.title(title)
            plt.show()
        else:
            print("Image not found")