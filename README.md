# Usage:

1. Install dependencies:
   ```bash
   pip install openai
   ```

2. Open Terminal and navigate to the path where GPT_File_Renamer is saved.
   ```bash
   cd /Users/music/Documents/Git/GPT_File_Renamer
   touch API_Key.txt
   ```

3. Paste your API Key into API_Key.txt. You may find your key [here](https://help.openai.com/en/articles/7039783-how-can-i-access-the-chatgpt-api).

3. Replace the contents of `Clean_String.txt` and `Modify_String.txt` with your desired prompts for cleaning and modifying filenames.

4. Run the script.

## Purpose:
This script modifies filenames using OpenAI’s ChatGPT. It reads all filenames within a specified directory, processes them to remove unwanted characters, and then renames the files based on ChatGPT’s responses.