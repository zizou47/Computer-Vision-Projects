from ultralytics import YOLO
import math

model = YOLO('yolov8x')
results = model.predict(r'C:\Users\yazid\Desktop\mon pt revision\My epita courses\S3\Computer Vision Projects\Football Analysis\input video\test.mp4', save = True)

print(results[0])
print('************')

for result in results:
    for box in result.boxes:
        if any(map(math.isnan, box)):
            print("NaN found in box coordinates:", box)
