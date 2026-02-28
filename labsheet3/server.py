import socket
import cv2
import threading
import os
import pickle
import struct

HOST = '0.0.0.0'
PORT = 9999
VIDEO_DIR = "videos"

def handle_client(conn, addr):
    print(f"[+] Client connected: {addr}")

    try:
        videos = os.listdir(VIDEO_DIR)
        conn.sendall(pickle.dumps(videos))

        video_name = conn.recv(1024).decode()
        video_path = os.path.join(VIDEO_DIR, video_name)

        if not os.path.exists(video_path):
            print("[-] Invalid video requested")
            conn.close()
            return

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("[-] Cannot open video")
            conn.close()
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            _, buffer = cv2.imencode('.jpg', frame)
            data = pickle.dumps(buffer)

            message = struct.pack("Q", len(data)) + data
            conn.sendall(message)

        cap.release()

    except Exception as e:
        print(f"[!] Error: {e}")

    finally:
        conn.close()
        print(f"[-] Client disconnected: {addr}")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[SERVER] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()