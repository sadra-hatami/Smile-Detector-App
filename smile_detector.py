import cv2

def main():
    # بارگذاری مدل‌های Haar از مسیر داخلی OpenCV
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    smile_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_smile.xml"
    )

    # وبکم
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ وب‌کم باز نشد. شماره وبکم را تغییر دهید (0/1) یا دسترسی را بررسی کنید.")
        return

    print("✅ برای خروج، کلید q را بزنید.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ فریم دریافت نشد.")
            break

        # برای سرعت و دقت Haar بهتر است خاکستری کنیم
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # تشخیص صورت‌ها
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(80, 80)
        )

        for (x, y, w, h) in faces:
            # کادر صورت
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # ناحیه صورت برای تشخیص لبخند
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # تشخیص لبخند (در ناحیه صورت)
            smiles = smile_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.7,
                minNeighbors=20,
                minSize=(25, 25)
            )

            if len(smiles) > 0:
                cv2.putText(frame, "SMILE :)", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

                # (اختیاری) نمایش کادر لبخندها
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)

        cv2.imshow("Smile Detector - Press q to quit", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()