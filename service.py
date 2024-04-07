from ultralytics import YOLO
import cv2

model = YOLO('D:\\Workspace\\DATN\\backend-py\\best.pt')

def predict(img):
    result_instance = []
    results = model.predict(source=img, conf=0.5)
    for result in results:
        for c in range(0,5):
            id = result.probs.top5[c]
            name = result.names[id]
            prob = float(result.probs.top5conf.numpy()[c])
            prob = float("{:.10f}".format(prob))
            result_instance.append({"id":id,"name": name,"prob": prob})
    return result_instance

if __name__ == '__main__':
    img = cv2.imread('D:\\Workspace\\DATN\\backend-py\\ee58fac2-fc57-4c63-a65b-ede727cf1d43___UF.GRC_BS_Lab Leaf 0809.JPG')
    results = predict(img)
    print(results)
