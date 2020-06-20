import os
import keras
import pydload
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color

import cv2
import numpy as np

WEIGHTS_URL = 'https://github.com/notAi-tech/LogoDet/releases/download/292_classes_v1/weights'
CLASSES_URL = 'https://github.com/notAi-tech/LogoDet/releases/download/292_classes_v1/classes'

home = os.path.expanduser("~")
model_folder = os.path.join(home, '.LogoDet/')
if not os.path.exists(model_folder):
    os.mkdir(model_folder)

model_path = os.path.join(model_folder, 'weights')

if not os.path.exists(model_path):
    print('Downloading the checkpoint to', model_path)
    pydload.dload(WEIGHTS_URL, save_to_path=model_path, max_time=None)

classes_path = os.path.join(model_folder, 'classes')

if not os.path.exists(classes_path):
    print('Downloading the class list to', classes_path)
    pydload.dload(CLASSES_URL, save_to_path=classes_path, max_time=None)

detection_model = models.load_model(model_path, backbone_name='resnet50')
classes = open(classes_path).readlines()
classes = [i.strip() for i in classes if i.strip()]

def detect_single(img_path, min_prob=0.4):
    image = read_image_bgr(img_path)
    image = preprocess_image(image)
    image, scale = resize_image(image)
    boxes, scores, labels = detection_model.predict_on_batch(np.expand_dims(image, axis=0))
    boxes /= scale
    processed_boxes = []
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        if score < min_prob:
            continue
        box = box.astype(int).tolist()
        label = classes[label]
        processed_boxes.append({'box': box, 'score': score, 'label': label})
        
    return processed_boxes


def detect_batch():
    # TODO
    pass