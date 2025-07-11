# fingercounter.py

TIP_IDS = [4, 8, 12, 16, 20]

def count_fingers(hand_landmarks, hand_type, img_shape):
    """
    Hitung jumlah jari yang terangkat dari satu tangan
    """
    h, w, _ = img_shape
    lm = hand_landmarks.landmark

    def px(id):
        return int(lm[id].x * w), int(lm[id].y * h)

    finger_up = [0] * 5

    # Cek jempol (horizontal)
    if hand_type == 'Right':
        finger_up[0] = px(4)[0] > px(3)[0]
    else:
        finger_up[0] = px(4)[0] < px(3)[0]

    # Cek 4 jari lain (vertical)
    for i in range(1, 5):
        finger_up[i] = px(TIP_IDS[i])[1] < px(TIP_IDS[i] - 2)[1]

    return sum(finger_up)
