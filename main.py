import os
import requests

# example url: https://images.bitmoji.com/3d/render/10226473-102178433100_27-s5-v1.webp?scale=0&trim=circle

image_address = input("Give url of BitMoji: ")
folder_name = input("Enter folder name where to save bitmojis: ")

os.mkdir(folder_name)
image_n = int(image_address.split("_")[1].split("-")[0])

for i in range(image_n, -1, -1):
    image_address_pt1 = image_address.split("_")[0]
    image_address_pt2 = "-".join(image_address.split("_")[1].split("-")[1:])
    recontructed_image_address = f"{image_address_pt1}_{i}-{image_address_pt2}"
    print(f"{i} to go of {image_n}")
    res = requests.get(recontructed_image_address.split("?")[0])
    fh = open(f"{folder_name}/image_{i}.webp", "wb")
    fh.write(res.content)
    fh.close()

print("Done")
