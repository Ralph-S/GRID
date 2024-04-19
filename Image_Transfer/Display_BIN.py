from PIL import Image
import io

# Replace this with the path to your .bin file
bin_file_path = 'cleaned.bin'

# Function to read the binary data and interpret it as an image
def display_image_from_bin(bin_path):
    # Read the binary content of the file
    with open(bin_path, 'rb') as file:
        image_data = file.read()

    # Attempt to display the image using PIL
    try:
        # Create a bytes stream from the binary data
        image_stream = io.BytesIO(image_data)
        
        # Open the image stream using PIL and display the image
        image = Image.open(image_stream)
        image.show()
        
        # Optionally, save the image to disk for further inspection
        image.save('output_image.jpg', 'JPEG')
        print("Image displayed and saved successfully.")
    except Exception as e:
        print(f"Failed to display image: {e}")

# Call the function and display the image
display_image_from_bin(bin_file_path)
