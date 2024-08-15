from PIL import Image

img = Image.open(r'.\images\astro.jpg')
print(img.size)

# new_img = img.resize((200,200))
# aspect ration maintain problem solve using thumbnail
img.thumbnail((200,200))
img.save('profile.jpg')
# print(new_img.size)