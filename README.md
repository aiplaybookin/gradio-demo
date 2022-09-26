# Use of Gradio for demo app UI

https://gradio.app/docs/

### Very easy and fast

Install Gradio
```
pip install gradio
```

Install torch
```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```

**torch hub** : collection of models , (timm has its own model repo)

**Interface** has inputs : where you can specify one or more text, images etc.

Gradio Image Params : look params for image
https://gradio.app/docs/#image

When you specify ```launch(share=True)``` One opened in local along with a public url

Run app visionApp.py 
```
gradio visionApp.py
```
![Output](./images/timmVision.png)

💡 When **Flag** is clicked it, saves input & output. Can be used to log false positives.

### APIs

Go to bottom of the app page and Click on **view api**

![View API](./images/bottom_api.png)


**View API docs** as below

![API Docs](./images/api_doc.png)




Ref:

```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```

