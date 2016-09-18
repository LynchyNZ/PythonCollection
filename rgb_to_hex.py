def rgb_to_hex(red, green, blue):
    hex_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    hex_str = ""    
    for colour in [red,green,blue]:
        if colour > 255:
            hex_str += "Number out of range"
            break
        else:
            hex_str += hex_list[colour//16]
            hex_str += hex_list[colour%16]
    return hex_str



print(rgb_to_hex(254,255,255))