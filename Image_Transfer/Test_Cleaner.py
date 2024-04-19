def process_hex_data(hex_data):
    result = bytearray()
    i = 0
    length = len(hex_data)
    print(f"LENGTH OF OUTPUT BYTES: {length}")
    while i < length:
        # First valid 2 hex chars (1 byte)
        if i + 1 <= length:
            result += hex_data[i:i+1]
            i += 1
        else:
            result += hex_data[i:length]
            break

        # Skip 62 hex zeros (31 bytes)
        if i + 31 <= length:
            i += 31
        else:
            break

        # Second valid 30 hex chars (15 bytes)
        if i + 15 <= length:
            result += hex_data[i:i+15]
            i += 15
        else:
            result += hex_data[i:length]
            break

        # if i == 5903:
        #     if i + 16 <= length:
        #         result += hex_data[i:i+16]
        #         i += 16
            # else:
            #     break
            # if i + 1 <= length:
            #     i += 1
            # else:
            #     break
            # continue
        # Skip 34 hex zeros (17 bytes)
        if i + 17 <= length:
            i += 17
        else:
            break

        # Third valid 32 hex chars (16 bytes)
        if i + 16 <= length:
            result += hex_data[i:i+16]
            i += 16
        else:
            result += hex_data[i:length]
            break

        # Skip 30 hex zeros (16 bytes) at the end of the sequence before it repeats
        if i + 16 <= length:
            i += 16
        else:
            break
        

    return result

def read_and_process_file(input_filename, output_filename):
    with open(input_filename, 'rb') as file:
        hex_data = file.read()

    with open('Image_byte_data.bin', 'rb') as file:
        hex_data_original = file.read()

    print(f"LENGTH OF ORIGINAL FILE: {len(hex_data_original)}")
    

    processed_data = process_hex_data(hex_data)

    with open(output_filename, 'wb') as file:
        file.write(processed_data)

# Example usage:
input_filename = 'output_bytes.bin'  # Use the uploaded file path
output_filename = 'cleaned.bin'  # Output file path for cleaned data
read_and_process_file(input_filename, output_filename)

with open('cleaned.bin', 'rb') as file:
    clean_data = file.read()

print(f"LENGTH OF CLEAN FILE: {len(clean_data)}")