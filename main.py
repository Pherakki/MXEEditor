import getopt
import os
import sys

from pyValkLib import MXE

from CSVExtract import interface_to_csvs
from CSVPack import csvs_to_interface

usage_string = "Usage:\n" + \
               "  -h/--help  : Prints the help string.\n" + \
               "  -r         : Packs/unpacks all MXEs in a supplied folder.\n" + \
               "  -u/--unpack: Unpacks an MXE file. If paired with '-r', it unpacks all MXEs in a folder.\n" + \
               "  -p/--pack  : Packs an MXE file. If paired with '-r', it packs all MXEs in a folder.\n" + \
               "  -o/--out   : Output directory."

def is_mxe_file(filepath):
    return os.path.isfile(filepath) and os.path.splitext(filepath)[-1] == os.path.extsep + "mxe"

def unpack_mxe_file(in_path, out_dir):
    mxec = MXE.init_from_file(in_path)
    interface_to_csvs(out_dir, mxec, os.path.splitext(os.path.split(in_path)[1])[0])

def pack_mxe_file(in_path, out_path):
    filename = os.path.split(in_path)[1]
    mxec = csvs_to_interface(in_path)
    mxe = MXE.init_from_mxecinterface(mxec)
    mxe.write(os.path.join(out_path, filename + os.path.extsep + "mxe"))

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hru:p:o:",["help","unpack=","pack=","out="])
    except getopt.GetoptError:
        print("Arg parsing error.")
        print(usage_string)
        sys.exit(2)

    recursive = False
    unpack_path = None
    pack_path = None
    output_path = None
    for opt, arg in opts:
        if opt == '-h':
            print(usage_string)
            sys.exit()
        elif opt == "-r":
            recursive = True
        elif opt in ("-u", "--unpack"):
            if unpack_path is not None:
                print("Unpack location specified twice. ONLY provide -u or --unpack.")
                exit(2)
            
            if pack_path is not None:
                print("Both pack and unpack locations specified. ONLY provide -u/--unpack or -p/--pack.")
                exit(2)
                
            unpack_path = arg
        elif opt in ("-p", "--pack"):
            if pack_path is not None:
                print("Pack location specified twice. ONLY provide -p or --pack.")
                exit(2)
            
            if unpack_path is not None:
                print("Both pack and unpack locations specified. ONLY provide -u/--unpack or -p/--pack.")
                exit(2)
                
            pack_path = arg
        elif opt in ("-o", "--out"):
            if output_path is not None:
                print("Output location specified twice. ONLY provide -o or --out.")
                exit(2)
            output_path = arg
            
    if unpack_path is not None:
        if recursive:
            if output_path is None:
                output_path = unpack_path
            os.makedirs(output_path, exist_ok=True)
            
            files = sorted([f for f in os.listdir(unpack_path) if is_mxe_file(os.path.join(unpack_path, f))])
            n_files = len(files)
            longest_name = max([len(nm) for nm in files])
            print()
            for i, file in enumerate(files):
                diff = longest_name - len(file)
                padding = " "*diff
                print(f"\rUnpacking file {i+1}/{n_files}... [{file}]{padding}", end="")
                filepath = os.path.join(unpack_path, file)
                unpack_mxe_file(filepath, output_path)
            print("\nDone.")
            exit()
        else:
            if output_path is None:
                output_path = os.path.split(unpack_path)[0]
            if is_mxe_file(unpack_path):
                print(f"Unpacking {unpack_path}...")
                unpack_mxe_file(unpack_path, output_path)
                print("Done.")
                exit()
            else:
                print(f"{unpack_path} is not an MXE file.")
                exit(2)
    elif pack_path is not None:
        if recursive:
            if output_path is None:
                output_path = pack_path
            os.makedirs(output_path, exist_ok=True)
            
            files = sorted([f for f in os.listdir(pack_path) if os.path.isdir(os.path.join(pack_path, f))])
            n_files = len(files)
            longest_name = max([len(nm) for nm in files])
            print()
            for i, folder in enumerate(files):
                diff = longest_name - len(folder)
                padding = " "*diff
                print(f"\rPacking file {i+1}/{n_files}... [{folder}]{padding}", end="")
                filepath = os.path.join(pack_path, folder)
                pack_mxe_file(filepath, output_path)
            print("\nDone.")
            exit()
        else:
            if output_path is None:
                output_path = os.path.split(pack_path)[0]
            if os.path.isdir(pack_path):
                print(f"Packing {pack_path}...")
                pack_mxe_file(pack_path, output_path)
                print("Done.")
                exit()
            else:
                print(f"{pack_path} is not a directory.")
                exit(2)
    else:
        print("Did not find a -u/--unpack or -p/--pack argument.")
        print(usage_string)
        sys.exit(2)

if __name__ == "__main__":
   main(sys.argv[1:])