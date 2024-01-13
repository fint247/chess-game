


from PIL import Image, ImageDraw

# Open your image
image1 = Image.open("white_knight.png")
image1 = image1.resize((1000,1000))
# Create a new image with a transparent background
width, height = image1.size  # Adjust as needed
image2 = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Create a drawing object
draw = ImageDraw.Draw(image2)

# Define circle parameters
circle_center = (width // 2, height // 2)
circle_radius = image1.size[0] // 5

# Draw a circle with X % transparency
circle_color = (100, 0, 255, int(255 * 0.5))  # RGBA format (red, green, blue, alpha)
draw.ellipse(
    [
        circle_center[0] - circle_radius,
        circle_center[1] - circle_radius,
        circle_center[0] + circle_radius,
        circle_center[1] + circle_radius,
    ],
    fill=circle_color,
)


final2 = Image.new("RGBA", image1.size)
final2 = Image.alpha_composite(final2, image1)
final2 = Image.alpha_composite(final2, image2)

# Save or display the result
final2.show()
