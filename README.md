# binln - symlinks to ~/bin/, the easy way

Too often I have to type this:

    ln -sv $PWD/foo.rb ~/bin/foo

`binln` is a tiny script that automates that.

    binln foo.rb

You can run it with `-f` to clobber a link, too.

## Installation

    ./binln.py binln.py
