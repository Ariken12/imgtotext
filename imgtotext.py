from PIL import Image, ImageDraw

#input().replace("\\", "\\\\")

img = Image.open('test3.png')

width = img.size[0]
height = img.size[1]
pix = img.load()
string = ""




def forbw(pix, height, width):
    f = open("txt3.txt", "w")
    r1 = 1
    r2 = 1
    chr1 = "0"
    chr2 = "#"
    line = ""
    for j in range(0, height, r1):
        for i in range(0, width, r2):
            if (pix[i, j][0] + pix[i, j][1] + pix[i, j][2]) > 384:
                pix[i, j] = (255, 255, 255)
                line += chr1
            else:
                pix[i, j] = (0, 0, 0)
                line += chr2
            print(1, end='')
        f.write(line + "\r")
        print()
        line = ""
    f.close()


def forclr(pix, h, w):
    line = ""
    for i in range(0, h, 1):
        for j in range(0, w, 1):
            if (pix[j, i][0] >= pix[j, i][1] and pix[j, i][0] > pix[j, i][2]) or (
                    pix[j, i][0] > pix[j, i][1] and pix[j, i][0] >= pix[j, i][2]):
                line += "1"
                pix[j, i] = (255, 0, 0)
            elif (pix[j, i][1] >= pix[j, i][0] and pix[j, i][1] > pix[j, i][2]) or (
                    pix[j, i][1] > pix[j, i][0] and pix[j, i][1] >= pix[j, i][2]):
                line += "2"
                pix[j, i] = (0, 255, 0)
            elif (pix[j, i][2] >= pix[j, i][1] and pix[j, i][2] > pix[j, i][0]) or (
                    pix[j, i][2] > pix[j, i][1] and pix[j, i][2] >= pix[j, i][0]):
                line += "3"
                pix[j, i] = (0, 0, 255)
            elif pix[j, i][0] == pix[j, i][1] and pix[j, i][0] == pix[j, i][2] and pix[j, i][0] > 128:
                line += "8"
                pix[j, i] = (255, 255, 255)
            elif pix[j, i][0] == pix[j, i][1] and pix[j, i][2] == pix[j, i][0] and pix[j, i][0] <= 128:
                line += "0"
                pix[j, i] = (0, 0, 0)
        f.write(line + "\r\n")
        line = ""


forbw(pix, height, width)

img.show()
