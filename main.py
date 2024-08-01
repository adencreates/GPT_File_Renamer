from openai import OpenAI
import os
import time

# Function to read the content of a file
def read_file(file):
    with open(file, "r") as f:  # Use a context manager to open the file
     return f.read()  # Read and return the entire file content

# Function to clean the filename using OpenAI's chat completion
def cleanname(filename):
    prompt = Clean_String + filename  # Create a prompt by combining the Clean_String and filename
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You process data. You answer with plain-text. You do not explain answers."},
            {"role": "user", "content": prompt}
        ]
    )
    response = response.choices[0].message.content
    return(response)

# Function to modify the filename using OpenAI's chat completion
def modifyname(filename):
    prompt = Modify_String + filename  # Create a prompt by combining the Clean_String and filename
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You process data. You answer with plain-text. You do not explain answers."},
            {"role": "user", "content": prompt}
        ]
    )
    response = response.choices[0].message.content
    return(response)

api_key1 = read_file("api_key.txt")
client = OpenAI(api_key=api_key1)

# Read the clean string prompt from a file
Clean_String = read_file("Clean_String.txt")

# Read the modify string prompt from a file
Modify_String = read_file("Modify_String.txt")

# Get the project root directory
project_root = os.getcwd()

# Ask the user for the directory path
print("Please enter the path to the files you want to rename:")
directory_path = input()
print("\n")

if directory_path == project_root:
    print("The directory you entered is the project root. Please choose a different directory, either within or outside the project root.")
    directory_path = input()
    print("\n")

# Loop through all files in the specified directory
for path in os.listdir(directory_path):
    if path.lower() == ".ds_store":
        continue
    else: print("Input: " + path)
    suffix = path.split(".")[-1]
    time.sleep(1)  # Add a delay of 1 second between iterations
    cleaned = cleanname(path)  # Clean the filename
    cleaned = cleaned.lstrip()  # Remove leading whitespace from the cleaned filename
    cleaned = cleaned.replace(",", "")
    modded = modifyname(cleaned)  # Modify the cleaned filename
    modded = modded.lstrip()  # Remove leading whitespace from the modified filename
    modded = modded.replace(",", "")
    # Rename the file with the modified filename and add .nkg extension
    newfilename = modded + "." + suffix
    print("Output: " + newfilename)
    os.rename(os.path.join(directory_path, path), os.path.join(directory_path, newfilename))
    print("\n")
