 from tqdm import tqdm
import cv2
import numpy as np
import geojson
from util.tiles import tiles_from_slippy_map
from util.features.building import Building_features
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("tile_dir", type=str, help="img dir containing predicted tiles")
parser.add_argument("out", type=str, help="path to GeoJSON to save merged features to")
parser.add_argument("--input_folder_name", type=str, default='input', help="input folder name in the same root folder as predicted tile")


def convert_binary(img_path):
    '''converts RGB imgs to binary images of (0,255) only

    '''
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
    return img

def mask_to_feature(mask_dir):

    handler = Building_features()
    
    tiles = list(tiles_from_slippy_map(mask_dir))

    for tile, path in tqdm(tiles, ascii=True, unit="mask"):
        predicted_tile = convert_binary(path)
        street_tile = convert_binary(path.replace("fake", "input"))
        # get only building footprints by finding difference of street networks and predicted imgs
        building_only = cv2.absdiff(street_tile, predicted_tile)
        mask = (building_only == 255).astype(np.uint8)
        handler.apply(tile, mask)
    
    # output feature collection
    feature = handler.jsonify()
    
    return feature

if __name__=="__main__":
    args = parser.parse_args()
    features = mask_to_feature(args.tile_dir)
    with open(args.out, "w") as fp:
        geojson.dump(features, fp)