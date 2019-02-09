# music-tools

Version v0.1 of these files were basically the files I wrote to automate the
process of creating usable MP3 CDs or SD card folders for playing media in the
cars I've owned over the last few years.

I've moved on somewhat, and I now have a more generic requirement to transcode
files from `M4A` to `MP3`. Because of circumstances. I therefore decided that
I'd fix one of the longer-standing irritations - that the original process was
single-threaded. Massive thanks to [Chris Kiehl](https://chriskiehl.com) for
this, who wrote an amazing article about how to do multiprocessing on Python,
[which you should totally check out
here](https://chriskiehl.com/article/parallelism-in-one-line).

However, using *that* meant having to port everything to Python 3. Which for us
Mac users means that the dependencies are now Python 3 and `ffmpeg`. The easiest
way to install both of those (if you have a Mac and don't have them already) is
[Homebrew](https://brew.sh), which I totally recommend the hell out of. Although,
as long as you have `python3` and `ffmpeg` on your path, you should be OK.

And then, of course, moving to Python 3 totally broke the ID3 tagging library I
was using. This was the `id3reader` code from [Ned Batchelder's web
site](https://nedbatchelder.com/code/modules/id3reader.html). Sadly, that's not
being updated any more, but [J-P Roberts](http://www.jpsoftware.co.uk/) ported
Ned's original code to Python3 [and made it available in the public domain
here](http://www.jpsoftware.co.uk/id3reader.html). Again, this is public domain
code, so I've included it here. I am grateful to both Ned Batchelder and J-P
Roberts, without whom none of this would have been possible. I've had to make
one set of changes to move libraries: `getValue` has to change to `get_value`.

Note that these scripts will only work unchanged on UNIX-family systems. Sorry,
Windows users, but as always I built all this for myself, and I have a Mac. Feel
free to download and have at rebuilding for Windows. Please credit me if you do
that, and if you can do it in a way that doesn't break the repo for me and UNIX
users, then I'll pull the edits. Of course, since this is licensed with GPL v3,
you can modify it however you want anyway.

## Major Changes

I originally put in some To-Dos - here's how I've progressed against them.

### I *think* I've fixed all of the Unicode bugs. Thanks, Beyoncé!

I've moved to Python 3, which meant that I could ditch quite a lot of the
Unicode messing about that I had to do before. To be fair, I haven't actually
checked this properly, but it seems to work.

### There's no indication of progress other than folders appearing.

There still isn't.

### It would be easier if you just ran one command, and it converted where necessary and moved afterwards

It does this now. For a folder with just `M4A` files in, it will convert a number
of files at once, and once the file is converted, it is moved to a sub-folder. You'll probably see
a bunch of folders appear quite quickly, and then not much change, because the script
moves the `MP3` files as it goes.

If there are any `MP3` file remaining after the `M4A` files are converted, they get moved 
into folders afterwards.

### It's single-threaded at the moment…

This is the big change. The script takes a parameter (see below) which controls how many
processes are kicked off at once. If you don't provide a parameter (or you pass 0), then
the script counts the number of CPUs in the machine, and runs that many jobs in parallel.
Note that the `MP3` move bit at the end is still single threaded, because there didn't seem
much point changing that - it's fast enough as it is.

## How To Use

Step 1 - put the executable files `transcode.py`, `mp3mover3.py`, and
`id3reader_p3.py` into the folder where your music files are. Run
`transcode.py`. Optionally specify how many processes you want:

```transcode.py``` - runs a process per CPU you have.

```transcode.py 1``` - uses only one process, so the same as the single-threaded version.

```transcode.py 16``` - runs 16 processes at once (if there are 16 or more files). If you
have 16 CPUs then I'm dead jealous!

Step 2 - move the new folders to the destination media. (Oh, check that you
don't have any compilation albums that have gone weird.) That's it.

If you just need to move `MP3` files, then you can use `mp3mover3.py` to do that. Or
you could probably just run `transcode.py`, as that will move `MP3` files as well. I've
left `mp3mover3.py` in the repo just in case it's useful.

## To Do

* I *think* I've fixed all of the Unicode bugs. Thanks, Beyoncé!

* See if there's a way to fix the Compilation Album issue. The script checks by
  looking for a custom tag called "`TCP`" - iTunes *seems* to set this to `1`
  for compilation albums, but not for regular albums. You'll know if this hasn't
  worked because you'll get far too many folders, many of which will have only
  one file in them. It's not fatal, but it's annoying.

* Clean up all the debug printing it does.

## Bugs

Well, I've not escaped something somewhere, because "Ty Dolla $ign" broke it
this time. Oddly, it was the file move piece that broke, so there's probably
just a set of double quotes missing somewhere.

## Dependencies

### ffmpeg

You'll need this. You can use `homebrew` to install it, or you can do a custom installation. Either is fine
as long as it appears in your path.

### id3reader_p3

As above, this is **public domain** code, with the explicit statement "Do with
it as you please" at the original distribution point:
[here](http://www.jpsoftware.co.uk/id3reader.html). Because of this statement, I
have included it here for your convenience, but I strongly suggest checking the
source just in case it's been updated.
