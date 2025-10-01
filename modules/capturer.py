from typing import Any
import cv2
import modules.globals  # Import the globals to check the color correction toggle


def get_video_frame(video_path: str) -> Any:
    """Grab a single frame from a stream or video device."""
    capture = cv2.VideoCapture(video_path)

    # Set MJPEG format for better color handling
    capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    has_frame, frame = capture.read()

    if has_frame and modules.globals.color_correction:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    capture.release()
    return frame if has_frame else None


def get_video_frame_total(video_path: str) -> int:
    """For streams this will return -1, works only for local files."""
    capture = cv2.VideoCapture(video_path)
    frame_total = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    capture.release()
    return frame_total
