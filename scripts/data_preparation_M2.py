import requests
import os

def download_answer_files(cloud_url, path_to_data_folder, respondent_index):
    for i in range(1, respondent_index + 1):
        file_url = f"{cloud_url}/a{i}.txt"
        response = requests.get(file_url)

        with open(f"{path_to_data_folder}/answers_respondent_{i}.txt", "wb") as f:
            f.write(response.content)
        
def collate_answer_files(data_folder_path):
    with open("output/collated_answers.txt", "w") as outfile:
        for i in range(1, 26):
            file_path = f"{data_folder_path}/answers_respondent_{i}.txt"
            with open(file_path, "r") as infile:
                    outfile.write(f"Respondent {i}:\n")
                    outfile.write(infile.read())  
                    outfile.write("\n*\n")