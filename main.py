from PIL import Image
from pandas import read_csv

# load dataset
dataframe = read_csv("Brightness.csv", delimiter=',', header=None, dtype=str)
# dataset = dataframe.values
dataset = dataframe.values
# define input sequence
raw_seq = dataset[:, 1]


# Calculate the image brightness as a scale of its RGB Histogram
def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale


if __name__ == '__main__':
    for i in range(0, 190):
        Optic_flow_image = Image.open(str(raw_seq[i]))
        b_value = calculate_brightness(Optic_flow_image)
        print("%s\t" % b_value)
