#!/bin/bash

for python_file_name in $(find $Folder_Path -name *.py)
do
   python $python_file_name
done