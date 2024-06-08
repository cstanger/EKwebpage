import os
import json

EPISODES_STORAGE_DIR = 'src/content/podcast'
TRANSCRIPT_STORAGE_DIR = 'src/data/transcripts'

def build_correct_file_path(file_path) -> str:
    """
    Build the correct path to files.

    If a python script gets called from `scripts` folder, 
    we need to get a level up.
    This function takes care about the correct path.
    """
    p = file_path

    # Determine if the script is called from root
    # or from the scripts directory.
    directory_path = os.getcwd()
    folder_name = os.path.basename(directory_path)
    if folder_name == "scripts":
        p = f"../{file_path}"
    
    return p


def get_podcast_episode_number_from_filename_number(filename) -> int:
    """
    A podcast episode filename is like `94-die-realität-des-freelancings-zwischen-selbstbestimmung-und-unsicherheit-mit-index-out-of-bounds.md`
    In the example, 94 is the episode number.

    This function retrieves the episode number from the episode filename.
    """
    index = filename.find('-')

    # We have one episode which starts with '-1'
    # If we search for '-', we get the minus sign.
    # Hence we need to skip it.
    if index == 0:
        index = filename[1:len(filename)].find('-')
        episode_number = filename[0:index+1]
        episode_number = int(episode_number) * -1

    else:
        episode_number = filename[0:index]

    return episode_number


def has_podcast_episode_a_transcript(episode_number) -> bool:
    """
    Checks if the given {episode_number} (e.g. 94) has a transcript.
    Returns True is yes, False otherwise.
    """
    transcript_file = f"{episode_number}-transcript-slim.json"
    file_path = build_correct_file_path(TRANSCRIPT_STORAGE_DIR) + '/' + transcript_file

    return os.path.exists(file_path)


def get_podcast_episode_transcript_by_number(number):
    """
    Reads and returns the transcript of a particular episode number.
    """
    episode_number = number.zfill(2)
    file_path = f"{build_correct_file_path(TRANSCRIPT_STORAGE_DIR)}/{episode_number}-transcript-slim.json"
    with open(file_path) as f:
        data = json.load(f)

    return data
