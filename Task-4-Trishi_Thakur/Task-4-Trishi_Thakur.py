import cv2
import numpy as np
import urllib.request
import os

# --- 1. NETWORK CONFIGURATION & SYSTEM INITIALIZATION ---
PROTOTXT = "MobileNetSSD_deploy.prototxt"
MODEL = "MobileNetSSD_deploy.caffemodel"

# Verify files exist locally
if not os.path.exists(PROTOTXT) or not os.path.exists(MODEL):
    raise FileNotFoundError("Missing architecture files! Run the curl commands to download them.")

# Load the deep learning pre-trained framework [cite: 45, 134]
print("[INFO] Loading MobileNet-SSD architecture from cache...")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)

# Standard VOC target classes dataset labels
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Strict metric filter matching milestone criteria 
CONFIDENCE_THRESHOLD = 0.80  


# --- 2. CORE DETECTION & RENDERING LOGIC ---
def process_and_display(frame, window_name="DecodeLabs AI Vision"):
    """
    Constructs a 4D blob from the image matrix, pipes it to the model, 
    and overlays bounding boxes on entities passing the 80% baseline gate.
    """
    h, w = frame.shape[:2]
    
    # Step 1: 4D Blob Construction (Scaling to network specifications 300x300) [cite: 82, 138]
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward() # Execute forward-pass inference
    
    # Step 2: Extract normalized spatial metrics from output matrix loop [cite: 143, 144]
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        # Enforce the strict 80% validation gate rule 
        if confidence >= CONFIDENCE_THRESHOLD:
            class_id = int(detections[0, 0, i, 1])
            label = CLASSES[class_id]
            
            # Step 3: Decode and translate coordinates back to pixel scaling [cite: 145, 149]
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            # Formulate text details and draw bounding overlays on matrix frames
            display_text = f"{label.upper()}: {confidence * 100:.1f}%"
            
            # Draw the green bounding box
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            
            # Boosted text scale from 0.5 to 1.2, and thickness from 2 to 3
            cv2.putText(frame, display_text, (startX + 10, startY + 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            
    cv2.imshow(window_name, frame)


def stream_video(source_path_or_idx, is_live=False):
    """
    Handles streaming for sequential frames (Webcam, saved Video files, or video URLs)
    """
    print(f"[INFO] Initializing visual input capture stream...")
    cap = cv2.VideoCapture(source_path_or_idx)
    
    if not cap.isOpened():
        print("[ERROR] Could not open or read the specified video matrix feed.")
        return

    print("-> Press 'q' on your keyboard to exit the stream window safely.")
    while True:
        ret, frame = cap.read()
        if not ret:
            if is_live:
                print("[WARNING] Frame dropped from live source stream.")
            else:
                print("[INFO] Video stream playback sequence complete.")
            break
            
        process_and_display(frame, "Continuous Array Pipeline")
        
        # Keep window running; check if user requests 'q' termination
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("[INFO] Stream terminated manually by user command.")
            break
            
    cap.release()
    cv2.destroyAllWindows()


# --- 3. EXECUTION PATHWAY GATE ---
if __name__ == "__main__":
    print("\n==============================================")
    print("   DECODELABS: AI OPTIC NERVE PLAYGROUND")
    print("==============================================")
    print("1. Local Image File (.jpg, .png)")
    print("2. Web Image URL (Direct link)")
    print("3. Live Webcam Feed")
    print("4. Saved Local Video File (.mp4, .avi)")
    
    choice = input("\nSelect an input format option (1-4): ").strip()
    
    if choice == '1':
        path = input("Enter your local image path (e.g., street.jpg): ").strip()
        img = cv2.imread(path)
        if img is not None:
            process_and_display(img, "Static Image Output Matrix")
            print("[INFO] Showing detection. Press any key on image window to exit.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("[ERROR] Valid image array could not be found at destination path.")
            
    elif choice == '2':
        url = input("Paste your target image URL: ").strip()
        try:
            print("[INFO] Requesting remote matrix data over HTTP network...")
            req = urllib.request.urlopen(url)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1) # Convert byte data to raw pixel matrix
            if img is not None:
                process_and_display(img, "URL Image Output Matrix")
                print("[INFO] Showing detection. Press any key on image window to exit.")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            else:
                print("[ERROR] Ingested network payload was not recognized as a valid image format.")
        except Exception as e:
            print(f"[ERROR] Connection failed to fetch content: {e}")
            
    elif choice == '3':
        # Default local hardware camera index is typically 0
        stream_video(0, is_live=True)
        
    elif choice == '4':
        video_path = input("Enter your local video file path (e.g., traffic.mp4): ").strip()
        stream_video(video_path, is_live=False)
        
    else:
        print("[ERROR] Invalid choice index entered. Aborting pipeline process execution sequence.")