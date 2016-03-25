## What is it?

A simple script to delete images metadata automatically.

Written in Python.

## Requirements

- Install ExifTool.

- Copy scripts to otherFunctions folder (see that folder's README).

- Tested in Ubuntu.


## Usage

Run the script. It guides you with some questions.

### Usage example

1 In terminal execute the script.

```
$ python '/home/carlos/Escritorio/funciones/deleteMetadata.py'
```

2 Now the script guides you with questions.

```
$ python '/home/carlos/Escritorio/funciones/deleteMetadata.py' 
Delete metadata of all files in a folder (1) or only one image (2)?
>>> 1
Complete route of the folder with images (/../../..):
>>> /home/carlos/Descargas/images
WARNING: file a.png doesn't change (metadata must be already deleted)
Save and move original files to a folder (1) or delete them (2)?
>>> 1
New folder has been created: originalImages
Files moved to originalImages folder
Process completed
```
