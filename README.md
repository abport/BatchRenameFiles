# Batch Rename Files in a Directory

This is a script that automates the task of renaming a batch of files in a directory. 

This script can be very useful if you have a large number of files that you want to rename quickly and efficiently.

To use this script, you will need to have Python installed on your computer. You can then save the script to a file and run it from the command line or terminal.

Here is the script:

```python
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
```
To use this script, you will need to modify the following lines to suit your needs:

-   `directory`: This should be set to the full path of the directory where the files are located.
-   `prefix`: This is the string that will be used as the prefix for the new filenames.
-   `suffix`: This is the string that will be used as the suffix for the new filenames.

Once you have modified the script to suit your needs, you can run it by navigating to the directory where the script is saved and running the following command:

```python
python rename_files.py
```
This will execute the script and rename all of the files in the specified directory according to the prefix and suffix that you set.
