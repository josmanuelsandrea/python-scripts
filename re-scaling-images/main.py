from PIL import Image

image_name = 'source' # You can change the name of the source image here
output_name = 'source' # You can change the output name of the new images here

image_format = 'png' # Image format
image = Image.open(f'{image_name}.{image_format}') # Open the image using open method

sizes = [8, 6, 4, 2, 1.5, 1] 
# These are the divisor numbers for the original resolution of the image. 
# If we have 8 and the image resolution is 500x500. This will divide 500/8
# and 63x63 is going to be the new resolution. The number will be rounded in case it's a float number.
# If you have 1 in the array, you're going to duplicate the original image

# If number is 4 and original res is 468x754. The output res is going to be 117x189

for size in sizes:
    new_size = [int(image.width / size), int(image.height / size)]

    # Resize the image using the Image.resize() method
    resized_image = image.resize(new_size)

    # Save the resized image with a new filename using the image.save() method
    if size == 1:
        output_name = output_name + '_original'
    resized_image.save(f'{output_name}_{new_size[0]}x{new_size[1]}.{image_format}')
    print(f'Generated image with {new_size[0]}x{new_size[1]} size')