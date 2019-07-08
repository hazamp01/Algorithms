import os
import time

# Source files from where we do start the process of saving
source_path = "/Users/mohanpraveenhazaru/Documents/Soup"

# Target path where we need to place the zip files
target_path = "/Users/mohanpraveenhazaru/Documents/targeted_zip"

target = target_path+os.sep+time.strftime('%y%m%d%h%m%s')+'.zip'

# Checking weather directory exixted or not
if not os.path.exists(target_path):
    os.makedirs(target_path)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source_path))
print('Zip command is:')
print(zip_command)
print('Running:')
# Checking weather it was zipped and saved in the targeted location
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

