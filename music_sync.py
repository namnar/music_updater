import os
import tqdm


#get_music_file(path)
def get_music_folder(folder_path, extensions=('.m4a', '.mp3', '.wav')):
  """
  returns a list of music from the given folder
  """
  return {song for song in os.listdir(folder_path) if song.endswith(extensions)}


def get_song_difference(destination, source):
  """
  returns the list of songs present in the target folder that are not in the source folder
  """
  source_file = get_music_folder(destination)
  target_file = get_music_folder(source)

  difference = target_file - source_file

  return difference


def download_difference(destination, source, difference):
  """
  downloads given list of songs into source folder
  """
  # difference_p = [os.path.join(target, song) for song in difference] #turns names of songs into navigable absolute paths

  for file in tqdm(difference, desc="Copying Files..."):
    source_path = os.path.join()

  print('complete')


def main():
  print("hello")
  destination_path = r"C:\Users\danie\Music\Music"
  source_path = r"C:\Users\danie\Music\Music"

  destination_list = get_music_folder(destination_path)
  source_list = get_music_folder(source_path)

  difference = get_song_difference(destination_path, source_path)
  print(destination_list)


  download_difference(destination_path, source_path, difference)

if __name__ == "__main__":
  main()
