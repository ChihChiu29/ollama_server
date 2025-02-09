import sys
from loguru import logger

import fileutil
import ollama_client

MODEL = 'deepseek-r1:8b'
# Do not write to file until this is seen.
NO_WRITE_UNTIL = '</think>'

INPUT_PROMPT_FILENAME = 'drama_prompt.txt'
OUTPUT_FILENAME = 'drama.txt'

SYSTEM_SETTING = {
  'role': 'system',
  'content': '你是一个童话作者，你擅长用中文写童话，你从来不用中文',
}

PRINT_CONTENT = True

def maybeprint(content, no_new_line=False):
  if PRINT_CONTENT:
    if no_new_line:
      print(content, end='')
    else:
      print(content)


def generate_new_story(input_prompt_filename: str, output_filename: str):
  user_prompt = open(input_prompt_filename).read()
  logger.info('Got user prompt:')
  logger.info(user_prompt)
  
  prompt = f'''
根据之前的故事继续续写下去：

${user_prompt}
  '''

  should_write = False
  with open(output_filename, 'w') as file:
    for next_chunk in ollama_client.quickchat_stream(MODEL, [
      SYSTEM_SETTING,
      {
        'role': 'user',
        'content': prompt,
      },
    ]):
      if should_write:
        file.write(next_chunk)
      if NO_WRITE_UNTIL in next_chunk:
        should_write = True
      maybeprint(next_chunk, no_new_line=True)
    file.flush()


def continue_story(previous_drama_filename: str, append_to_filename: str):
  user_prompt = open(previous_drama_filename).read()
  logger.info('Previous story:')
  logger.info(user_prompt)
  
  prompt = f'''
${user_prompt}
  '''
  
  should_write = False
  with open(append_to_filename, 'a') as file:
    for next_chunk in ollama_client.quickchat_stream(MODEL, [
      SYSTEM_SETTING,
      {
        'role': 'user',
        'content': prompt,
      },
    ]):
      if should_write:
        file.write(next_chunk)
      if NO_WRITE_UNTIL in next_chunk:
        should_write = True
      maybeprint(next_chunk, no_new_line=True)
    file.flush()



def main():
  cmd = 'NONE'
  try:
    cmd = sys.argv[1]
  except IndexError:
    pass
  
  if cmd == 'continue':
    continue_story(OUTPUT_FILENAME, OUTPUT_FILENAME)
  else:
    generate_new_story(INPUT_PROMPT_FILENAME, OUTPUT_FILENAME)


if __name__ == '__main__':
  main()