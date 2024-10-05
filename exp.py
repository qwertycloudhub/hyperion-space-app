from os.path import join
import os
from obspy import read

print("i")
def get_all_mseed_files(dir=""):
    return [join(dir, file) for file in os.listdir(dir) if file.endswith("mseed")]

def filter(trace):
    return trace

def main():
    all_mseed_files = get_all_mseed_files(dir="./data/mars/training/data")
    print(all_mseed_files)
    data_list = []
    print(all_mseed_files)

    for file in all_mseed_files:
        data_stream = read(file)
        
        print(data_stream.__dict__)
main()