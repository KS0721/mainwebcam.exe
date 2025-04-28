# mainwebcam.exe 배포

기존에 만들어둔 `mainwebcam.py`를 `.exe` 파일로 변환하는 코드입니다.

### 1. PyInstaller 설치 및 .exe 파일 생성

- `-w`: 콘솔 창을 숨깁니다.
- `-F`: 여러 패키지와 인터프리터를 포함한 모든 파일을 하나의 `.exe` 파일로 묶습니다.
- `--debug all`: 디버그 정보를 출력합니다.
- `--add-data "pyqtapp2.ui;."`: `pyqtapp2.ui` 파일을 포함시켜 `.exe` 파일과 함께 배포합니다.
```bash
pip install pyinstaller
pyinstaller -w -F --debug all --add-data "pyqtapp2.ui;." mainwebcam.py
```

### 2. mainwebcam.exe 파일을 생성
![image](https://github.com/user-attachments/assets/10aea60d-688b-4260-9989-a667005476fe)

![image](https://github.com/user-attachments/assets/1ee3c6b7-f5f9-44b6-a5d7-47a3656a6ce9)

### 3. mainwebcam.exe 파일 실행
<img src="https://github.com/user-attachments/assets/b249c314-e09f-458b-8509-34b06ec1619c" width="250"/>

### 4. 소프트웨어 설치 프로그램을 만드는 데 사용되는 도구 다운로드
[![image](https://github.com/user-attachments/assets/0aabf0d6-bda2-432f-b4dc-555cfe3041a6)](https://dinae.tistory.com/23)
(이미지 클릭시 사이트 이동)
### 5. webCamApp_setup.exe 설치 파일 만들기
#### 5.1 프로젝트 이름 변경
- InstallFactory에서 프로젝트 이름을 변경하여, 최종적으로 생성되는 설치 파일의 이름과 관련된 설정을 합니다.

#### 5.2 소스 폴더 설정
- `.exe` 파일이 포함된 폴더의 경로를 지정합니다. 이 경로는 설치 파일을 생성할 때 포함될 파일들의 소스 위치를 결정합니다.

#### 5.3 기본 설치 폴더 경로 설정
- 사용자가 소프트웨어를 설치할 기본 폴더를 설정합니다. 이 폴더는 프로그램이 설치될 위치를 지정하며, 일반적으로 "C:\Program Files" 또는 "C:\Users\Username" 등의 경로를 선택할 수 있습니다.

#### 5.4 설치 파일 생성 경로 설정
- 최종 설치 파일이 생성될 폴더를 지정합니다. 이 경로는 배포용 설치 파일을 저장할 위치로, 예를 들어 "D:\Installers"와 같은 경로로 설정할 수 있습니다.

#### 5.5 설치 파일 이름 설정
- 생성될 설치 파일의 이름을 설정합니다. 예를 들어, "MyApp_Setup.exe"와 같은 형태로 파일 이름을 설정하여 배포 시 이름을 일관되게 할 수 있습니다.
<img src="https://github.com/user-attachments/assets/9c9d6da7-0a6d-402c-84b5-170b122b578a" width="500"/>

### 6 설치 파일 생성 및 열기
![image](https://github.com/user-attachments/assets/b2436b40-e46f-4fa8-9471-e8d92b349814)

<img src="https://github.com/user-attachments/assets/ac2c9633-c11d-4146-ad17-a1a3eecab108" width="300"/>

### 7 파일생성 확인
<img src="https://github.com/user-attachments/assets/4de1af65-554c-44c9-bfb7-42406c66d755" width="300"/>




