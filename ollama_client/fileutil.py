# From ChatGPT
def read_file_in_chunks(file_path: str, chunk_size: int):
  with open(file_path, 'r') as file:
    chunk = []
    for i, line in enumerate(file, start=1):
      chunk.append(line)
      if i % chunk_size == 0:
        yield chunk  # Return the current chunk
        chunk = []  # Reset the chunk
    if chunk:  # Yield the last chunk if it has leftover lines
      yield chunk
