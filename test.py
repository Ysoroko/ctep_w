# working, provoking win dll error
import os
from pathlib import Path,WindowsPath
import zipfile
from urllib import request
from pathlib import Path
from platform import system
import ctypes

def path_file(filename):
    return os.path.join(os.path.abspath(os.path.dirname(filename)), filename)

def download_from_url(download_url, path_to_filename):
    try:
        request.urlretrieve(download_url, path_to_filename)
        print('Downloaded %s from %s', path_to_filename, download_url)
    except Exception as e:
        print('Failed to download %s : %s', download_url, e)

def unzip_file(path_to_filename, path_to_extract):
    try:
        with zipfile.ZipFile(path_file(path_to_filename)) as zip_file:
            print('ok')
            zip_file.extractall(path_file(path_to_extract))
        print('ok1')
        os.remove(path_file(path_to_filename))
        print('ok2')
        print('Unzipped %s to %s', path_to_filename, path_to_extract)
    except Exception as e:
        print('Failed to unzip %s : %s', path_to_filename, e)
print('----')
print(Path(__file__))
print(Path(__file__).parent.resolve())
print(Path(__file__).parent.resolve().parent.resolve()) # works
print((Path(__file__).parent.resolve().parent / 'lib/ctep/').resolve()) # works

# print(Path(__file__).parents[2])
print('----')

lib_path = (Path(__file__).parent.resolve().parent / 'lib').resolve()
lib_extension = 'so' if system() == 'Linux' else 'dll'
easyCTEPPath = lib_path / f'ctep_w-main/libeasyctep.{lib_extension}' # to check
print(easyCTEPPath)

# path to download = "(Path(__file__).parent.resolve().parent / 'lib').resolve()"
# path to unzip = path to download
# path to ctypes = path_to_unzip / 'ctep_w_main

if __name__ == '__main__':
    if not easyCTEPPath.exists():
        # To adapt to real nightly download files
        download_from_url('https://github.com/Ysoroko/ctep_w/archive/refs/heads/main.zip', lib_path  / 'ctep.zip')
        unzip_file(lib_path / 'ctep.zip', lib_path) #fails if not ran as admin
    else:
        easyCTEP = ctypes.CDLL(str(easyCTEPPath)) if system() == 'Linux' else ctypes.WinDLL(str(easyCTEPPath))
    print(str(easyCTEP))
