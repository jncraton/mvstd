import sys
import os
import re
import argparse

def has_ext(filename, ext):
  """
  >>> has_ext('test.mp3',['opus','mp3','aac'])
  True
  >>> has_ext('test.mp4',['opus','mp3','aac'])
  False
  >>> has_ext('test.opus.gz',['opus','mp3','aac'])
  False
  >>> has_ext('test.1.OPUS',['opus','mp3','aac'])
  True
  """

  return filename.split('.')[-1].lower() in ext

def is_audio(f): return has_ext(f, ['opus','mp3','aac','m4a','ogg'])
def is_video(f): return has_ext(f, ['mp4','avi','mov','mkv'])
def is_image(f): return has_ext(f, ['png','jpeg','jpg'])
def is_media(f): return is_audio(f) or is_video(f) or is_image()

def normalize(filename):
  """
  >>> normalize('Test 1.txt')
  'test-1.txt'
  >>> normalize('another-TEst_file.mp4')
  'another-test-file.mp4'
  >>> normalize('Linkin Park - In the End (Official Video)-HJCw2w8f23.opus')
  'linkin-park-in-the-end.opus'
  """
  if is_audio(filename): pass

  path = filename.split('/')[:-1]
  filename = filename.split('/')[-1]

  filename = filename.lower().replace('_','-').replace(' ','-').replace('–','-')

  if is_audio(filename):
    filename = re.sub(r'[\(\[].*?[\)\]]','', filename) # Remove parentheticals

  words = filename.split('-')

  words = [re.sub("[A-z0-9]*[0-9]+[A-z]+[0-9]+[A-z0-9]*",'',w) for w in words]

  words = filter(None, words)

  filename = '-'.join(words)

  filename = re.sub(r'[\'\!\:\,]','', filename)

  filename = re.sub(r'-+\.+','.', filename)

  filename = re.sub(r'\-+','-', filename)

  return '/'.join(path + [filename])

def main():
    ap = argparse.ArgumentParser(description='Rename files to a standard format')
    ap.add_argument('files', nargs='+', help="List of files")
    args = ap.parse_args()

    for file in args.files:
        os.rename(filename, normalize(filename))    
