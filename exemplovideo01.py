# Captura foto da webcam
import cv2

# Zero para camera da propria maquina, 1 para cameras externas
cv2.namedWindow("Imagem WebCamera")
webcamera = cv2.VideoCapture(0)

camera, frame = webcamera.read()

while True:

  if frame is not None:
     cv2.imshow("Imagem WebCamera", frame)
  camera, frame = webcamera.read()

  if cv2.waitKey(1) & 0xFF == ord('f'):
    break

webcamera.release()
cv2.destroyAllWindows()
