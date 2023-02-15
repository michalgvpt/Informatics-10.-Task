from PIL import Image
img=Image.open('steneography/dolphins.png')
pixels=img.load()
message='Hello Dudo#'


def preparation(message:str):
    result=[]
    for letter in message:
        number=bin(ord(letter))[2::]
        while len(number)<8:
            number='0'+number
        for j in number:
            result.append(int(j))
    return result
preparation(message)

def encoder(message:str):
    mesinbin=preparation(message)
    for i in range(len(mesinbin)):
        width=img.size[0]
        x=i%width 
        y=i//width 
        bluepixel=pixels[x,y][2]
        newbluepixel=int(bin(bluepixel)[2:-1:] + str(mesinbin[i]),2) 
        newcolour=(pixels[x,y][0],pixels[x,y][1],newbluepixel)
        pixels[x,y]=newcolour
encoder(message)

def decoder(img):
    binary=''
    string=''
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if '#' in binary:
                return binary
            renblue=str(bin(pixels[x,y][2]))[-1]
            string+=renblue
            hash=(bin(ord('#'))[2::])
            space=(bin(ord(' '))[2::])
            if len(string)== 8 or string[2::]==hash or string[2::]==space:
                binary+=chr(int((string),2))
                string=''
print(decoder(img))
