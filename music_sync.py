import os



#get_music_file(path)
def get_music_folder(folder_path, extensions=('.m4a', '.mp3', '.wav')):
  """
  returns a list of music from the given folder
  """
  return {song for song in os.listdir(folder_path) if song.endswith(extensions)}


def get_song_difference(source, target):
  """
  returns the list of songs present in the target folder that are not in the source folder
  """
  source_file = get_music_folder(source)
  target_file = get_music_folder(target)

  difference = target_file - source_file
  difference = [os.path.join(target, song) for song in difference]

  return difference


def download_difference(source, difference):
  """
  downloads given list of songs into source folder
  """
  print('complete')


def main():
  print("hello")
  source = r"C:\Users\danie\Music\Music"
  music_list = get_music_folder(source)
  music_list = [os.path.join(source, song) for song in music_list]
  print(music_list)

if __name__ == "__main__":
  main()
