#!/usr/bin/python

import os
import id3reader

def ensuredir(artist, album):
  artist = artist.replace('/','_')
  album = album.replace('/','_')
  dirname = unicode('%s-%s' % (artist,album))
  if(not(os.access(dirname, os.F_OK))):
    os.mkdir(dirname)
  return(dirname)

def processfile(fname):
  id3r = id3reader.Reader(fname)
  album = unicode(id3r.getValue('album'))
  artist = unicode(id3r.getValue('performer'))
  title = unicode(id3r.getValue('title'))
  newdir = ensuredir(artist, album)
# os.system('mv "%s" "%s"' % (fname,newdir))
  os_str = 'mv '
  os_str += '"'
  os_str += fname.encode("utf-8", "ignore")
  os_str += '"'
  os_str += ' '
  os_str += '"'
  os_str += newdir.encode("utf-8", "ignore")
  os_str += '"'
  os.system(os_str)



def procallfiles():
  files = os.listdir(os.getcwd())
  for f in files:
    if ('.mp3' == f[-4:]):
      processfile(f)
  
procallfiles()


