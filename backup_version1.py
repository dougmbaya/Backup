#! /usr/bin/env/ python3

#date:   2013-12-27 23:03:52
#author: huliyou
#brief:  This programe helps you to backup your important files.

import os
import time

# origin_source: the files or directories which you want to back up
origin_source = ['~/HLY/Algorithm','~/HLY/HTML5/HTML5/bg/nightbg.jpg']

# main_backup_directory: the main backup directory which
# your all backup files will put in here.
main_backup_directory = '~/workspace/Python_space/Backup'


#backup_source: the name of your compress backup file.
backup_source = main_backup_directory + os.sep + time.strftime('%Y%m%d%H%M%s') + 'zip'

#compress command
zip_command = 'zip -qr {0} {1}'.format(backup_source, ' '.join(origin_source))


if os.system(zip_command) == 0:
    print('backup successfully to', main_backup_directory)
else:
    print('bckup failed!')
