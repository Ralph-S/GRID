import serial
import time
from PIL import Image
import io

def setup_serial_connection(port, baud_rate=115200):
    """Establishes serial connection with the specified port and baud rate."""
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)  # Allow time for serial connection to establish
        ser.reset_input_buffer()  # Clear the serial input buffer
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
        return None

def send_handshake(ser, handshake_byte=b'1'):
    """Sends a handshake byte to start data transmission."""
    if ser:
        ser.write(handshake_byte)
        print("Handshake sent. Waiting for data...")

def receive_image_data(ser):
    """Receives JPEG image data from the serial port, handling fragmented markers."""
    image_data = bytearray()
    buffer = bytearray()
    start_marker_found = False
    end_marker_found = False

    while not end_marker_found:
        if ser.in_waiting > 0:
            new_data = ser.read(ser.in_waiting)
            buffer += new_data  # Add new data to buffer
            print(f"Data received: {new_data.hex()}")  # Log the raw data received

            if not start_marker_found:
                # Permissive search for the start marker 'FF D8'
                i = 0
                while i < len(buffer) - 1:
                    if buffer[i] == 0xFF:
                        # Check the next bytes until 'D8' is found or buffer ends
                        j = i + 1
                        while j < len(buffer) and buffer[j] == 0x00:  # Skip zeros
                            j += 1
                        if j < len(buffer) and buffer[j] == 0xD8:
                            start_marker_found = True
                            start_index = i
                            print(f"Start marker found at index: {start_index}")
                            image_data += buffer[start_index:]
                            buffer = bytearray()  # Clear buffer after the start marker
                            break
                    i += 1
                if not start_marker_found:
                    print("Start marker not yet found.")
            else:
                image_data += buffer
                buffer = bytearray()  # Clear buffer after appending to image data

                # Search for the end marker 'FF D9'
                end_index = image_data.find(b'\xFF\xD9')
                if end_index != -1:
                    image_data = image_data[:end_index + 2]
                    end_marker_found = True
                    print(f"End marker found at index: {end_index}")
                else:
                    print("End marker not yet found.")

    return image_data
    
def display_image(image_data):
    """Display the image from the received data."""
    try:
        image_stream = io.BytesIO(image_data)
        image = Image.open(image_stream)
        image.show()
        image.save("output.jpg")  # Save the image to a file for inspection
    except Exception as e:
        print(f"Failed to display image: {e}")
        with open("output_bytes.bin", "wb") as file:  # Save the raw data for inspection
            file.write(image_data)
        print("Raw image data saved as 'output_bytes.bin'. Please inspect this file with a hex editor.")

def main():
    port = 'COM8'  # Replace with your actual COM port
    ser = setup_serial_connection(port)
    print("hello")
    if ser:
        send_handshake(ser)
        data = receive_image_data(ser)
        if data:
            print("Displaying image.")
            display_image(data)
        else:
            print("No data to display.")
        ser.close()

if __name__ == "__main__":
    main()










# import serial
# import time
# from PIL import Image
# import io

# def setup_serial_connection(port, baud_rate=115200):
#     """Establishes serial connection with the specified port and baud rate."""
#     try:
#         ser = serial.Serial(port, baud_rate, timeout=1)
#         time.sleep(2)  # Allow time for serial connection to establish
#         ser.reset_input_buffer()  # Clear the serial input buffer
#         return ser
#     except serial.SerialException as e:
#         print(f"Error opening serial port {port}: {e}")
#         return None

# def send_handshake(ser, handshake_byte=b'1'):
#     """Sends a handshake byte to start data transmission."""
#     if ser:
#         ser.write(handshake_byte)
#         print("Handshake sent. Waiting for data...")

# def receive_image_data(ser):
#     """Receives JPEG image data from the serial port, handling fragmented markers."""
#     image_data = bytearray()
#     buffer = bytearray()
#     packet_count = 0
#     total_bytes_received = 0
#     last_data_time = time.time()  # Initialize time for timeout management

#     while True:
#         if ser.in_waiting > 0:
#             new_data = ser.read(ser.in_waiting)
#             buffer += new_data  # Append new data to buffer
#             total_bytes_received += len(new_data)

#             # Detect and handle start marker 'FF D8'
#             if b'\xFF\xD8' in buffer and not image_data:
#                 start_index = buffer.find(b'\xFF\xD8')
#                 image_data = buffer[start_index:]
#                 buffer = bytearray()  # Clear buffer after finding start marker
#                 print("JPEG start marker found.")

#             # Detect end marker 'FF D9'
#             if b'\xFF\xD9' in image_data:
#                 end_index = image_data.find(b'\xFF\xD9') + 2
#                 image_data = image_data[:end_index]
#                 print("JPEG end marker found.")
#                 break

#             # Update packet count and log received data
#             packet_count += 1
#             print(f"Packet {packet_count}: Received {len(new_data)} bytes, Data: {new_data.hex()}")

