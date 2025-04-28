# mainwebcam.exe 배포

기존에 만들어둔 `mainwebcam.py`를 `.exe` 파일로 변환하는 코드입니다.

### 1. PyInstaller 설치 및 .exe 파일 생성

- `-w`: 콘솔 창을 숨깁니다.
- `-F`: 여러 패키지와 인터프리터를 포함한 모든 파일을 하나의 `.exe` 파일로 묶습니다.

```bash
pip install pyinstaller
pyinstaller -w -F mainwebcam.py
```

### 2. mainwebcam.exe 파일을 생성
