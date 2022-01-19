import sys
import noisereduce as nr
import numpy
import numpy as np
import pyaudio
from kivy.app import App
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window
import kivy.event
import urllib.request
import urllib
import soundfile as sf
import io
import threading
from kivy.graphics import Rectangle
import wave
from kivy.config import Config
kivy.config.Config.set('graphics','resizable', False)








#enable_trigger()

class Touch(Widget):
    def enable_trigger(self):
        #trigger = True  # trigger of filter, defaulted as true
        global trigger
        trigger = True  # repeat the same thing because i'm not sure if you declare the variable global before or after it's creation
    enable_trigger(True)
    Clock.schedule_once(enable_trigger)

    def enable_audio(self):
        #audio = True    # audio enabled or not, defaulted as true
        global audio
        audio = True  # repeat the same thing because i'm not sure if you declare the variable global before or after it's creation
    enable_audio(True)
    print(audio)
    Clock.schedule_once(enable_audio)

    def mutething(audio):
        #   enable_audio(True)
        if audio == True:
            audio = False
            print(audio)
        elif audio == False:
            audio = True
            print(audio)

    def helpme(trigger):
        CHUNK = 21600
        FORMAT = pyaudio.paInt32
        CHANNELS = 1
        RATE = 48000
        p = pyaudio.PyAudio()

        #stream = p.open(format=FORMAT,
                        #channels=CHANNELS,
                        #rate=RATE,
                        #input=True,
                        #output=True,
                        #frames_per_buffer=CHUNK)
        frames = []
        data = stream.read(CHUNK)
        # change the format to numpy int16
        frames.append(np.fromstring(data, dtype=np.int16))
        # newS = np.fromstring(frames,dtype=np.int16)
        url = "https://raw.githubusercontent.com/timsainb/noisereduce/master/assets/cafe_short.wav"
        response = urllib.request.urlopen(url)
        noise_data, noise_rate = sf.read(io.BytesIO(response.read()))
        snr = 2  # signal to noise ratio
        noise_clip = noise_data / snr
        reduced_noise = nr.reduce_noise(y=frames, sr=RATE, y_noise=noise_clip, prop_decrease=0,
                                        freq_mask_smooth_hz=65534, n_std_thresh_stationary=1300, n_fft=2048,
                                        sigmoid_slope_nonstationary=100, thresh_n_mult_nonstationary=1.5,
                                        stationary=True)
        reduced_data = bytes(reduced_noise)
        stream.write(reduced_data, CHUNK)
        print()

    def configure_stream(self):
        global CHUNK
        CHUNK = 21600
        global FORMAT
        FORMAT = pyaudio.paInt32
        global CHANNELS
        CHANNELS = 1
        global RATE
        RATE = 48000
        global p
        p = pyaudio.PyAudio()

        global stream
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=True,
                        frames_per_buffer=CHUNK)

    def end_stream(self):
        stream.stop_stream()
        stream.close()
        p.terminate()

    #def dosomething(self):
        #print(audio)

    #Clock.schedule_interval(dosomething, .1)
    if audio == True:
        Clock.schedule_once(configure_stream)
        Clock.schedule_interval(helpme, .1)
    elif audio == False:
        Clock.schedule_once(end_stream)


    def button_scaling(self):
        btn = Button(on_press=None)    #frames.append(data)
        btn1 = Button(on_press=mutething(audio))
        btn2 = Button(on_press=None)
        btn3 = Button(on_press=None)

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        #with self.canvas:
            #Color(1, 1, 1, .5, mode='rgba')
            #self.help = Rectangle(source=("button (2).png"), pos=(432,734), size=(332.5,100))
            #self.me = Rectangle(source=("button (2).png"), pos=(432,576), size=(332.5,100))
            #self.pls = Rectangle(source=("button (2).png"), pos=(432,406), size=(332.5,100))
            #self.iwantdie = Button(source=("button (2).png"), pos=(432,218), size=(332.5,100))

    #def on_touch_down(self, touch):
        #self.help.pos = touch.pos
        #print("Mouse Down", touch)

    #def on_touch_move(self, touch):
        #self.help.pos = touch.pos
        #print("Mouse Move", touch)

    #def on_touch_up(self, touch):
        #self.help.pos = touch.pos
        #print("Mouse Up", touch)

    #global Toggle
    #Toggle = True
    #print (Toggle)
    #def triggerfilter(toggle=True):
        #if toggle == True:
            #toggle = False
        #elif toggle == False:
            #toggle = True
        #return toggle

    #def enable_trigger(self):
        #trigger = True
        #global trigger
        #trigger = True


    #def triggerfilter(self):
        #if trigger == True:
            #trigger = False
        #elif trigger == False:
            #trigger = True







    #helpme(True)






#class helpmebro(Widget):
    #name = ObjectProperty(None)
    #email = ObjectProperty(None)

    #def btn(self):
        #print("Name:", self.name.text, "Email:", self.email.text)
        #self.name.text = ""
        #self.email.text = ""




class ThirdApp(App):
    def build(self):
        #windowsize = numpy.array(Window.size)
        #width = windowsize[0]
        #height = windowsize[1]
        #print('Width', width)
        #print('Height', height)

        def enable_trigger(self):
            # trigger = True  # trigger of filter, defaulted as true
            global trigger
            trigger = True  # repeat the same thing because i'm not sure if you declare the variable global before or after it's creation

        enable_trigger(True)
        Clock.schedule_once(enable_trigger)

        def enable_audio(self):
            # audio = True    # audio enabled or not, defaulted as true
            global audio
            audio = True  # repeat the same thing because i'm not sure if you declare the variable global before or after it's creation

        enable_audio(True)
        Clock.schedule_once(enable_audio)
        return Touch()


if __name__ == "__main__":
    ThirdApp().run()
