import urllib

import numpy as np
import gradio as gr
import torch
import random

from PIL import Image
from transformers import MaskFormerFeatureExtractor, MaskFormerForInstanceSegmentation

from typing import Dict

device = torch.device("cuda:0")
model = MaskFormerForInstanceSegmentation.from_pretrained(
    "facebook/maskformer-swin-tiny-ade"
).to(device)
model.eval()
preprocessor = MaskFormerFeatureExtractor.from_pretrained(
    "facebook/maskformer-swin-tiny-ade"
)

label2color = {
    label: (random.randint(0, 1), random.randint(0, 255), random.randint(0, 255))
    for label in range(150)  # 150 classes in ADE20K
}

def visualize_instance_seg_mask(mask):
    image = np.zeros((mask.shape[0], mask.shape[1], 3))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j, :] = label2color[mask[i, j]]
    image = image / 255
    return image

def predict(img: np.array):
    target_size = (img.shape[0], img.shape[1])
    inputs = preprocessor(images=img, return_tensors="pt")
    inputs = inputs.to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    outputs.class_queries_logits = outputs.class_queries_logits.cpu()
    outputs.masks_queries_logits = outputs.masks_queries_logits.cpu()
    results = (
        preprocessor.post_process_segmentation(
            outputs=outputs, target_size=target_size
        )[0]
        .cpu()
        .detach()
    )
    results = torch.argmax(results, dim=0).numpy()
    results = visualize_instance_seg_mask(results)
    return results

demo = gr.Interface(
    fn=predict,
    live=True,
    inputs=[gr.Image(source="webcam", streaming=True)],
    outputs=[gr.Image()],
    title="MaskFormer Instance Segmentation",
)

demo.launch(debug=True)