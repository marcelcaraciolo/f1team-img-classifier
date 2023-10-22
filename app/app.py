import gradio as gr
import tensorflow as tf
from huggingface_hub import from_pretrained_keras

CLASS_NAMES = ['alfaromeo',
 'alphatauri',
 'alpine',
 'astonmartin',
 'ferrari',
 'haas',
 'mclaren',
 'mercedes',
 'redbull',
 'williams']


model = from_pretrained_keras("marcelcaraciolo/keras-efficientnetb0-f1teams")


def predict(img):
    img = img.reshape(1,224,224,3)
    prediction = model.predict(img)
    probs = tf.squeeze(tf.round(prediction))
    return {CLASS_NAMES[i]: float(probs[i]) for i in range(len(CLASS_NAMES))}

title = "F1 2023 Car Team Classifier"
description = "A F1 Car Team classifier trained on the Formula One 2023 car images dataset with keras tensorflow. Created as a demo for Gradio and HuggingFace Spaces."
article="<p style='text-align: center'><a href='https://github.com/marcelcaraciolo/f1team-img-classifier' target='_blank'>Further information</a></p>"
examples = ['alfaromeo_40.jpg', 'alphatauri_38.jpg', 'alpine_6.jpg', 'ferrari_8.jpg', 'haas_76.jpg', 'mercedes_47.jpg', 'redbull_10.jpg', 'williams_12.jpg', 'astonmartin_37.jpg', 'mclaren_53.jpg']
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,inputs=gr.inputs.Image(shape=(224, 224)),outputs=gr.outputs.Label(num_top_classes=3),title=title,description=description,article=article,examples=examples,interpretation=interpretation,enable_queue=enable_queue).launch()