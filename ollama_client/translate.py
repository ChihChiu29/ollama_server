from loguru import logger

import fileutil
import ollama_client

MODEL = 'llama3.2'
CHUNK_LINE_SIZE = 60

PRINT_CONTENT = False

def maybeprint(content):
  if PRINT_CONTENT:
    print(content)

def quickchat(prompt: str) -> str:
  return ollama_client.quickchat(MODEL, [
    {
      'role': 'system',
      'content': 'You are a professional translator who *always translates Chinese into English*. You try to stay faithful to the original content, and you are very consistent.'
    },
    {
      'role': 'user',
      'content': prompt,
    },
  ])


def translate(source_filename: str, target_filename: str):
  previous_translated_chunk = None

  line_count = 0
  with open(target_filename, 'w') as file:
    for chunk in fileutil.read_file_in_chunks(source_filename, chunk_size=CHUNK_LINE_SIZE):
      previous_instruction = ''
      chunk_joined = '\n'.join(chunk)
      if previous_translated_chunk:
        previous_instruction = f'''
You have previously translated the following content, use it as reference and make sure the new translation is consistent with
previous ones. In particular, make sure the name choices are consistent.

===== PREVIOUS_CONTENT START =====
{previous_translated_chunk}
===== PREVIOUS_CONTENT END =====
'''

      prompt = f'''
Translate the following *into English*. Do not give any commentary or suggestions, just translates it.
If previously translated content is also given, use it as reference.
Combine multiple empty lines in a row into a single one.

===== CONTENT TO TRANSLATE =====
{chunk_joined}

Here is the translated content in English:
'''
      maybeprint(prompt)
      translated_chunk = quickchat(prompt)
      maybeprint(translated_chunk)

      short_translated_chunk = translated_chunk.replace('\n\n', '\n').replace('\n\n', '\n')
      file.write(short_translated_chunk)
      file.flush()

      previous_translated_chunk = short_translated_chunk

      line_count += CHUNK_LINE_SIZE
      logger.info(f'Processed lines: {line_count}')
      # if line_count > 400:
      #   return


def main():
  translate('source.txt', 'translated.txt')


if __name__ == '__main__':
  main()