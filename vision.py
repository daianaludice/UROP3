import io
import os

#export GOOGLE_APPLICATION_CREDENTIALS = /Users/lenovo/UROP3/My Project Vison-142fec25897d.json

from google.cloud import vision

vision_client = vision.Client()

file_name = os.path.join(
    os.path.dirname(__file__),
    '1.jpg')

with io.open(file_name, 'rb') as image_file :
   content =image_file.read()
   image = vision_client.image(
      content=content)

labels = image.detect_labels()

print('Labels:')
for label in labels:
  print(label.description)

