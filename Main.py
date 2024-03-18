import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound


def recognize_speech(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


def translate_text(text, target_language="fr"):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.origin, translated_text.text


def text_to_speech(text, output_file_path):
    tts = gTTS(text, lang="en")
    tts.save(output_file_path)


def speech_to_text_translation(audio_file_path, target_language="fr"):
    # Speech-to-Text
    recognized_text = recognize_speech(audio_file_path)

    # Translate
    original_text, translated_text = translate_text(recognized_text, target_language=target_language)

    return original_text, translated_text


def text_to_speech_and_play(text):
    output_file_path = "output.mp3"
    text_to_speech(text, output_file_path)
    playsound.playsound(output_file_path)


if __name__ == "__main__":
    audio_file_path = "C:\\StoS\\wheels.wav"

    original_text, translated_text = speech_to_text_translation(audio_file_path, target_language="es")

    print(f"Original Text: {original_text}")
    print(f"Translated Text: {translated_text}")

    text_to_speech_and_play(translated_text)
