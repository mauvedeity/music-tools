#!/usr/local/bin/python3

from multiprocessing import Pool as ThreadPool
from multiprocessing import cpu_count
from subprocess import Popen, DEVNULL, STDOUT
import sys
import os
import id3reader_p3

def mkcmdline(fname):
        newname = os.path.splitext(fname)[0] + '.mp3'
        shellex = ['ffmpeg','-i']
        shellex.append(fname)
        shellex.append('-f')
        shellex.append('mp3')
        shellex.append('-y')
        shellex.append(newname)
        return(shellex,newname)

def transcode_item(name):
        shellex,mp3name = mkcmdline(name)
        print('--->', name)
        p = Popen(shellex, stdout=DEVNULL, stderr=DEVNULL)
        p.wait()
        processfile(mp3name)
        print('<---', name)

def multiprocess(fnames, proc_kount):
        print("Starting to process...")
        pool = ThreadPool(proc_kount)
        process = pool.map(transcode_item, fnames)
        pool.close()
        pool.join()
        print("All done")

def getfilescurdir():
        files = []
        filect = 0
        with os.scandir('.') as dirlist:
                for dirent in dirlist:
                        if not dirent.name.startswith('.'):
                                if (dirent.is_file() and os.path.splitext(dirent.name)[1] == '.m4a'):
                                        files.append(dirent.name)
                                        filect += 1
        print(filect, "files found")
        return(files)

def process():
        use_cores = 0
        if(len(sys.argv) == 2):
                uc = sys.argv[1]
                if (uc.isdigit()):
                        use_cores = int(uc)
        if(use_cores == 0):
                use_cores = cpu_count()
        print("Using", use_cores, "CPUs")
        multiprocess(getfilescurdir(), use_cores)

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

def procexistmp3():
        files = os.listdir(os.getcwd())
        for f in files:
                if ('.mp3' == f[-4:]):
                        processfile(f)

if __name__ == '__main__':
        process()
        procexistmp3()
