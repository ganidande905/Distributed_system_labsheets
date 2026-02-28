import socket
import cv2
import pickle
import struct

SERVER_IP = '127.0.0.1'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

data = b""
payload_size = struct.calcsize("Q")

videos = pickle.loads(client.recv(4096))
print("Available videos:")
for v in videos:
    print(" -", v)

choice = input("Enter video name: ")
client.send(choice.encode())

try:
    while True:
        while len(data) < payload_size:
            packet = client.recv(4096)
            if not packet:
                raise ConnectionError
            data += packet

        packed_size = data[:payload_size]
        data = data[payload_size:]
        frame_size = struct.unpack("Q", packed_size)[0]

        while len(data) < frame_size:
            data += client.recv(4096)

        frame_data = data[:frame_size]
        data = data[frame_size:]

        frame = pickle.loads(frame_data)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        cv2.imshow("Video Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception:
    pass

finally:
    client.close()
    cv2.destroyAllWindows()