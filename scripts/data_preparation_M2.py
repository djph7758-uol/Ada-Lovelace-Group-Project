import os
import zipfile
import shutil

#https://drive.google.com/drive/u/0/folders/1HvZbaD2O02urkPgg87HHW8pugq4mHa6A

import urllib.request
import zipfile
import os
import shutil

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    for i in range(1, respondent_index + 1):
        # Construct the URL for the specific file (e.g., a1.txt, a2.txt, etc.)
        file_url = f"{cloud_url}/a{i}.txt"

        # Step 1: Download the file
        response = requests.get(file_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Step 2: Save the file as answers_respondent_X.txt
            with open(f"{path_to_data_folder}/answers_respondent_{i}.txt", "wb") as f:
                f.write(response.content)
            print(f"Downloaded and saved: answers_respondent_{i}.txt")
        else:
            print(f"Failed to download file: a{i}.txt")

    print("All files downloaded and saved!")