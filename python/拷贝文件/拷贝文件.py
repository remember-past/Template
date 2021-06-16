import shutil

share_dir = r"\\tsclient\share\data\CellCycle\experiment\downsampling_simulation"
old_path = os.path.join(output_file_dir, output_file_name)
new_path = os.path.join(share_dir, output_file_name)
shutil.copyfile(old_path, new_path)