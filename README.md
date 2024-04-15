# study-python
study python
### 기본 문법

### 가상환경 setting
@나도코딩님

(윈도우)

1. 가상 환경 생성
   python -m venv myenv

2. 가상 환경 활성화
   .\myenv\Scripts\activate

- 권한 에러 발생 시
  2-1. Windows PowerShell 관리자로 실행
  2-2. Set-ExecutionPolicy RemoteSigned 입력 후 Y 입력
  2-3. 다시 활성화 시도

3. 패키지 설치
   pip install xlwings

4. 패키지 목록 저장
   pip freeze > requirements.txt

5. vscode 설정
   단축키 : Ctrl + Shift + P
   Python: Select Interpreter 클릭 후 가상 환경 선택 (myenv)

6. 가상 환경 비활성화
   deactivate

7. 가상 환경 폴더 삭제
   rmdir myenv

8. vscode 설정 해제
   단축키 : Ctrl + Shift + P
   Python: Select Interpreter 클릭 후 기존 환경 선택 (글로벌)

9. 공용 공간 패키지 + 가상 환경 생성
   python -m venv myenv --system-site-packages

10. 패키지 설치 (파일로부터)
    pip install -r requirements.txt

11. 가상 환경 내 패키지 목록 조회
    pip list --local

---

(맥)

1. 가상 환경 생성
   python3 -m venv myenv

2. 가상 환경 활성화
   source myenv/bin/activate

3. 패키지 설치
   pip3 install xlwings

4. 패키지 목록 저장
   pip3 freeze > requirements.txt

5. vscode 설정
   단축키 : Command + Shift + P
   Python: Select Interpreter 클릭 후 가상 환경 선택 (myenv)

6. 가상 환경 비활성화
   deactivate

7. 가상 환경 폴더 삭제
   rm -rf myenv

8. vscode 설정 해제
   단축키 : Command + Shift + P
   Python: Select Interpreter 클릭 후 기존 환경 선택 (글로벌)

9. 공용 공간 패키지 + 가상 환경 생성
   python3 -m venv myenv --system-site-packages

10. 패키지 설치 (파일로부터)
    pip3 install -r requirements.txt

11. 가상 환경 내 패키지 목록 조회
    pip3 list --local

### anaconda (macOS) setting
https://velog.io/@yoonsy/Homebrew%EB%A1%9C-Anaconda-%EC%84%A4%EC%B9%98-%EB%B0%8F-conda-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%85%8B%ED%8C%85%ED%95%98%EA%B8%B0

- jupyter notebook

 $ jupyter notebook
- terminal에서 다음 명령어 치기