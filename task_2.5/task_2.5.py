import os
import subprocess

# create folder in working directory with given name
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print('Folder "' + folder_name + '" created.')
    else:
        print('Folder "' + folder_name + '" already exists.')

# image resize for source to result folder
def image_resize(source_folder, result_folder, resize_pixels):
    for image in os.listdir(source_folder):
        if os.path.splitext(image)[1] == '.jpg':
            from_file = os.path.join(source_folder, image)
            to_file = os.path.join(result_folder, image)
            command_line = 'convert ' + from_file + ' -resize ' + str(resize_pixels) + ' ' + to_file
            try:
                subprocess.run(command_line)
                print(command_line, ' ...done')
            except:
                print(command_line, ' ...error')

source_folder = 'Source'
result_folder = 'Result'

create_folder(result_folder)
image_resize(source_folder, result_folder, 200)
