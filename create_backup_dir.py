import datetime
import os
import shutil


src_dir_loc = ""                                       # source directory location
bkp_dir_loc = ""                                       # backup directory location                   

def get_backup_directory(base_directory):
    ''' create directory backup
        Args:
            base_directory: location path to create folder in
        return:
            directory concatinate with main folder name & date backup created 
    '''
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    folder_name = src_dir_loc.split("/")[-1]               # get folder naem to use in rename backup folder
    return bkp_dir_loc +"{0}_backup_{1}".format(folder_name,date)


def copy_files_to(srcdir,bkpdir):
    '''copy files to another directory
    Args:
        srcdir: source directory location
        bkpdir: Backup directory location
    '''
    for file in os.listdir(srcdir):
        file_path = os.path.join(srcdir,file)
        if os.path.isfile(file_path):
            shutil.copy(file_path,bkpdir)

def copy_files(srcdir,bkpdir):
    '''copy files
    Args:
        srcdir: source directory location
        bkpdir: Backup directory location
    '''
    copy_files_to(srcdir,bkpdir)

def perform_backup(srcdir,base_directory):
    backup_directory=get_backup_directory(base_directory)
    os.makedirs(backup_directory)
    copy_files(srcdir,backup_directory)
    print("Backup Craeted Successfuly")
