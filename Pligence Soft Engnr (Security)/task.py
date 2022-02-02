
def process_byte(b):
    # binary = bin(b)
    byte = b
    # print(integer)
    # integer = int(str(binary),2)
    # if ((binary > bin(int('20',16)).zfill(8)) and (binary < bin(int('7F',16)).zfill(8))):
    # final = ''
    if ((byte > int('0x20',16)) and (byte < int('0x7f',16))):
        final = chr(byte)
        # integer = int(binary,2)
        # integer = binary
        # print(integer)
        return final
    # return final

# def main():
str_data = ''
with open("term-size.exe", "rb") as f:
    bytes_read = f.read()
for b in bytes_read:
    char = process_byte(b)
    if(char != None):
        str_data = str_data + str(char)
        print (str_data)

    

# if __name__ == "__main__":
#     main()
