import subprocess
import threading
import time
import os
import re
import contractions
from nltk.corpus import cmudict
import nltk
from g2p_en import G2p
from pydub import AudioSegment
from pydub.playback import play

# nltk.download('cmudict', quiet=True)
        
class TTS:
    def __init__(self):
        self.pronouncing_dict = cmudict.dict()
        self.g2p = G2p()
        self._setup()
        
    def _setup(self, pitch_mean=160, pitch_std=15, speed=0.85, delay_per_word=0.3, output_path="output.wav"):
        self.pitch_mean = pitch_mean
        self.pitch_std = pitch_std
        self.speed = speed
        self.delay_per_word = delay_per_word
        self.output_path = output_path

    def __clean_word(self, word):
        word = word.lower()
        word = re.sub(r"[^\w\s]", "", word)
        word = contractions.fix(word)
        return word
    
    def generate_audio(self, text):
        lisp_script = f"""
        (voice_kal_diphone)
        (Parameter.set 'Duration_Stretch {self.speed})
        (Parameter.set 'Int_Target_Mean {self.pitch_mean})
        (Parameter.set 'Int_Target_Stddev {self.pitch_std})
        (set! utt1 (Utterance Text "{text}"))
        (utt.synth utt1)
        (utt.save.wave utt1 "{self.output_path}" 'riff)
        """
        subprocess.run(['festival', '--pipe'], input=lisp_script.encode())
    
    def get_phonemes(self, text):
        words = self.__clean_word(text).split()
        result = []
        
        for word in words:
            try:
                if word in self.pronouncing_dict:
                    phonemes = self.pronouncing_dict[word][0]
                else:
                    phonemes = []
                    for p in self.g2p(word):
                        if p.isalpha():
                            phonemes.append(p)
            except:
                phonemes = "Error"
            result.append((word, phonemes))

        self.word_phonemes = result
    
    def __mimic(self, mouth):
        print("\n--- Speaking ---")
        for word, phonemes in self.word_phonemes:
            phonemes = re.sub(r'[^a-zA-Z\s]', '', ' '.join(phonemes))
            print(f"{word}: {phonemes}")
            for phoneme in phonemes.split(" "):
                self.__phoneme_to_mouth_action(phoneme, mouth)
            
            time.sleep(self.delay_per_word)
    
    def __play_audio(self):
        play(AudioSegment.from_file(self.output_path, format="wav"))
    
    def speak(self, text, mouth, delete_after=True):
        self.generate_audio(text)
        self.get_phonemes(text)
        audio_thread = threading.Thread(target=self.__play_audio)
        mimic_thread = threading.Thread(target=lambda n=mouth: self.__mimic(n))
        audio_thread.start()
        mimic_thread.start()
        audio_thread.join()
        mimic_thread.join()
        
        if delete_after:
            os.remove(self.output_path)

    def __phoneme_to_mouth_action(self, phoneme, mouth):
        phoneme = phoneme.upper()

        if phoneme in ["AA", "AH", "AO"]:
            # Wide open
            mouth.move_jaw(1.0)
            mouth.move_upper_lips(0.5)
            mouth.move_lower_lips(0.5)
            mouth.move_left_lips_corner(1.0)
            mouth.move_right_lips_corner(1.0)

        elif phoneme in ["AE", "EH", "EY", "AY"]:
            # Slightly open and lips spread
            mouth.move_jaw(0.6)
            mouth.move_upper_lips(0.3)
            mouth.move_lower_lips(0.3)
            mouth.move_left_lips_corner(0.7)
            mouth.move_right_lips_corner(0.7)

        elif phoneme in ["B", "P", "M"]:
            # Fully closed
            mouth.move_jaw(0.0)
            mouth.move_upper_lips(0.0)
            mouth.move_lower_lips(0.0)
            mouth.move_left_lips_corner(0.0)
            mouth.move_right_lips_corner(0.0)

        elif phoneme in ["F", "V"]:
            # Lower lip slightly forward
            mouth.move_jaw(0.1)
            mouth.move_upper_lips(0.1)
            mouth.move_lower_lips(0.4)
            mouth.move_left_lips_corner(0.0)
            mouth.move_right_lips_corner(0.0)

        elif phoneme in ["IY", "IH"]:
            # Smile-like expression
            mouth.move_jaw(0.3)
            mouth.move_left_lips_corner(1.0)
            mouth.move_right_lips_corner(1.0)
            mouth.move_upper_lips(0.2)
            mouth.move_lower_lips(0.2)

        elif phoneme in ["OW", "UW", "UH", "AW"]:
            # Rounded lips and jaw open
            mouth.move_jaw(0.5)
            mouth.move_upper_lips(0.6)
            mouth.move_lower_lips(0.6)
            mouth.move_left_lips_corner(0.3)
            mouth.move_right_lips_corner(0.3)

        elif phoneme in ["R", "L", "N", "D", "T", "S", "Z"]:
            # Soft articulation
            mouth.move_jaw(0.4)
            mouth.move_upper_lips(0.2)
            mouth.move_lower_lips(0.2)
            mouth.move_left_lips_corner(0.3)
            mouth.move_right_lips_corner(0.3)

        elif phoneme in ["W", "Y", "OY"]:
            # Subtle round and forward motion
            mouth.move_jaw(0.4)
            mouth.move_upper_lips(0.5)
            mouth.move_lower_lips(0.4)
            mouth.move_left_lips_corner(0.4)
            mouth.move_right_lips_corner(0.4)

        elif phoneme in ["CH", "SH", "JH", "ZH"]:
            # Slight closure and round
            mouth.move_jaw(0.3)
            mouth.move_upper_lips(0.3)
            mouth.move_lower_lips(0.3)
            mouth.move_left_lips_corner(0.2)
            mouth.move_right_lips_corner(0.2)

        elif phoneme in ["TH", "DH"]:
            # Soft open
            mouth.move_jaw(0.3)
            mouth.move_upper_lips(0.3)
            mouth.move_lower_lips(0.3)
            mouth.move_left_lips_corner(0.2)
            mouth.move_right_lips_corner(0.2)
        
        elif phoneme == "ER":
            mouth.move_jaw(0.4)
            mouth.move_upper_lips(0.4)
            mouth.move_lower_lips(0.4)
            mouth.move_left_lips_corner(0.2)
            mouth.move_right_lips_corner(0.2)

        elif phoneme == "HH":
            mouth.move_jaw(0.5)
            mouth.move_upper_lips(0.3)
            mouth.move_lower_lips(0.3)
            mouth.move_left_lips_corner(0.2)
            mouth.move_right_lips_corner(0.2)
            
        else:
            # Default neutral
            mouth.move_jaw(0.3)
            mouth.move_upper_lips(0.3)
            mouth.move_lower_lips(0.3)
            mouth.move_left_lips_corner(0.3)
            mouth.move_right_lips_corner(0.3)
    
    
if __name__=="__main__":
    tts = TTS()
    tts.speak("Hello World")
    
    