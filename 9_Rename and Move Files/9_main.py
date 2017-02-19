import os

prev_name = 'rename_me.txt'
new_name = 'renamed.txt'  # we can even change to .doc or whatever
os.rename(prev_name, new_name)

prev = 'move_me.txt'
new = 'sample_folder/move_me.txt'
os.rename(prev, new)
