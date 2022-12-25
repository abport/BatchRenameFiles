import os

# Set the directory where the files are located
directory = '/path/to/directory'

# Set the prefix and suffix for the new filenames
prefix = 'new_name_'
suffix = '.txt'

# Get a list of the files in the directory
files = os.listdir(directory)

# Iterate through the files, renaming them with the new prefix and suffix
for i, file in enumerate(files):
  old_name = os.path.join(directory, file)
  new_name = os.path.join(directory, prefix + str(i) + suffix)
  os.rename(old_name, new_name)

print('Renaming complete!')
