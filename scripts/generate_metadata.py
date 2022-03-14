
import os
import yaml
import ffmpy

### UTILITY ###
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def read_yaml(path):
    with open(path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def convert_to_gif(name, input, output):
    ffmpy.FFmpeg(
        inputs={os.path.join(input, f'{name}.mp4'): None},
        outputs={os.path.join(output, f'{name}.gif'): None}
    ).run()

### CONFIG
BASE_PATH = os.path.dirname(os.getcwd())
OUT_PATH  = os.path.join(BASE_PATH, "assets")
RDR_PATH = os.path.join(BASE_PATH, 'BlenderFiles', 'Render')

ROYALTY = 500
CREATORS = [
    {"address": "6j4nNrozTJkk1zatiXHezSLZArnRUq3WkGKHACThXGpZ", "share": 75} #weiwei
    ,{"address": "6j4nNrozTJkk1zatiXHezSLZArnRUq3WkGKHACThXGpZ", "share": 25} #mine
]
COLLECTION = {"name": "Generation n0m", "family": "BurgerDAO"}


### TEMPLATE
template = {
    "name": "Burger",
    "symbol": "BD",
    "description": "", ###
    "seller_fee_basis_points": ROYALTY,
    "image": "", ###
    "attributes": [], ####[{"trait_type": "Layer-1", "value": "0"}],
    "properties": {
        "creators": CREATORS,
        "files": [] #[{"uri": "8.png", "type": "image/png"}]
    },
    "collection": COLLECTION
}

# create jsons
def main():
    files = os.listdir(RDR_PATH)
    files = [f.split('.')[0] for f in files if '.mp4' in f]

    #convert to gif
    for name in files: convert_to_gif(name, RDR_PATH, OUT_PATH)

    # create jsons


# OG = read_yaml(os.path.join(CUR_FDR, "metadata.yaml"))



if __name__ == "__main__":
    main()