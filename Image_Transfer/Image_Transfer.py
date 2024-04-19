import serial
import time
from PIL import Image

# Setup the serial connection
ser = serial.Serial('COM7', 115200, timeout=1)
time.sleep(2)  # Allow some time for the serial connection to establish

def send_image(file_path):
    with open(file_path, 'rb') as img:
        data = img.read()
        total_packets = 0
        total_bytes_sent = 0

        # Send data in 32-byte chunks
        for i in range(0, len(data), 32):
            packet = data[i:i+32]
            ser.write(packet)
            packet_size = len(packet)
            total_bytes_sent += packet_size
            total_packets += 1

            # Print the number of bytes sent in this packet
            print(f"Packet {total_packets}: Sent {packet_size} bytes")

            time.sleep(0.1)  # Give Arduino time to process and send

        print(f"Total packets sent: {total_packets}")
        print(f"Total bytes sent: {total_bytes_sent}")



def save_image_data_to_file(file_path, output_file_path):
    with open(file_path, 'rb') as img:
        data = img.read()
        with open(output_file_path, 'wb') as out:
            out.write(data)
            print(f"Data written to {output_file_path} for inspection.")

# Call the function to save the byte data
save_image_data_to_file('Image2.jpg', 'Image_byte_data.bin')
send_image('Image2.jpg')

