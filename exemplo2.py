import cv2

webCamera = cv2.VideoCapture(0)
classificadorVideo = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
classificadorOlho = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

while True:
    camera, frame = webCamera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificadorVideo.detectMultiScale(cinza, scaleFactor=1.3, minNeighbors=3)
    for (x, y, l, a) in detecta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2)
        pegarOlho = frame[y:y + a, x:x + l]
        olhoCinza = cv2.cvtColor(pegarOlho, cv2.COLOR_BGR2GRAY)
        localizaOlho = classificadorOlho.detectMultiScale(olhoCinza)
        for (ox, oy, ol, oa) in localizaOlho:
            cv2.rectangle(pegarOlho, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

    cv2.imshow("Video Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

webCamera.release()
cv2.destroyAllWindows()
