import sys
from PIL import Image

def animate(prompt):
    # Placeholder for AnimateDiff code
    print(f"Animating: {prompt}")
    image = Image.open("output/image.png")
    image.save("output/video.mp4")  # Placeholder only

if __name__ == "__main__":
    animate(sys.argv[1])
