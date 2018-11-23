# music-tools
These are the files I wrote to automate the process of creating usable MP3 CDs
or SD card folders for playing media in the cars I've owned over the last few
years.

Note that these scripts will only work on UNIX-family systems. Sorry, Windows
users, but as always I built all this for myself, and I have a Mac. Feel free
to download and have at rebuilding for Windows. Please credit me if you do
that, and if you can do it in a way that doesn't break the repo, then I'll 
pull the edits.

## How To Use

Step 1 - Just dump all of the files into the same folder where you cloned the
repo. This was the original use case, because that's what happens when you drag
a playlist or several out of iTunes. 

Step 2 - if the files are M4As, not MP3s, and you don't have another way to
batch convert the files, then use the `convert.sh` script to process them into
MP3 format. This can be automated using `find`:
```bash
find . -name "*.m4a" -exec convert.sh {} \;
```
should work to convert all of the files. Note that this **requires** that
`ffmpeg` is on your path. 

Step 3 - run `mp3mover.py` to move all of the files into folders. If the iTunes 'compilation' flag is set
then the file will be treated as part of a compilation album, otherwise it's treated as a regular album.
The difference is, a regular album's files will be moved into a folder named "Artist-Album", whereas
a compilation album's files will go into a folder called "Album". 

The script checks by looking for a custom tag called "`TCP`" - iTunes *seems* to set this to `1`
for compilation albums, but not for regular albums. You'll know if this hasn't worked because you'll
get far too many folders, many of which will have only one file in them. It's not fatal, but it's annoying.

Step 4 - move the folder structure, minus the script files, to your destination media.

## To Do

* I *think* I've fixed all of the Unicode bugs. Thanks, Beyoncé!
* There's no indication of progress other than folders appearing.
* It would be easier if you just ran one command, and it converted where
  necessary and moved afterwards.
* It's single-threaded at the moment, so only one `ffmpeg` conversion process gets
  kicked off at a time, which leads to a fair bit of under use of the processor.
  It'd be nice if it would do multiple file conversions.

## Bugs

I don't know of any at the moment. Do let me know if you find any.

## Dependencies

### ffmpeg
You'll need this. You can use `homebrew` to install it, or you can do a custom installation. Either is fine
as long as it appears in your path.

### id3reader
The `id3reader` code comes from
[Ned Batchelder's web site](https://nedbatchelder.com/code/modules/id3reader.html)
but that doesn't seem to have been updated for a while, sadly.
I've included it here as the page above clearly states this
code is in the public domain. Follow the link for more information.



