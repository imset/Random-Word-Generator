# Random-Word-Generator
Randomly generates a (theoretically) pronounceable word.

###What's this here thing?
It basically generates a word with a length of your choosing. It's (probably) not a real word, whatever it is that you generate. I did get it to generate the word 'lulz' once, so this program does seem to have a predisposition to dated memes.

###How to use
There are two arguments: the first is how many letters you'd like it to be. Any number should work.
The second is, if you enter 'exclude', it will allow you to exclude certain letters from being generated in your word.
As always I made the whole thing a function because I have grand plans for this (not really, I made this to make coming up with names for my characters in DnD easier)
Running it without arguments defaults to a non-excluded 5 letter word.

###This code sucks
Trust me, I know that this is terrible. I realized a lot of the stuff in it is unnecessary. But screw it, I'm too tired right now to make it pretty.
Or commented. :^)
It Just Werks!

###How it'll get better
Not that you care, but it'll be improved on, definitely.
I intend to use a better arguments parser so that I can make the whole thing work entirely from the command line.
Also, I hope to add the function to control what letter the whole thing starts with if you want, but don't hold your breath.

#####Known Bugs:
If you exclude too many letters, your entire exclusion will fall apart possibly (likely), and it'll just generate a five letter word. This has been known to happen pretty much no matter what if you exclude all the vowels. Who would've thought, wow.
This particular glitch made me double the size in my code, because I thought that I had to do some stupid roundabout solution to make the whole exclusion work. That's because in my bugtesting, I was removing all the vowels from generated words, and it would default back to removing my exclusion. I'm dumb!
