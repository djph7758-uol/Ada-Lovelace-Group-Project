import os
import zipfile
import shutil

#https://drive.google.com/drive/u/0/folders/1HvZbaD2O02urkPgg87HHW8pugq4mHa6A

import urllib.request
import zipfile
import os
import shutil

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    os.makedirs(path_to_data_folder, exist_ok=True)

    zip_path = "quiz_answers.zip"

    print("Downloading ZIP file...")
    urllib.request.urlretrieve(cloud_url, zip_path)

    print("Extracting ZIP file...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("temp_extracted/")

    print("Renaming files...")
    for i in range(1, respondent_index + 1):
        old_filename = f"temp_extracted/a{i}.txt"
        new_filename = os.path.join(path_to_data_folder, f"answers_respondent_{i}.txt")
        shutil.move(old_filename, new_filename)

    os.remove(zip_path)
    shutil.rmtree("temp_extracted")
    print("Download and extraction complete!")

