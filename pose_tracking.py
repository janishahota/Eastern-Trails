import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Store previous foot & knee positions
prev_left_y, prev_right_y = None, None
prev_left_knee_y, prev_right_knee_y = None, None

movement_threshold = 0.02  # Reduced for better sensitivity
stability_factor = 0.015  # Slightly more relaxed

def detect_leg_movement(frame):
    global prev_left_y, prev_right_y, prev_left_knee_y, prev_right_knee_y

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        left_foot = landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
        right_foot = landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
        left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
        right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE]

        left_y, right_y = left_foot.y, right_foot.y
        left_knee_y, right_knee_y = left_knee.y, right_knee.y

        if None in (prev_left_y, prev_right_y, prev_left_knee_y, prev_right_knee_y):
            prev_left_y, prev_right_y = left_y, right_y
            prev_left_knee_y, prev_right_knee_y = left_knee_y, right_knee_y
            return False  # First frame, no movement detected

        # Measure displacement
        left_foot_movement = abs(left_y - prev_left_y)
        right_foot_movement = abs(right_y - prev_right_y)
        left_knee_movement = abs(left_knee_y - prev_left_knee_y)
        right_knee_movement = abs(right_knee_y - prev_right_knee_y)

        # Update previous positions
        prev_left_y, prev_right_y = left_y, right_y
        prev_left_knee_y, prev_right_knee_y = left_knee_y, right_knee_y

        # **Walking Detection**
        walking_detected = (
            (left_foot_movement > movement_threshold and right_foot_movement < stability_factor) or
            (right_foot_movement > movement_threshold and left_foot_movement < stability_factor)
        ) and (
            left_knee_movement > stability_factor or right_knee_movement > stability_factor
        )

        return walking_detected  # True if movement is detected

    return False
