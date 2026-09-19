import h5py

file_path = "data/raw/2017-05-12_batchdata_updated_struct_errorcorrect.mat"

with h5py.File(file_path, "r") as f:
    print("Top-level keys:")
    for key in f.keys():
        print(" -", key)