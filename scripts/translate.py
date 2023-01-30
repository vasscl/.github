import sys
import os
import re
import time
from googletrans import Translator

def process_match(match):
  text = match[0]
  sha = str(hash(match[0]))
  shalist[sha] = text
  return sha

translator = Translator(service_urls=[
      'translate.google.com',
    ])

if len(sys.argv) < 4:
    print("Usage: python3 translate.py <destination language code> <source path> <destination path>")
    sys.exit()

shalist = {}
dest_lang = sys.argv[1]
source_path = sys.argv[2]
destination_path = sys.argv[3]

print(f"Translate to: {dest_lang}")
print(f"Source path: {source_path}")
print(f"Destination path: {destination_path}")
print("-----------------------------------------------------")

for dirpath, dirnames, files in os.walk(source_path, topdown=False):
  print(f"Processing files in {dirpath}")
  for file_name in files:
    file_path = os.path.join(dirpath, file_name)
    dest_file_path = os.path.join(dirpath.replace(source_path, destination_path), file_name)
    print(f"Processing file: {file_path}")

    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)

    with open(file_path, "r") as file:
      with open(dest_file_path, mode = "w") as dest_file:
        time.sleep(1)
        file_content = file.read()
        code_block_regexp = re.compile("```[a-z]*\n[\s\S]*?\n```")

        dehydrated_content = code_block_regexp.sub(process_match, file_content)

        translated_content = translator.translate(dehydrated_content, src="en", dest=dest_lang).text

        for sha, text in shalist.items():
          translated_content = translated_content.replace(sha, text)

        translated_content = translated_content.replace("** ", "**")
        translated_content = translated_content.replace(" **", "**")
        translated_content = translated_content.replace("] (", "](")
        shalist = {}
        dest_file.write(translated_content)
      dest_file.close()
    file.close()
