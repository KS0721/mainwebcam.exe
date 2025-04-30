from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer
import cv2
import os
import sys
import datetime
import csv

# 리소스 경로 설정 (PyInstaller 대응용)
def resource_path(relative_path):
    """PyInstaller에서도 리소스 정상 접근 가능하게 만드는 함수"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# UI 파일 로드
try:
    ui_path = resource_path("pyqtapp2.ui")
    Form, Window = uic.loadUiType(ui_path)
except Exception as e:
    print(f"UI 파일 로드 실패: {e}")

class MyWindow(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼 연결
        if hasattr(self, 'filmBut'):
            self.filmBut.clicked.connect(self.capture_photo)
        else:
            print("filmBut 버튼을 찾을 수 없습니다!")

        if hasattr(self, 'SaveBut'):
            self.SaveBut.clicked.connect(self.save_files)
        else:
            print("SaveBut 버튼을 찾을 수 없습니다!")

        self.cap = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.start_camera()

    def start_camera(self):
        """웹캠 시작 (DirectShow 사용)"""
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not self.cap.isOpened():
            QMessageBox.critical(self, "오류", "카메라를 열 수 없습니다.")
            return

        self.timer.start(30)

    def update_frame(self):
        """카메라 프레임을 QLabel에 표시"""
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                return

            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            self.label_Cam.setPixmap(QPixmap.fromImage(q_image))

    def capture_photo(self):
        """웹캠에서 사진 캡처 및 자동 파일명 생성"""
        if not self.cap or not self.cap.isOpened():
            QMessageBox.warning(self, "경고", "카메라가 열려 있지 않습니다.")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        image_file_name = f"image_{timestamp}.png"

        self.lineEdit_file.setText(image_file_name)

        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite(image_file_name, frame)

            name = self.lineEdit_Name.text().strip()
            num = self.lineEdit_Num.text().strip()
            remark = self.textEdit_Remark.toPlainText().strip()

            self.image_file_name = image_file_name
            self.name = name
            self.num = num
            self.remark = remark

            QMessageBox.information(self, "저장 준비", f"이미지 파일명은 자동으로 생성되었습니다:\n{image_file_name}")
        else:
            QMessageBox.critical(self, "오류", "사진을 찍는 데 실패했습니다.")

    def save_files(self):
        """파일 저장: 이미지 파일과 CSV 저장"""
        if not hasattr(self, 'image_file_name'):
            QMessageBox.warning(self, "경고", "먼저 사진을 캡처하세요.")
            return

        image_file_name = self.image_file_name
        csv_file_name = image_file_name.replace('.png', '.csv')

        with open(csv_file_name, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Number", "Remark", "Image File"])
            writer.writerow([self.name, self.num, self.remark, image_file_name])

        QMessageBox.information(self, "저장 완료", f"이미지와 CSV 파일이 저장되었습니다:\n{image_file_name}\n{csv_file_name}")

    def closeEvent(self, event):
        """종료 시 카메라 해제"""
        self.timer.stop()
        if self.cap:
            self.cap.release()
        event.accept()

# 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
