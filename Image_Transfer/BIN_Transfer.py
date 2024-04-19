import serial
import time


def send_file_over_serial(file_path, com_port, baud_rate=115200):
    # Open the serial port
    try:
        ser = serial.Serial(com_port, baud_rate, timeout=1)
        print(f"Opened serial port {com_port}")
    except serial.SerialException as e:
        print(f"Error opening serial port {com_port}: {e}")
        return

    time.sleep(2)  # Give some time to establish the connection

    # Open the file in binary read mode
    try:
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(32)  # Read in 32-byte chunks
                if not data:
                    break  # Break the loop if no more data is read
                
                ser.write(data)  # Send the 32-byte chunk over serial
                time.sleep(0.1)  # Short delay to prevent overwhelming the receiver

            print(f"Finished sending the file {file_path} over {com_port}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while sending the file: {e}")

    # Close the serial port
    ser.close()
    print(f"Closed serial port {com_port}")

# Set the path to your binary file and COM port
bin_file_path = '100_bytes.bin'  # Replace with your binary file path
com_port = 'COM7'  # Replace with your COM port

# Call the function to send the file over serial
send_file_over_serial(bin_file_path, com_port)
