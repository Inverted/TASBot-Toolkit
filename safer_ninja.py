import argparse
import json
import socket
import hashlib

TIMEOUT_DELAY = 1.0

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', "--immediately", help="play animation immediately (NOT WORKING YET)", default=False,
                    action="store_true")
parser.add_argument('-p', '--port', help="TCP port that should be used", default=8082)
parser.add_argument('animation', help="the animation gif that is to inject")
parser.add_argument('ip', help="IP address of the receiver")
args = parser.parse_args()

print(f"[INFO] Sending {args.animation} to {args.ip}:{args.port}, playing it immediately: {str(args.immediately)}")

# Determine animation mode
ani_mode = 'now' if args.immediately else 'queued'

# Create payload dictionary
payload = {
    "mode": ani_mode,
    "data": None
}

# Open and read file
with open(args.animation, 'rb') as file:
    data = file.read()

    # Read bytes into list
    byte_list = []
    for byte in data:
        byte_list.append(byte)
    payload["data"] = byte_list

# Send to receiver
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(TIMEOUT_DELAY)
    s.connect((args.ip, args.port))
    s.sendall(json.dumps(payload).encode('utf-8'))
