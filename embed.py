import obtain_pixel
import convert

pixels = obtain_pixel.pixels
bin_list = convert.bin_list
sel_pixels=obtain_pixel.sel_pixels
bin_RGB=[]
for i in range(0,len(sel_pixels)):
    ht=sel_pixels[i]["ht"]
    wt=sel_pixels[i]["wt"]
    RGB=pixels[wt,ht]
    RGB_BIN=[]    
    for values in RGB:
        temp=bin(values)
        RGB_BIN.append(int(temp[2::]))
    bin_RGB.append(RGB_BIN)
    
print(bin_RGB)    