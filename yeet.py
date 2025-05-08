# 9x9 number recognition NN by DoctorEnilno
import os
from PIL import Image
import random

os.system("cls")

def image_to_pixel_list(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    pixels = list(img.getdata())
    pixel_list = [0 if pixel < 128 else 1 for pixel in pixels]
    return pixel_list

def neuron(inputs, weights, bias):
    out_n = []
    for i in range(len(inputs)-1):
        out_n.append(inputs[i]*weights[i])
    num_n = 0
    for i in out_n:
        num_n += i
    num_n += bias
    return num_n
    
def find_max(numbers):
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    
    return max_num
#--------------------------------------------------

pixels = image_to_pixel_list("images/"+random.choice(os.listdir("images")))

num = 0
newliste = []
print("\n")
for i in pixels:
    newliste.append(str(i))
    num += 1
    if num == 9:
        print("".join(newliste).replace("0", ' '))
        num = 0
        newliste = []
        
print("\n")
#--------------------------------------------------

bias_n1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bias_n2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bias_n3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

bias_o1  = [0, 0, 0]
bias_o2  = [0, 0, 0]
bias_o3  = [0, 0, 0]
bias_o4  = [0, 0, 0]
bias_o5  = [0, 0, 0]
bias_o6  = [0, 0, 0]
bias_o7  = [0, 0, 0]
bias_o8  = [0, 0, 0]
bias_o9  = [0, 0, 0]
bias_o10 = [0, 0, 0]


weight_n1 = 0
weight_n2 = 0
weight_n3 = 0

num_n1 = neuron(pixels, bias_n1, weight_n1)
num_n2 = neuron(pixels, bias_n2, weight_n2)
num_n3 = neuron(pixels, bias_n3, weight_n3)

out_hl = [num_n1, num_n2, num_n3]

#--------------------------------------------------

num_o1 = neuron(out_hl, bias_o1, 0)
num_o2 = neuron(out_hl, bias_o2, 0)
num_o3 = neuron(out_hl, bias_o3, 0)
num_o4 = neuron(out_hl, bias_o4, 0)
num_o5 = neuron(out_hl, bias_o5, 0)
num_o6 = neuron(out_hl, bias_o6, 0)
num_o7 = neuron(out_hl, bias_o7, 0)
num_o8 = neuron(out_hl, bias_o8, 0)
num_o9 = neuron(out_hl, bias_o9, 0)
num_o10 = neuron(out_hl, bias_o10, 0)

out_out = [num_o1, num_o2, num_o3, num_o4, num_o6, num_o7, num_o8, num_o9, num_o10]

#-----------------------------------------

for i in range(9):
    if out_out[i] == find_max(out_out):
        print(f" [*] {i}: {out_out[i]}")
    else:
        print(f" [ ] {i}: {out_out[i]}")