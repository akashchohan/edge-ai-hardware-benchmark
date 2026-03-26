import torch
import torchvision.models as models

def load_model():
    model = models.mobilenet_v2(pretrained=True)
    model.eval()
    return model