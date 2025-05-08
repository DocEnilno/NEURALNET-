import os
import math
from PIL import Image
import random
import time
import json

os.system("cls")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def image_to_pixel_list(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    pixels = list(img.getdata())
    pixel_list = [0 if pixel < 20 else 0.5 if pixel < 253 else 1 for pixel in pixels]
    return pixel_list

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neuron(inputs, weights, bias):
    return sigmoid(sum(i * w for i, w in zip(inputs, weights)) + bias)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

# Initialize weights and biases



bias_n1, bias_n2, bias_n3 = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)

file_path = 'data.json'


with open(file_path, 'r') as f:
    biases= json.load(f)





right = 0
wrong = 0
iterations = 0


os.system("cls")
file = random.choice(os.listdir("images"))
pixels = image_to_pixel_list("images/" + file)

num = 0
newliste = []
print("\n")
for i in pixels:
    newliste.append(str(i))
    num += 1
    if num == 9:
        print(bcolors.BOLD + bcolors.OKCYAN + "".join(newliste).replace("0", '_').replace(".5", '.').replace("1", '#') + bcolors.ENDC)
        num = 0
        newliste = []
        
print("\n")

number = int(file.split("_")[0])

num_n1 = neuron(pixels, biases["weights_n1"], bias_n1)
num_n2 = neuron(pixels, biases["weights_n2"], bias_n2)
num_n3 = neuron(pixels, biases["weights_n3"], bias_n3)

out_hl = [num_n1, num_n2, num_n3]

out_out = [
    neuron(out_hl, biases['w1'], biases['o1']),
    neuron(out_hl, biases['w2'], biases['o2']),
    neuron(out_hl, biases['w3'], biases['o3']),
    neuron(out_hl, biases['w4'], biases['o4']),
    neuron(out_hl, biases['w5'], biases['o5']),
    neuron(out_hl, biases['w6'], biases['o6']),
    neuron(out_hl, biases['w7'], biases['o7']),
    neuron(out_hl, biases['w8'], biases['o8']),
    neuron(out_hl, biases['w9'], biases['o9']),
    neuron(out_hl, biases['w10'], biases['o10'])
]

predicted = out_out.index(find_max(out_out))

print(f"Guess={predicted} , Percent=%")


