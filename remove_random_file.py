import create_backup_dir
import os
import random

src_dir_loc = "E:/Courses/Data Science/Epsilon/Lecture_4_Thanos_Project/Thanos_Project/Universe"
bkp_dir_loc = "E:/Courses/Data Science/Epsilon/Lecture_4_Thanos_Project/Thanos_Project/Backup/"

# call perfrom_backup function & create backup
create_backup_dir.perform_backup(src_dir_loc,bkp_dir_loc)

# get list of folder files to remove random 
folder_files = os.listdir(src_dir_loc)
# check folder files before removing files
print(len(folder_files))

# looping on directory & remove 50% of random files 
for file in random.sample(folder_files,int(len(folder_files)/2)):
    os.remove(os.path.join(src_dir_loc,file))
print("Files removed successfuly, folder contains{}".format(len(os.listdir(src_dir_loc))))