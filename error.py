import sys
import socket
import argparse

def main():
    # Setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="filename", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.filename

    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    # Second try-except block -- connect to the given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Connection error: %s" % e)
        sys.exit(1)

    # Third try-except block -- sending data 
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)

    while True:
        # Fourth try-except block -- waiting to receive data from the remote host 
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: %s" % e)
            sys.exit(1)
        if not buf:
            break
        # Write the received data 
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == '__main__':
    main()
