import os
import numpy as np
#import time
import json
#import codecs
import datetime
import cv2
#import requests
#from PIL import Image
from azure.storage.blob import BlockBlobService
import base64
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check():
    try:
        if request.method != "POST":
            return 'GET METHOD'
        else:
            return 'POST METHOD'
    except:
        return 'exception'
    
if __name__ == "__main__":
    app.run()
