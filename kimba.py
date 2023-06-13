import difflib
import os


def check_code_plagiarism(code_file, repository_path):

    with open(code_file, 'r') as file:
        code = file.read()

    repo_files = []
    for root, _, files in os.walk(repository_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as repo_file:
                    repo_files.append(repo_file.read())

    plagiarism_results = []
    for repo_code in repo_files:
        similarity = calculate_similarity(code, repo_code)
        if similarity >= 80:
            plagiarism_results.append((similarity, repo_code))

    if plagiarism_results:
        print("Plagiarism Detected:")
        for similarity, repo_code in plagiarism_results:
            print(f"- Similarity: {similarity}%")
            print(f"  Matched Code:\n{repo_code}")
            print()
    else:
        print("No plagiarism detected.")


def calculate_similarity(code1, code2):
    matcher = difflib.SequenceMatcher(None, code1, code2)
    similarity = matcher.ratio() * 100
    return similarity


code_file_path = "/Users/info/Desktop/test/manage.py"
repository_path = "/Users/info/Desktop/test/Social_Media/Social_book/social_book"

check_code_plagiarism(code_file_path, repository_path)
