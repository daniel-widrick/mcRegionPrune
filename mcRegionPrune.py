import sys, os, argparse


def pruneWorld(path, keepRadius):
    chunkRadius = int(keepRadius / 16)
    chunkRadius += 1; #Conservative

    regionFileList = os.listdir(path)
    for regionFile in regionFileList:
        parts = regionFile.split(".")
        if regionFile.endswith(".mca"):
            if abs(int(parts[1])) > chunkRadius or abs(int(parts[2])) > chunkRadius:
                print(regionFile)


parser = argparse.ArgumentParser("Prune region files outside a given block radius")
parser.add_argument("-p","--path",required=True, help="Path to directory containing region files in world directory");
parser.add_argument("-b","--blocks",required=True, type=int, help="Block radius around 0,0 to keep");

args = parser.parse_args()
pruneWorld(args.path,args.blocks)
