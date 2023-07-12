import configparser
from transformers import pipeline

config = configparser.ConfigParser()
config.read("env.cfg")

img_token = config.get("default", "token", fallback=None)

def img_to_text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)
    return text

img_to_text("test.JPG")