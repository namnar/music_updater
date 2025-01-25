import os
import tqdm
import shutil
from dotenv import load_dotenv


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
    source_path = os.path.join(source, file)
    destination_path = os.path.join(destination, file)

    shutil.copy2(source_path, destination_path)

  print("All missing files successfully copied o7")


def main():
  load_dotenv()

  # destination_path = os.getenv("MUSIC_DESTINATION_PATH")
  # source_path = os.getenv("MUSIC_SOURCE_PATH")

  destination_path = os.getenv("TEST1")
  source_path = os.getenv("TEST2")

  destination_list = get_music_folder(destination_path)
  source_list = get_music_folder(source_path)

  difference = get_song_difference(destination_list, source_list)
  print("Expected: All Night Radio, Alone")
  print(difference)


  # download_difference(destination_path, source_path, difference)

if __name__ == "__main__":
  main()
