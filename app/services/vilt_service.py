from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image
import torch

class Service:
    def __init__(self):
        self.model_name = "dandelin/vilt-b32-finetuned-vqa"
        self.processor = ViltProcessor.from_pretrained(self.model_name)
        self.model = ViltForQuestionAnswering.from_pretrained(self.model_name)

    def predict(self, text: str, image: Image.Image) -> str:
        encoding = self.processor(image, text, return_tensors = "pt")
        
        with torch.no_grad():
            outputs = self.model(**encoding)
        
        logits = outputs.logits
        index = logits.argmax(-1).item()
        return self.model.config.id2label[index]

# Singleton - not to reload the model on each request
vilt_service = Service()