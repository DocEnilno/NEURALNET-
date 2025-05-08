import os
import math
from PIL import Image
import random
import json

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

def get_color_for_percentage(percent):
    if percent > 75:
        return bcolors.OKGREEN
    elif percent > 50:
        return bcolors.WARNING
    else:
        return bcolors.FAIL

def image_to_pixel_list(image_path):
    img = Image.open(image_path)
    img = img.convert('L')
    pixels = list(img.getdata())
    pixel_list = [0 if pixel < 20 else 0.5 if pixel < 253 else 1 for pixel in pixels]
    return pixel_list

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def neuron(inputs, weights, bias):
    z = sum(i * w for i, w in zip(inputs, weights)) + bias
    return sigmoid(z)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

# Initialize weights and biases
bias_n1, bias_n2, bias_n3 = random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)

file_path = 'data.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        biases = json.load(f)
else:
    biases = {
        'o1': random.uniform(-1, 1),
        'o2': random.uniform(-1, 1),
        'o3': random.uniform(-1, 1),
        'o4': random.uniform(-1, 1),
        'o5': random.uniform(-1, 1),
        'o6': random.uniform(-1, 1),
        'o7': random.uniform(-1, 1),
        'o8': random.uniform(-1, 1),
        'o9': random.uniform(-1, 1),
        'o10': random.uniform(-1, 1),
        'lr': 0.01,
        'w1': [random.uniform(-1, 1) for _ in range(3)],
        'w2': [random.uniform(-1, 1) for _ in range(3)],
        'w3': [random.uniform(-1, 1) for _ in range(3)],
        'w4': [random.uniform(-1, 1) for _ in range(3)],
        'w5': [random.uniform(-1, 1) for _ in range(3)],
        'w6': [random.uniform(-1, 1) for _ in range(3)],
        'w7': [random.uniform(-1, 1) for _ in range(3)],
        'w8': [random.uniform(-1, 1) for _ in range(3)],
        'w9': [random.uniform(-1, 1) for _ in range(3)],
        'w10': [random.uniform(-1, 1) for _ in range(3)],
        "weights_n1": [random.uniform(-1, 1) for _ in range(81)],
        "weights_n2": [random.uniform(-1, 1) for _ in range(81)],
        "weights_n3": [random.uniform(-1, 1) for _ in range(81)]
    }

right = 0
wrong = 0
iterations = 0

while True:
    os.system("cls" if os.name == 'nt' else "clear")
    file = random.choice(os.listdir("images"))
    pixels = image_to_pixel_list("images/" + file)

    print(f"Processing file: {file}")
    print(f"Pixels: {pixels}")

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

    print(f"Neuron 1 output: {num_n1}")
    print(f"Neuron 2 output: {num_n2}")
    print(f"Neuron 3 output: {num_n3}")

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

    print(f"Output layer values: {out_out}")

    predicted = out_out.index(find_max(out_out))
    print(f"Predicted number: {predicted}")
    print(f"Actual number: {number}")

    if predicted == number:
        right += 1
        for j in range(3):
            biases[f'w{number+1}'][j] += biases['lr'] * out_hl[j]
        biases[f'o{number+1}'] += biases['lr']
    else:
        for j in range(3):
            biases[f'w{predicted+1}'][j] -= biases['lr'] * out_hl[j]
            biases[f'w{number+1}'][j] += biases['lr'] * out_hl[j]
        biases[f'o{predicted+1}'] -= biases['lr']
        biases[f'o{number+1}'] += biases['lr']
        wrong += 1

    iterations += 1
    percent = (right / iterations) * 100
    color = get_color_for_percentage(percent)

    print(f"Right: {right}, Wrong: {wrong}, Percent: {color}{round(percent, 2)}%{bcolors.ENDC}")
    print(f"Biases: {json.dumps(biases, indent=4)}")

    with open(file_path, 'w') as f:
        json.dump(biases, f, indent=4)
