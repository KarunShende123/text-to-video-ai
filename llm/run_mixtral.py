import sys

def run_mixtral(prompt):
    scene = {
        "scene": "futuristic lab",
        "character": "Tony Stark in Dr. Doom suit",
        "action": "walking through fire"
    }
    with open("output/scene.json", "w") as f:
        f.write(str(scene))

if __name__ == "__main__":
    run_mixtral(sys.argv[1])
