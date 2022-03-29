import os
import sys
from collections import defaultdict
from io import StringIO

import numpy as np
import six.moves.urllib as urllib
import tensorflow as tf
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Blueprint
from werkzeug.utils import secure_filename

from animal_info import *
from user_info import *

sys.path.append("..")
from utils import label_map_util
from utils import visualization_utils as vis_util

MODEL_NAME = '../imagedetection/model'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
PATH_TO_LABELS = os.path.join('../imagedetection/data', 'label.pbtxt')
NUM_CLASSES = 8
animal_name = ''

save_blueprint = Blueprint("save_blueprint", __name__)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '../imagedetection/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@save_blueprint.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('save_blueprint.uploaded_file',
                                filename=filename))


@save_blueprint.route('/uploads/<filename>')
def uploaded_file(filename):
    PATH_TO_TEST_IMAGES_DIR = app.config['UPLOAD_FOLDER']
    TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, filename.format(i)) for i in range(1, 2)]
    IMAGE_SIZE = (12, 8)

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            for image_path in TEST_IMAGE_PATHS:
                image = Image.open(image_path)
                image_np = load_image_into_numpy_array(image)
                image_np_expanded = np.expand_dims(image_np, axis=0)
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                scores = detection_graph.get_tensor_by_name('detection_scores:0')
                classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                vis_util.visualize_boxes_and_labels_on_image_array(
                    image_np,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    category_index,
                    use_normalized_coordinates=True,
                    line_thickness=8)
                im = Image.fromarray(image_np)
                im.save('../imagedetection/uploads/' + filename)
            global animal_name
            mylabel = ([category_index.get(value) for index, value in enumerate(classes[0]) if scores[0, index] > 0.5])
            animal_name = getMappedName(mylabel[0].get('name'))
    return redirect(url_for('save_blueprint.fetch_details_for',animal_name=animal_name))


@save_blueprint.route('/<animal_name>', methods=['POST'])
def fetch_details_for(animal_name):
    animal_info = get_all_details_for(animal_name)
    return render_template("index.html", name=animal_name, users=user_details(), loaded=True, info=animal_info)