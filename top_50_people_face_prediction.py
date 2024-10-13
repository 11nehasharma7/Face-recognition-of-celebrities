# -*- coding: utf-8 -*-
pip install gradio

pip install face_recognition

import face_recognition
import pickle
import numpy as np
def predictive_system(reference_image_path):
  # Load the model (face encodings and file names)
  with open('face_recognition_model.pkl', 'rb') as f:
      encoded_images, image_files = pickle.load(f)

  # Find the best match
  distances = np.linalg.norm(encoded_images - reference_encoding, axis=1)
  best_match_index = np.argmin(distances)

  # Print the best match result
  res = image_files[best_match_index]
  res = res.replace(".jpg","")
  return res

import gradio as gr
title = "Face Prediction"

app = gr.Interface(fn = predictive_system, inputs="image", outputs="textbox", title=title)

app.launch(share=True)
