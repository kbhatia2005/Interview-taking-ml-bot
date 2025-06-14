import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import pickle
import time

# Load model and vectorizer
with open('logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

recognizer = sr.Recognizer()

def speak(text, filename="temp.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand. Please try again.")
            return listen()

def detect_yes_or_no(text):
    if "yes" in text or "yeah" in text or "yup" in text:
        return "yes"
    elif "no" in text or "not" in text:
        return "no"
    return "unknown"

def start_interview():
    # 1. Greet & Name
    speak("Welcome to the interview. Please tell me your name.")
    name = listen()
    speak(f"Nice to meet you {name}.")

    # 2. Bot Intro
    speak("I am Priyanka, version 3.0, the artificial intelligence interview bot of Bahra University.")
    speak("I was developed by Karan Bhatia.")
    speak("Today, I will be taking your interview for the Python developer position.")

    # 3. Ask prior experience
    speak("Can you tell me, have you studied Python or programming before?")
    prior = listen()

    if detect_yes_or_no(prior) == "yes":
        speak("Great! Where did you study it means from internet sources or books ")
        place = listen()
        speak(f"Studying from {place} will definitely help you crack this interview.")
    else:
        speak("This interview might be a bit challenging for you, but do your best.")

    # 4. Ask OOP knowledge
    speak("Do you know about OOP concepts?")
    oop_ans = listen()

    if detect_yes_or_no(oop_ans) == "yes":
        speak("How much do you know? Say fifty to seventy five or seventy five to one hundred.")
        range_know = listen()
        speak(f"Good, having {range_know} percent knowledge will help.")
    else:
        speak("Okay, don't worry. Let's see how well you can handle the basics.")

    # 5. Interview Instruction
    speak("We will now begin with ten basic Python technical questions.")
    speak("If you are ready, please say: Yes, I am ready.")
    ready = listen()
    if "yes" not in ready:
        speak("Okay, please run the program again when you're ready.")
        return

    # 6. Start Questions
    questions = [
        "What is Python?",
        "What is a list in Python?",
        "What is a function?",
        "What is a loop?",
        "What is inheritance?",
        "What is an object?",
        "What is recursion?",
        "What is pip in Python?",
        "What is indentation?",
        "What is a dictionary?"
    ]

    correct = 0
    for i, question in enumerate(questions):
        speak(f"Question {i+1}: {question}")
        answer = listen()

        if "i don't know" in answer or "no idea" in answer:
            speak("It's okay to not know everything. Let's move to the next question.")
            continue

        X_test = vectorizer.transform([answer])
        prob = model.predict_proba(X_test)[0]
        pred = model.predict(X_test)[0]

        if prob[pred] < 0.6:
            speak("Hmm... I'm not fully convinced with your answer.")
        elif pred == 1:
            speak("Great! You seem to know that well.")
            correct += 1
        else:
            speak("That’s not quite right, but don’t worry.")

        time.sleep(1)

    # 7. Final Result
    speak(f"Interview completed. You answered {correct} out of 10 questions correctly.")

    if correct >= 6:
        speak(f"🎉 Congratulations {name}, you are selected for the next round.")
        speak("Your HR round is scheduled on 8th June 2025.")
    else:
        speak(f"Sorry {name}, you are not selected. Better luck next time!")

if __name__ == "__main__":
    start_interview()
