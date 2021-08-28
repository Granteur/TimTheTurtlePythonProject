import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color = (red, green, blue)
    rgb_colors.append(new_color)

print(rgb_colors)
