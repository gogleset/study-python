# TTS (Text To Speech)
# STT (Speech To Text)
from gtts import gTTS
from playsound import playsound

# 영어 문장
# text = "Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight."
# file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang="en") # tts 전환
# tts_en.save(file_name) # 음성 저장
# playsound(file_name) # 음성 출력

# 한글 문장
# ko_file_name = 'sample_ko.mp3'
# ko_text = "파이썬을 배우면 이런 것도 할 수 있어요"
# tts_ko = gTTS(text=ko_text, lang="ko")
# tts_ko.save(ko_file_name)
# playsound(ko_file_name)

# 긴 문장(파일에서 불러와서 처리)
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

file_name = 'txt_file_sample.mp3'
tts_en = gTTS(text=text, lang="en") # tts 전환
tts_en.save(file_name) # 음성 저장
playsound(file_name) # 음성 출력