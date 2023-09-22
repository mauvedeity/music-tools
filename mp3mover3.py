#!env python3

import os
import id3reader_p3

def ensuredir(artist, album):
  artist = artist.replace('/','_')
  album = album.replace('/','_')
  dirname = ('%s-%s' % (artist,album))
  if(not(os.access(dirname, os.F_OK))):
    os.mkdir(dirname)
  return(dirname)

def ensurecdir(album):
  album = album.replace('/', '_')
  dirname = album
  if(not(os.access(dirname, os.F_OK))):
    os.mkdir(dirname)
  return(dirname)

def processfile(fname):
  id3r = id3reader_p3.Reader(fname)
  album = id3r.get_value('album')
  artist = id3r.get_value('performer')
  title = id3r.get_value('title')
  iscomp = id3r.get_value('TCP')

  if (iscomp is None):
    newdir = ensuredir(artist, album)
  else:
    newdir = ensurecdir(album)

  os_str = 'mv "'
  os_str += fname
  os_str += '" "'
  os_str += newdir
  os_str += '"'
  os.system(os_str)
  print(os_str)

def procallfiles():
  files = os.listdir(os.getcwd())
  for f in files:
    if ('.mp3' == f[-4:]):
      processfile(f)
  
procallfiles()


