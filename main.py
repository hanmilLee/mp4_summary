import whisper #https://github.com/openai/whisper
import urllib3

dwn_link = 'https://fastcamp.video.kr.kollus.com/kr/media-file.mp4?_s=d9f0d36c18830a62c64c964d15f75a8af7ee20551468a2b0ba6fa39ca4e969cecc7651eaf6ad0b94cbb7c984077d73269a8b648d315982ee75012bc543ec369972e854db479075bcaef6c6904cb0d1d4ce0d6382f7098f9a78b789b788e35ca19a11217b11823e43db5cf0455ecbf408c3231f25e2036d52eecadf038c8db868182819a97c000176cb6b16a772ed62eb788991525a1e3901c8661cf72e701566e6a3b8d0d54beb5cf0114eeed8b1ae7ed7820fd4ae86919b7fd658dd4ccb9e58baee8133abf5898ca82fefcf7f1a410d5ad6825d9c35c0180b6b99893ab27b35bba44b84279a4e532ec466a89f1d8a65fd6b5625df1db2279c8435b61f364081548142daa385333af7c72e3ff91260013670ae843a6ecd0529bfb5d9684ed287cb8c9d729cb898ffbe427ccf579679eb20016f14c88f72cc347e05b7b2798fc6f49c4221d32ae7a5253f8fe3991969f24c0df61059732073d05afc1afa6d9c4b80c42046f0520e1a217c79cdfdcd84e3&channelkey=xu3rmt6gvvks45ky'
file_name = 'CH01_01.데이터엔지니어링이란'



http = urllib3.PoolManager()
with http.request('GET', dwn_link, preload_content=False) as r, open(file_name + '.mp4', 'wb') as out_file:
    while True:
        data = r.read(1024)
        if not data:
            break
        out_file.write(data)

r.release_conn()

model = whisper.load_model('base')
result = model.transcribe(file_name +'.mp4')



with open(file_name + "_script.txt", "w") as text_file:
    text_file.write(result['text'])