import threading

import nls
import pyaudio
from flask import Blueprint

listen_bp = Blueprint('listen', __name__)

URL = "wss://nls-gateway.cn-shanghai.aliyuncs.com/ws/v1"
AKID = "LTAI5t6fq9nRwt8FVYS9bpS6"
AKKEY = "B3mtT8a6aNx45W3xV1MVNrv1yn0f9t"
APPKEY = "W7LavLPl8y2FuzjS"

# TEXT = '大壮正想去摘取花瓣，谁知阿丽和阿强突然内讧，阿丽拿去手枪向树干边的阿强射击，两声枪响，阿强直接倒入水中'
global uid


# 以下代码会根据上述TEXT文本反复进行语音合成
class TestTts:
    def __init__(self, tid, test_file):
        self.__th = threading.Thread(target=self.__test_run)
        self.__id = tid
        self.__test_file = test_file

    def start(self, text):
        self.__text = text
        self.__f = open(self.__test_file, "wb")
        self.__th.start()

    def test_on_metainfo(self, message, *args):
        print("on_metainfo message=>{}".format(message))

    def test_on_error(self, message, *args):
        print("on_error args=>{}".format(args))

    def test_on_close(self, *args):
        print("on_close: args=>{}".format(args))
        try:
            self.__f.close()
        except Exception as e:
            print("close file failed since:", e)

    def test_on_data(self, data, *args):
        try:
            self.__f.write(data)
        except Exception as e:
            print("write data failed:", e)

    def test_on_completed(self, message, *args):
        print("on_completed:args=>{} message=>{}".format(args, message))

    def __test_run(self):
        print("thread:{} start..".format(self.__id))
        tts = nls.NlsSpeechSynthesizer(
            url=URL,
            akid=AKID,
            aksecret=AKKEY,
            appkey=APPKEY,
            on_metainfo=self.test_on_metainfo,
            on_data=self.test_on_data,
            on_completed=self.test_on_completed,
            on_error=self.test_on_error,
            on_close=self.test_on_close,
            callback_args=[self.__id]
        )

        print("{}: session start".format(self.__id))
        r = tts.start(self.__text, voice="ruoxi")
        print("{}: tts done with result:{}".format(self.__id, r))


@listen_bp.route('/api/listen')
def multiruntest(txt):
    TEXT = txt
    num = 500
    i = range(0, num)
    name = "thread" + str(i)
    t = TestTts(name, "tests/test_tts.pcm")
    t.start(TEXT)
    nls.enableTrace(True)


@listen_bp.route('/api/play')
def play():
    # 初始化播放器
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=16000, output=True)

    # 将 pcm 数据直接写入 PyAudio 的数据流
    with open("tests/test_tts.pcm", "rb") as f:
        stream.write(f.read())
    stream.stop_stream()
    stream.close()
    p.terminate()
    return 200
