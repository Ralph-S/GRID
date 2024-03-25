import torch
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt

class AerialImageSegmenter:
    def __init__(self, use_cuda=False):
        self.model = models.segmentation.deeplabv3_resnet101(pretrained=True)
        self.model.eval()
        self.use_cuda = use_cuda and torch.cuda.is_available()
        
        if self.use_cuda:
            self.model.cuda()
        
        self.transform = transforms.Compose([
            transforms.ToTensor(), 
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
    
    def segment_image(self, image_path):
        """
        Perform semantic segmentation on an image.
        
        Parameters:
        - image_path: Path to the image file.
        
        Returns:
        - output_predictions: The segmented output as a 2D tensor.
        """
        input_image = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(input_image)
        input_batch = input_tensor.unsqueeze(0)
        
        if self.use_cuda:
            input_batch = input_batch.cuda()
        
        with torch.no_grad():
            output = self.model(input_batch)['out'][0]
        output_predictions = output.argmax(0)
        
        return output_predictions
    
    def display_segmentation(self, image_path):
        """
        Display the original and segmented image side by side.
        
        Parameters:
        - image_path: Path to the image file.
        """
        output_predictions = self.segment_image(image_path)
        
        # Load the original image for display
        original_image = Image.open(image_path).convert("RGB")
        
        # Display the original and segmented images
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.imshow(original_image)
        plt.title('Original Image')
        plt.subplot(1, 2, 2)
        plt.imshow(output_predictions.cpu().numpy())
        plt.title('Segmented Image')
        plt.show()

# Example usage:
segmenter = AerialImageSegmenter(use_cuda=True)
segmenter.display_segmentation('/home/wgt/Desktop/GRID/GRID/img_processing/images/img1.jpg')