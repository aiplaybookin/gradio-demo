import urllib

import gradio as gr
import torch
import timm

from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform

from typing import Dict

MODEL: str = "resnet18"

model = timm.create_model(MODEL, pretrained=True)
model.eval()

# Download human-readable labels for ImageNet.
# get the classnames
url, filename = (
    "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt",
    "imagenet_classes.txt",
)
urllib.request.urlretrieve(url, filename)
with open("imagenet_classes.txt", "r") as f:
    categories = [s.strip() for s in f.readlines()]

def predict(inp_img: Image) -> Dict[str, float]:
    config = resolve_data_config({}, model=MODEL)
    transform = create_transform(**config)

    img_tensor = transform(inp_img).unsqueeze(0)  # transform and add batch dimension

    # inference
    with torch.no_grad():
        out = model(img_tensor)
        probabilities = torch.nn.functional.softmax(out[0], dim=0)
        confidences = {categories[i]: float(probabilities[i]) for i in range(1000)}

    return confidences

gr.Interface(
    fn=predict,
    live=True,
    inputs=gr.Image(source="webcam", streaming=True, type="pil"),
    outputs=gr.Label(num_top_classes=10),
).launch(share=True)