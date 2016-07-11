# Random-Word-Generator
Randomly generates a (theoretically) pronounceable word.

###What's this here thing?
It basically generates a word with a length of your choosing. It's (probably) not a real word, whatever it is that you generate. I did get it to generate the word 'lulz' once, so this program does seem to have a predisposition to dated memes.

###How to use
This was written in Python 3.5.2. Just run the script and you'll get a random, 5 letter word which at this time only excludes the letter 'q'.
Using the -l or --length argument will control how long the word is, -b or --begin will let you choose what letter the word starts with, and -e or --exclude will allow you to choose a letter to exclude. You **must** pass -e for every letter you want to exclude, like so:

__$ python3 dictionarymaker.py -e a -e b -e c__

The above will exclude a, b, and c.

###This code sucks
I know.

#####Known Bugs:
If you exclude too many letters, your entire exclusion will fall apart possibly (likely), and it'll just generate a five letter word. This has been known to happen pretty much no matter what if you exclude all the vowels. Who would've thought, wow.
