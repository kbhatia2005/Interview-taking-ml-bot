# 🤖 Voice-Based Interview Bot using Machine Learning

![Interview Bot Flowchart](![bot](https://github.com/user-attachments/assets/5ab52662-e0cd-49bc-a98e-2a92ab13b82e)
)

This project is a **Voice-Based Interview Taking Bot** that conducts technical interviews by asking questions using voice, listening to spoken answers, and predicting correctness using a machine learning model.

🎥 **Demo Video:**  
[![Watch on YouTube](https://img.shields.io/badge/Watch%20Demo%20on-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/c61faWght-0?si=i3xiKb1_GDzvDBDm)

---

## 🔧 Key Features

- 🎤 **Voice Interaction**
  - Questions spoken using `gTTS`
  - Answers captured and converted using `SpeechRecognition`

- 🧠 **Machine Learning Evaluation**
  - Uses `Logistic Regression` to classify answers as Right or Wrong

- 🌐 **Web Scraping**
  - Questions are collected dynamically using `BeautifulSoup` and `requests`

- 📊 **Live Score Prediction**
  - Each answer is evaluated, and feedback is given instantly

---

## 🛠️ Libraries Used

| Category            | Libraries                                      |
|---------------------|------------------------------------------------|
| Voice               | `gTTS`, `playsound`, `SpeechRecognition`, `pyaudio` |
| ML & Data Handling  | `scikit-learn`, `pandas`, `numpy`              |
| Web Scraping        | `requests`, `BeautifulSoup4`                   |

---

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kbhatia2005/interview-bot.git
   cd interview-bot