#             last_data_time = time.time()  # Update last data time
#         elif time.time() - last_data_time > 3:  # Timeout if no new data for 3 seconds
#             print("Timeout reached. No more data received.")
#             break

#     print(f"Total packets received: {packet_count}")
#     print(f"Total bytes received: {total_bytes_received}")
#     return image_data

# def display_image(image_data):
#     """Attempts to create and display an image from the received data."""
#     try:
#         image_stream = io.BytesIO(image_data)
#         image = Image.open(image_stream)
#         image.show()
#         image.save("output.jpg")  # Save the image to a file for inspection
#     except Exception as e:
#         print(f"Failed to display image: {e}")

# def main():
#     port = 'COM8'  # Replace with your actual COM port
#     ser = setup_serial_connection(port)
#     if ser:
#         send_handshake(ser)
#         data = receive_image_data(ser)
#         if data:
#             print("Displaying image.")
#             display_image(data)
#         else:
#             print("No data to display.")
#         ser.close()

# if __name__ == "__main__":
#     main()












# import serial
# import time
# from PIL import Image
# import io

# def setup_serial_connection(port, baud_rate=115200):
#     """Establishes serial connection with the specified port and baud rate."""
#     try:
#         ser = serial.Serial(port, baud_rate, timeout=1)
#         time.sleep(2)  # Allow time for serial connection to establish
#         ser.reset_input_buffer()  # Clear the serial input buffer
#         return ser
#     except serial.SerialException as e:
#         print(f"Error opening serial port {port}: {e}")
#         return None

# def send_handshake(ser, handshake_byte=b'1'):
#     """Sends a handshake byte to start data transmission."""
#     if ser:
#         ser.write(handshake_byte)
#         print("Handshake sent. Waiting for data...")

# def receive_image_data(ser):
#     """Receives JPEG image data from the serial port, handling fragmented markers."""
#     image_data = bytearray()
#     buffer = bytearray()
#     start_marker_found = False
#     end_marker_found = False

#     while not end_marker_found:
#         if ser.in_waiting > 0:
#             new_data = ser.read(ser.in_waiting)
#             buffer += new_data  # Add new data to buffer
#             print(f"Data received: {new_data.hex()}")  # Log the raw data received

#             if not start_marker_found:
#                 # Permissive search for the start marker 'FF D8'
#                 i = 0
#                 while i < len(buffer) - 1:
#                     if buffer[i] == 0xFF:
#                         # Check the next bytes until 'D8' is found or buffer ends
#                         j = i + 1
#                         while j < len(buffer) and buffer[j] == 0x00:  # Skip zeros
#                             j += 1
#                         if j < len(buffer) and buffer[j] == 0xD8:
#                             start_marker_found = True
#                             start_index = i
#                             print(f"Start marker found at index: {start_index}")
#                             image_data += buffer[start_index:]
#                             buffer = bytearray()  # Clear buffer after the start marker
#                             break
#                     i += 1
#                 if not start_marker_found:
#                     print("Start marker not yet found.")
#             else:
#                 image_data += buffer
#                 buffer = bytearray()  # Clear buffer after appending to image data

#                 # Search for the end marker 'FF D9'
#                 end_index = image_data.find(b'\xFF\xD9')
#                 if end_index != -1:
#                     image_data = image_data[:end_index + 2]
#                     end_marker_found = True
#                     print(f"End marker found at index: {end_index}")
#                 else:
#                     print("End marker not yet found.")

#     return image_data



# def display_image(image_data):
#     """Attempts to create an image from data and display it, also saves to file for inspection."""
#     try:
#         # Locate the exact positions of the start and end markers within the data
#         start = image_data.find(b'\xFF\xD8')
#         end = image_data.find(b'\xFF\xD9', start) + 2  # Include the end marker length

#         if start == -1 or end == -1 or start >= end:
#             print("Correct JPEG markers not found in the data, or are incorrectly placed.")
#         else:
#             print(f"JPEG markers found. Start at: {start}, End at: {end}")
#             # Extract the clean JPEG data
#             clean_image_data = image_data[start:end]

#             # Save this data to a file to verify it manually if needed
#             file_path = "C:/Users/Charbel/Documents/Arduino/Radio_Module/Image_Transfer/verified_output.jpg"
#             with open(file_path, "wb") as file:
#                 file.write(clean_image_data)
#                 print(f"Verified image data saved for inspection at: {file_path}")

#             # Optionally, try to display the image
#             image_stream = io.BytesIO(clean_image_data)
#             image = Image.open(image_stream)
#             image.show()
#     except Exception as e:
#         print(f"Failed to display image: {e}")


# def main():
#     port = 'COM8'  # Replace with your actual COM port
#     ser = setup_serial_connection(port)
#     if ser:
#         send_handshake(ser)
#         data = receive_image_data(ser)
#         if data:
#             print("Displaying image.")
#             display_image(data)
#         else:
#             print("No data to display.")
#         ser.close()

# if __name__ == "__main__":
#     main()













