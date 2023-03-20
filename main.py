import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab

# Load the target images
target_image_filenames = ['resources/play_button.png', 'resources/end_turn.png', 'resources/next.png',
                          'resources/collect_rewards.png', 'resources/final_turn.png', 'resources/reconnect.png']
target_images = [cv2.imread(filename) for filename in target_image_filenames]

while True:
    # Take a screenshot of the SNAP application
    snap_app = pyautogui.getWindowsWithTitle('SNAP')[0]
    snap_app_rect = snap_app.left, snap_app.top, snap_app.width, snap_app.height
    snap_app_screenshot = np.array(ImageGrab.grab(snap_app_rect))

    # Convert the screenshot to grayscale
    snap_app_screenshot_gray = cv2.cvtColor(snap_app_screenshot, cv2.COLOR_BGR2GRAY)

    # Loop over the target images and try to match each one in the screenshot
    for target_image, target_image_filename in zip(target_images, target_image_filenames):
        # Convert the target image to grayscale
        target_image_gray = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

        # Match the template image in the screenshot
        result = cv2.matchTemplate(snap_app_screenshot_gray, target_image_gray, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        positions = np.where(result >= threshold)
        if len(positions[0]) > 0:
            # Click on the center of the first match
            target_x, target_y = pyautogui.center((positions[1][0], positions[0][0], target_image.shape[1], target_image.shape[0]))
            pyautogui.click(target_x, target_y)
            print(f"Clicked on {target_image_filename}")
            break

    # Wait for a short time before taking the next screenshot
    time.sleep(1)
    