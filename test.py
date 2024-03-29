import cv2

cap = cv2.VideoCapture('D:\Introduction_To_WebDev\Cristiano Ronaldo Top 10 Impossible Goals ● Is He Human.mp4')
input_frame_rate = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (1280, 720), isColor=False)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 50)
        edges = cv2.resize(edges, (1280, 720))
        out.write(edges)
        cv2.imshow('Edge Detection', edges)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
