import cv2
import mediapipe as mp
import random
import time
import os

# -----------------------------
# Camera
# -----------------------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# -----------------------------
# MediaPipe
# -----------------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# -----------------------------
# Load Images (JPG + PNG support)
# -----------------------------
def load_img(name):
    for ext in ["jpg", "jpeg", "png"]:
        path = f"assets/{name}.{ext}"
        if os.path.exists(path):
            img = cv2.imread(path)
            return cv2.resize(img, (180, 180))
    return None

rock_img = load_img("rock")
paper_img = load_img("paper")
scissors_img = load_img("scissors")

# -----------------------------
# Game Variables (BEST OF 5)
# -----------------------------
player_score = 0
computer_score = 0
draws = 0

choices = ["Rock", "Paper", "Scissors"]

gesture = "Unknown"
computer_move = ""
result = ""

ROUND_TIME = 3
RESULT_TIME = 2

round_start = time.time()
round_done = False
result_start = 0

game_over = False
winner_text = ""

# -----------------------------
# Winner Logic
# -----------------------------
def decide(player, comp):
    if player == comp:
        return "Draw"
    if (player == "Rock" and comp == "Scissors") or \
       (player == "Paper" and comp == "Rock") or \
       (player == "Scissors" and comp == "Paper"):
        return "Win"
    return "Lose"

# -----------------------------
# Fullscreen
# -----------------------------
cv2.namedWindow("RPS PRO", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("RPS PRO", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# -----------------------------
# Main Loop
# -----------------------------
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    # ---------------- HAND TRACKING ----------------
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hands.process(img_rgb)

    gesture = "Unknown"

    if res.multi_hand_landmarks:
        for hand in res.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            lm = []
            for p in hand.landmark:
                lm.append((int(p.x * w), int(p.y * h)))

            fingers = 0
            if lm[8][1] < lm[6][1]: fingers += 1
            if lm[12][1] < lm[10][1]: fingers += 1
            if lm[16][1] < lm[14][1]: fingers += 1
            if lm[20][1] < lm[18][1]: fingers += 1

            if fingers == 0:
                gesture = "Rock"
            elif fingers == 2:
                gesture = "Scissors"
            elif fingers >= 4:
                gesture = "Paper"

    # ---------------- GAME FLOW ----------------
    if not game_over:

        if not round_done:
            t = int(ROUND_TIME - (time.time() - round_start))

            if t > 0:
                cv2.putText(img, str(t), (600, 350),
                            cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,255), 8)
            else:
                if computer_move == "":
                    if gesture in choices:
                        computer_move = random.choice(choices)

                        r = decide(gesture, computer_move)

                        if r == "Win":
                            result = "YOU WIN"
                            player_score += 1
                        elif r == "Lose":
                            result = "COMPUTER WINS"
                            computer_score += 1
                        else:
                            result = "DRAW"
                            draws += 1
                    else:
                        result = "NO GESTURE"

                round_done = True
                result_start = time.time()

        else:
            if time.time() - result_start > RESULT_TIME:
                round_start = time.time()
                round_done = False
                computer_move = ""
                result = ""

    # ---------------- BEST OF 5 ----------------
    if player_score >= 3:
        game_over = True
        winner_text = "YOU WON MATCH!"
    elif computer_score >= 3:
        game_over = True
        winner_text = "COMPUTER WON MATCH!"

    # ---------------- UI PANEL ----------------
    cv2.rectangle(img, (0,0), (420,260), (30,30,30), -1)

    cv2.putText(img, f"Gesture: {gesture}", (10,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(img, f"Result: {result}", (10,80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    cv2.putText(img, f"You: {player_score}", (10,130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(img, f"CPU: {computer_score}", (150,130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.putText(img, f"Draws: {draws}", (300,130),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

    # ---------------- COMPUTER IMAGE ----------------
    if computer_move:
        cimg = None

        if computer_move == "Rock":
            cimg = rock_img
        elif computer_move == "Paper":
            cimg = paper_img
        elif computer_move == "Scissors":
            cimg = scissors_img

        if cimg is not None:
            img[50:230, w-200:w-20] = cimg
            cv2.putText(img, "COMPUTER", (w-200, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    # ---------------- GAME OVER SCREEN ----------------
    if game_over:
        cv2.rectangle(img, (250,250), (1100,450), (0,0,0), -1)
        cv2.putText(img, winner_text, (350,330),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255), 4)
        cv2.putText(img, "Press R to Restart / Q to Quit", (300,400),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    cv2.imshow("RPS PRO", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if key == ord('r'):
        player_score = 0
        computer_score = 0
        draws = 0
        game_over = False
        computer_move = ""
        result = ""
        round_start = time.time()
        round_done = False

cap.release()
cv2.destroyAllWindows()
