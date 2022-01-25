import sys
import speech_recognition
import pyttsx3 as tts
from smart import GenericAssistant

recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 180)

todo_list = ["Listen to music", "complete this project"]


def Create_a_note():
    global recognizer

    speaker.say("What do you want to write on to your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a file name:")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you . Please repeat again")
            speaker.runAndWait()


def add_todo():
    global recognizer

    speaker.say("What should i add to your todo list?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                todo = recognizer.recognize_google(audio)
                todo = todo.lower()

                speaker.say("Sir, where do you want to add your to-do list?")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filname, 'w') as f:
                f.write(todo)
                done = True
                speaker.say("have successfully creted your todo list")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you . Please repeat again")
            speaker.runAndWait()


def show_todo():
    speaker.say("The items on your to do list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("Hello! What can i do for you?")
    speaker.runAndWait()


def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello(),
    "create_note": Create_a_note(),
    "add_todo": add_todo(),
    "show_todos": show_todo(),
    "exit": quit(),
}

assistant = GenericAssistant('chatbot.json')
assistant.train_model()

assistant.request("How are you?")

while True:
    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
