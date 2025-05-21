import speech_recognition as sr
import time

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.text = None
        self._stop_listening = None
        # self.setup()

    def setup(self, energy_threshold=150, dynamic_energy_threshold=False, pause_threshold=0.8):
        self.recognizer.energy_threshold = energy_threshold
        self.recognizer.dynamic_energy_threshold = dynamic_energy_threshold
        self.recognizer.pause_threshold = pause_threshold
    
    def callback(self, recognizer, audio):
        try:
            self.text = recognizer.recognize_google(audio)
            print("You said: " + self.text)
        except sr.UnknownValueError:
            print("Could not understand audio")
            self.text = ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            self.text = ""
            return None
        
    def start_listening(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            
        self._stop_listening = self.recognizer.listen_in_background(self.microphone, self.callback)
        print("Speak now...")
        
    def stop_listening(self):
        if self._stop_listening != None:
            self._stop_listening(wait_for_stop=False)
            self._stop_listening = None
            print("Stopped Listening ")
            return self.text
            
    def listening_until_stop_speaking(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Speak now...")
            audio = self.recognizer.listen(source)
        
        self.callback(self.recognizer, audio)
        return self.text
    
    def write(self):
        try:
            with open("microphone-results.wav", "wb") as f:
                f.write(self.audio.get_wav_data())
        except:
            print("Failed writing audio file.")

if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    
    recognizer.listening_until_stop_speaking()
    
    time.sleep(2)
    
    recognizer.start_listening()
    
    for _ in range(500):
        time.sleep(0.1)
        
    recognizer.stop_listening()
