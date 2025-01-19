# Define the specific palette mentioned in the request
from matplotlib import pyplot as plt

specific_palette = {

    "Aqua Blue": (37/255, 163/255, 179/255),

    "Deep Ocean Blue": (18/255, 108/255, 132/255),

    "Light Teal": (150/255, 212/255, 220/255),

    "Cerulean Blue": (38/255, 123/255, 191/255),

    "Bright Azure Blue": (63/255, 169/255, 245/255),

    "Ice Blue": (200/255, 230/255, 255/255),

    "Navy Blue": (8/255, 58/255, 81/255),

}



# Create a figure to display the requested palette

fig, ax = plt.subplots(figsize=(12, 2))



# Display each color as a rectangle

for i, (name, rgb) in enumerate(specific_palette.items()):

    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=rgb))

    ax.text(i + 0.5, -0.2, name, ha='center', va='center', fontsize=10)



# Configure the plot

ax.set_xlim(0, len(specific_palette))

ax.set_ylim(0, 1)

ax.axis('off')



plt.show()