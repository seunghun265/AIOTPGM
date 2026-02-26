# 다운로드 폴더에 있는 실행파일을 지정된 디렉토리로 이동하는 파이썬 코드 작성해줘

import os
import shutil

source_dir = r"[다운로드 폴더의 주소]"
dest_dir = r"[설치 파일 모음 폴더의 주소]"

for file_name in os.listdir(source_dir):
    if file_name.endswith(".exe"):
        shutil.move(os.path.join(source_dir, file_name), dest_dir)