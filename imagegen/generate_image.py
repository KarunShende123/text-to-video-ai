import sys
from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt):
    pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
    pipe.to("cuda")
    image = pipe(prompt).images[0]
    image.save("output/image.png")

if __name__ == "__main__":
    generate_image(sys.argv[1])
