__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile


base_dir = os.getcwd()
cache_dir = os.path.join(base_dir, "cache")
zip_name = "data.zip"


def clean_cache():
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    os.mkdir(cache_dir)


def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, "r") as zip:
        zip.extractall(cache_dir)


# Calling the functions
# clean_cache()

"""

import os
import shutil

map_name = "cache"
parrent_dir = os.getcwd()
dir = os.path.join(parrent_dir, map_name)


def clean_cache():
    # Check of onze foldermap bestaat
    if os.path.isdir(dir):
        # Welke bestanden zitten er in de map?
        current_files = os.listdir(map_name)
        # Ga elke bestand in de map langs
        for file in current_files:
            # En verwijder het bestand
            os.remove(os.path.join(dir, file))
    else:
        # Als onze foldermap nog niet bestaat: maak 'm dan
        os.mkdir("cache")


def cache_zip(zip_file_path, cache_dir_path):
    shutil.unpack_archive(zip_file_path, cache_dir_path)


def cached_files():
    cache_list = []
    path = os.getcwd()
    os.chdir(dir)
    for file in os.listdir(dir):
        cache_list.append(os.path.abspath(file))
    os.chdir(path)
    return cache_list


def find_password(list):
    # Ga de lijst met bestandsnamen langs
    for file in list:
        # Open het bestand
        with open(file, "r") as f:
            # Inhoud lijn voor lijn lezen
            for line in f:
                # Op zoek naar de term password
                if "password" in line:
                    # Gevonden. Nu de lijn splitten.
                    split = line.split()
                    # En nu het item na password selecteren om te returnen
                    return split[1]
"""
