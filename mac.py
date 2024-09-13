import uuid
import pixel 
from PIL import Image
def getpixels():
    img=Image.open(r"C:/Users/rahul/test.png");
    pixels = img.load()  # Access pixel data
    height=img.size[0];
    width=img.size[1];
    total_pixels=height*width;
    return height,width
    

total_pixels = pixel.total_pixels
def get_mac_address():
    # Get the MAC address as an integer
    mac = uuid.getnode()
    return mac

mac = get_mac_address()
#total_pixels = getpixels()
height,width=getpixels()
print("MAC Address:", get_mac_address())
print("Total pixels: ",getpixels())

key_position_height = mac%height
key_position_width = mac%width
print("key position: ",key_position_height,key_position_width)
