# Python script to create a binary file of 100 bytes

# Define the file path for the new file
bin_file_path = '100_bytes.bin'

# Create 100 bytes of data (this will just be 0 to 99 for simplicity)
data = bytes(range(100))

# Write the data to the binary file
with open(bin_file_path, 'wb') as bin_file:
    bin_file.write(data)

print(f"Created a binary file with 100 bytes at: {bin_file_path}")
