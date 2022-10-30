import argparse
import socket

# networking
IP = "127.0.0.1"
PORT_OUT = 8080
PORT_IN = 8081

# payload
MAX_PATH_LENGTH = 4096
MAX_MESSAGE_LENGTH = 64
MAX_DATAGRAM_SIZE = (MAX_PATH_LENGTH + MAX_MESSAGE_LENGTH)

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-I', "--immediately", help="play animation immediately", default=False, action="store_true")
parser.add_argument('animation')
args = parser.parse_args()

# Determine animation mode
ani_mode = 'I' if args.immediately else 'Q'
print(f"[INFO] Requesting to play {args.animation}; Immediately: {str(args.immediately)}")

# Connect to TASBot via UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT_IN))

# Construct and send payload
payload = f"{ani_mode};{args.animation}"
sock.sendto(payload.encode('utf-8'), (IP, PORT_OUT))

# Wait for answer and print out
data, addr = sock.recvfrom(MAX_DATAGRAM_SIZE)
print(f"[TASBot]: {data.decode('utf-8')}")

# Close socket
sock.close()
