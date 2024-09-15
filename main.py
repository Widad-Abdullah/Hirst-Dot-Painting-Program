import colorgram

colors = colorgram.extract("Replace_this_with_image_address.jpg", 30) #Change this number to specify number of colors to extract
rgb_lst=[]
for i in colors:
    r = i.rgb.r #h
    g = i.rgb.g #s
    b = i.rgb.b #l
    new_tuple=(r,g,b)
    rgb_lst.append(new_tuple)

print(rgb_lst)

