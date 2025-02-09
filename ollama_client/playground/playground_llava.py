import ollama_client

def main():
  # Using LLaVA for image analysis
  with open('image.jpg', 'rb') as file:
    response = ollama_client.client().chat(
      model='llava:13b',
      messages=[
        {
          'role': 'user',
          'content': 'What are a rough area containing "right ear"? '
              'Return relative coordinates between 0 and 1 in the format '
              '"left,top,width,height" (no quotes). ',
          'images': [file.read()],
        },
      ],
    )

  print(response['message']['content'])


if __name__ == '__main__':
  main()