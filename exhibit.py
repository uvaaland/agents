import glob
import json


def get_title():
    with open("gallery/title", 'r') as tfile:
        title = tfile.read().rstrip()

    return title


def get_images():
    return glob.glob("gallery/*.png")


def create_slides():

    title = get_title()
    images = get_images()

    delimiter = "\n\n---\n"

    with open("slides.md", 'w') as slides:
        slides.write(f"# {title}{delimiter}")

        for image in images:
            slides.write(f"![]({image}){delimiter}")


def create_reveal_config_file():

    config = {
                'controls': False,
                'progress': False,
                'transition': 'fade'
             }

    config = json.dumps(config)

    with open("reveal.json", 'w') as cfile:
        cfile.write(config)


if __name__ == "__main__":
    create_slides()
    create_reveal_config_file()
