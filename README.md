# ✊✋✌️ Rock Paper Scissors using Hand Gestures

A real-time **Rock Paper Scissors** game powered by **Computer Vision** and **Hand Gesture Recognition**. The game uses your webcam to detect hand gestures with **MediaPipe**, allowing you to play against the computer without touching the keyboard or mouse.

The first player to win **3 rounds (Best of 5)** wins the match.

---

## 📌 Features

- 🎥 Real-time hand gesture recognition using a webcam
- ✋ Supports Rock, Paper, and Scissors gestures
- 🤖 Computer opponent with random move generation
- 🏆 Best-of-5 game mode (First to 3 wins)
- 📊 Live score tracking
- 🖼️ Displays the computer's selected move with images
- ⏳ Countdown timer before each round
- 🔄 Restart game without closing the application
- 🖥️ Full-screen gaming interface

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- Random
- Time
- OS Module

---

## 📂 Project Structure

```text
Rock-Paper-Scissors-Hand-Gesture/
│
├── assets/
│   ├── rock.png
│   ├── paper.png
│   └── scissors.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/koushik995/Gesture_Rock_Paper_Scissors.git

cd Gesture_Rock_Paper_Scissors
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install opencv-python mediapipe
```

---

## ▶️ Run the Project

```bash
python main.py
```

Ensure your webcam is connected before launching the game.

---

# 🎮 How to Play

1. Start the application.
2. Show one of the supported hand gestures in front of the webcam.
3. A countdown begins before each round.
4. The computer randomly selects its move.
5. The winner of the round is displayed.
6. The first player to reach **3 wins** wins the match.
7. Press **R** to restart or **Q** to quit.

---

# ✋ Supported Gestures

| Hand Gesture | Detected Move |
|--------------|---------------|
| ✊ Closed Fist | Rock |
| ✌️ Two Fingers | Scissors |
| 🖐️ Open Hand | Paper |

---

## 🧠 How It Works

1. Captures live video using OpenCV.
2. Detects hand landmarks using MediaPipe.
3. Counts the number of raised fingers.
4. Maps the detected gesture to Rock, Paper, or Scissors.
5. Generates a random computer move.
6. Compares both moves to determine the winner.
7. Updates the scoreboard and continues until one player reaches three wins.

---

## 📸 Gameplay

During gameplay, the application displays:

- Live webcam feed
- Hand landmarks
- Current detected gesture
- Countdown timer
- Computer's move
- Round result
- Player score
- Computer score
- Draw count

---

## 🚀 Future Improvements

- Difficulty levels
- Sound effects and background music
- Animated transitions
- Multiplayer mode
- AI opponent using Machine Learning
- Gesture confidence indicator
- Match history and statistics
- Custom game modes (Best of 3, Best of 7)

---

## 📋 Requirements

- Python 3.9 or above
- Webcam
- Windows, Linux, or macOS

---

## 📦 Requirements File

```text
opencv-python
mediapipe
```

---

## 📷 Demo

You can add:

- Gameplay screenshots
- Demo GIF
- Screen recording

Example:

```text
demo.gif
screenshots/
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## ⭐ Support

If you enjoyed this project, please consider giving it a **⭐ Star** on GitHub.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Koushik**
GitHub: https://github.com/koushik995
Feel free to connect and contribute to improve the project.
````
