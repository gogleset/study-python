import speech_recognition as sr
r = sr.Recognizer() # 인식 소프트웨어
with sr.Microphone() as source:
    print('듣고 있습니다...')
    audio = r.listen(source) # 마이크로부터 음성을 저장

try:
    # Bing API로 인식
    text = r.recognize_bing(audio_data=audio, language="en-US")
    print(text)
    pass
except sr.UnknownValueError:
    print("인식 실패")
except sr.RequestError as e:
    print("요청 실패: {0}".format(e)) # API KEY ERROR, 또는 네트워크 에러