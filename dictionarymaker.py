import random
import sys
import argparse

def wordGen():
	parser = argparse.ArgumentParser(description='Generates a random, theoretically pronounceable word. The letter \'q\' is currently not 		generated due to how it breaks the flow of many words.')
	parser.add_argument('-e','--exclude', help='Excludes a character from word generation. Known to fail if all vowels are excluded. 		Example: using \'-e a -e f -e m\' all together will exclude a, f, and m.', action='append', required=False)
	parser.add_argument('-l','--length', help='Defines the length of the word. Defaults to 5 without.', required=False)
	parser.add_argument('-b', '--begin', help='Choose what letter the word will start with. Fails if there is more than one letter, or 		currently fails if the letter is \'q\'.', required=False)
	args = parser.parse_args()
	
	excludeList = [] #creates an empty list to add letters for exclusion.

	try:
		excludeList.extend(args.exclude)
	except Exception:
		pass

	#attempts to add the values of the -e arguments to excludeList. Only should fail if there are no excluded letters. This is a relic of the past, should be updated.

	try:
		if int(args.length) >= 1:
			arg1 = args.length
		else:
			arg1 = 5
	except:
		arg1 = 5

	#very similar to above, it very simply sets the value of arg1. This is also a relic of older versions, and will be updated. Sets default value of five if there was no -l flag or if the number inputted is less than one.

	totalLength = arg1 #there's that relic of the past I was talking about.


	totalWord = [] #totalWord will have every letter that is randomly generated in it, all seperated.
	allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z'] #allLetters is used to start off the whole thing. Q has been removed.
	# the following lists are of letters that can come after the list's name.
	a = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z'] #Q has been removed from this list.
	b = ['a','e','i','l','o','r','y']
	c = ['a','e','h','i','l','o','r','u','w','y']
	d = ['a','e','f','g','i','j','o','r','u','w','y']
	e = ['a','b','c','d','f','g','h','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z'] #Q has been removed from this list.
	f = ['a','e','i','l','o','r','u','w','y']
	g = ['a','e','h','i','l','o','r','u','w','y']
	h = ['a','e','i','o','u','y']
	i = ['a','b','c','d','e','f','g','k','l','m','n','o','p','r','s','t','v','x','z'] #Q has been removed from this list.
	j = ['a','e','i','o','u','y']
	k = ['a','e','i','l','o','r','u','w','y']
	l = ['a','e','i','o','u','y']
	m = ['a','e','i','o','u','y']
	n = ['a','e','i','o','u','y']
	o = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','r','s','t','u','v','w','x','y','z'] #Q has been removed from this list.
	p = ['a','e','h','i','l','o','r','u','w','y']
	# reminder: figure out how to implement Q in a non shitty way.
	r = ['a','e','i','o','u','y']
	s = ['a','c','e','h','i','k','l','m','n','o','p','t','u','v','w','y'] #Q has been removed from this list.
	t = ['a','e','h','i','o','r','u','w','y']
	u = ['b','c','d','e','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','z'] #Q has been removed from this list.
	v = ['a','e','i','o','u','w','y']
	w = ['a','e','i','o','r','u','y']
	x = ['a','e','i','o','u','y']
	y = ['a','e','i','o','u']
	z = ['a','e','i','o','u','w','y']
	# these lists are used to figure out the last letter based upon the letter before it.
	aend = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','u','v','w','x','y','z']
	bend = ['a','e','i','o','s','u','y']
	cend = ['a','c','e','h','k','o','r','s','u','y']
	dend = ['a','e','i','o','s','u','y']
	eend = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','r','s','t','v','w','x','z']
	fend = ['a','e','f','i','n','o','p','s','t','u','y','z']
	gend = ['a','e','h','i','n','o','s','u','y']
	hend = ['a','e','i','k','o','p','s','u','y']
	iend = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','v','w','x','z']
	jend = ['a','e','i','o','u','y']
	kend = ['a','e','i','k','o','s','u','y']
	lend = ['a','c','d','e','f','g','i','l','m','n','o','p','s','t','u','v','x','y','z']
	mend = ['a','b','e','f','i','k','m','n','o','p','s','t','u','y','z']
	nend = ['a','b','c','d','e','f','g','h','i','k','n','o','p','s','t','u','v','x','y','z']
	oend = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
	pend = ['a','e','f','h','i','o','p','s','t','u','y','z']
	# see the above Q reminder.
	rend = ['a','b','d','e','g','i','m','n','o','p','r','s','t','u','v','x','y','z'] #Q has been removed from this list.
	send = ['a','b','c','e','g','h','i','k','m','o','p','t','u','y']
	tend = ['a','e','h','i','o','s','t','u','y']
	uend = ['a','b','c','d','e','f','g','h','k','l','m','n','p','r','s','t','v','w','x','z']
	vend = ['a','e','g','i','k','o','s','t','u','y','z']
	wend = ['a','e','i','o','u','y']
	xend = ['a','e','i','o','u','x','y']
	yend = ['a','b','c','d','e','g','i','k','o','p','s','t','u','v','x','z']
	zend = ['a','e','i','o','u','y']

	#the following excludes the letters from excludeList from the lists a-z and aend-zend. This process can possibly make entirely blank lists, which is a problem if too many letters are excluded.
	
	allLetters = [ex for ex in a if ex not in (excludeList)]
	a = [ex for ex in a if ex not in (excludeList)]
	b = [ex for ex in b if ex not in (excludeList)]
	c = [ex for ex in c if ex not in (excludeList)]
	d = [ex for ex in d if ex not in (excludeList)]
	e = [ex for ex in e if ex not in (excludeList)]
	f = [ex for ex in f if ex not in (excludeList)]
	g = [ex for ex in g if ex not in (excludeList)]
	h = [ex for ex in h if ex not in (excludeList)]
	i = [ex for ex in i if ex not in (excludeList)]
	j = [ex for ex in j if ex not in (excludeList)]
	k = [ex for ex in k if ex not in (excludeList)]
	l = [ex for ex in l if ex not in (excludeList)]
	m = [ex for ex in m if ex not in (excludeList)]
	n = [ex for ex in n if ex not in (excludeList)]
	o = [ex for ex in o if ex not in (excludeList)]
	p = [ex for ex in p if ex not in (excludeList)]
	r = [ex for ex in r if ex not in (excludeList)]
	s = [ex for ex in s if ex not in (excludeList)]
	t = [ex for ex in t if ex not in (excludeList)]
	u = [ex for ex in u if ex not in (excludeList)]
	v = [ex for ex in v if ex not in (excludeList)]
	w = [ex for ex in w if ex not in (excludeList)]
	x = [ex for ex in x if ex not in (excludeList)]
	y = [ex for ex in y if ex not in (excludeList)]
	z = [ex for ex in z if ex not in (excludeList)]
	aend = [ex for ex in aend if ex not in (excludeList)]
	bend = [ex for ex in bend if ex not in (excludeList)]
	cend = [ex for ex in cend if ex not in (excludeList)]
	dend = [ex for ex in dend if ex not in (excludeList)]
	eend = [ex for ex in eend if ex not in (excludeList)]
	fend = [ex for ex in fend if ex not in (excludeList)]
	gend = [ex for ex in gend if ex not in (excludeList)]
	hend = [ex for ex in hend if ex not in (excludeList)]
	iend = [ex for ex in iend if ex not in (excludeList)]
	jend = [ex for ex in jend if ex not in (excludeList)]
	kend = [ex for ex in kend if ex not in (excludeList)]
	lend = [ex for ex in lend if ex not in (excludeList)]
	mend = [ex for ex in mend if ex not in (excludeList)]
	nend = [ex for ex in nend if ex not in (excludeList)]
	oend = [ex for ex in oend if ex not in (excludeList)]
	pend = [ex for ex in pend if ex not in (excludeList)]
	rend = [ex for ex in rend if ex not in (excludeList)]
	send = [ex for ex in send if ex not in (excludeList)]
	tend = [ex for ex in tend if ex not in (excludeList)]
	uend = [ex for ex in uend if ex not in (excludeList)]
	vend = [ex for ex in vend if ex not in (excludeList)]
	wend = [ex for ex in wend if ex not in (excludeList)]
	xend = [ex for ex in xend if ex not in (excludeList)]
	yend = [ex for ex in yend if ex not in (excludeList)]
	zend = [ex for ex in zend if ex not in (excludeList)]


	#if the -b argument exists and is a one letter string, it will set the value of firstLetter to the chosenn letter. Otherwise, it is random.
	if isinstance(args.begin, str) == True and len(args.begin) == 1 and args.begin.lower() != 'q':
		firstLetter = args.begin.lower()
	else:
		firstLetter = random.choice(allLetters)

	totalWord.append(firstLetter) #appends firstLetter to the total word.

	nextLetter = firstLetter #creates a new variable, nextLetter, which is for all intents and purposes the same as firstLetter. This is for readability purposes.

	while len(totalWord) < int(totalLength) - 1: #must be - 1 for the end letter function down below to work properly.
	#depending on the current value of nextLetter, this huge monster will decide which list to randomly pull the next value of nextLetter from.
		if nextLetter == 'a':
			nextLetter = random.choice(a)
		elif nextLetter == 'b':
			nextLetter = random.choice(b)
		elif nextLetter == 'c':
			nextLetter = random.choice(c)
		elif nextLetter == 'd':
			nextLetter = random.choice(d)
		elif nextLetter == 'e':
			nextLetter = random.choice(e)
		elif nextLetter == 'f':
			nextLetter = random.choice(f)
		elif nextLetter == 'g':
			nextLetter = random.choice(g)
		elif nextLetter == 'h':
			nextLetter = random.choice(h)
		elif nextLetter == 'i':
			nextLetter = random.choice(i)
		elif nextLetter == 'j':
			nextLetter = random.choice(j)
		elif nextLetter == 'k':
			nextLetter = random.choice(k)
		elif nextLetter == 'l':
			nextLetter = random.choice(l)
		elif nextLetter == 'm':
			nextLetter = random.choice(m)
		elif nextLetter == 'n':
			nextLetter = random.choice(n)
		elif nextLetter == 'o':
			nextLetter = random.choice(o)
		elif nextLetter == 'p':
			nextLetter = random.choice(p)
		#elif nextLetter == 'q':
			#nextLetter = random.choice(q)
		elif nextLetter == 'r':
			nextLetter = random.choice(r)
		elif nextLetter == 's':
			nextLetter = random.choice(s)
		elif nextLetter == 't':
			nextLetter = random.choice(t)
		elif nextLetter == 'u':
			nextLetter = random.choice(u)
		elif nextLetter == 'v':
			nextLetter = random.choice(v)
		elif nextLetter == 'w':
			nextLetter = random.choice(w)
		elif nextLetter == 'x':
			nextLetter = random.choice(x)
		elif nextLetter == 'y':
			nextLetter = random.choice(y)
		elif nextLetter == 'z':
			nextLetter = random.choice(z)
		#elif nextLetter == 'ou':
			#nextLetter = random.choice(u)
		else:
			print("An error has occured")
		totalWord.append(nextLetter) #appends the random value that was decided, and starts the loop anew until the length is satisfied.


	#the following will decide, based on the value of nextLetter, what the last letter should be from the sperate _end lists.
	if nextLetter == 'a':
		lastLetter = random.choice(aend)
	elif nextLetter == 'b':
		lastLetter = random.choice(bend)
	elif nextLetter == 'c':
		lastLetter = random.choice(cend)
	elif nextLetter == 'd':
		lastLetter = random.choice(dend)
	elif nextLetter == 'e':
		lastLetter = random.choice(eend)
	elif nextLetter == 'f':
		lastLetter = random.choice(fend)
	elif nextLetter == 'g':
		lastLetter = random.choice(gend)
	elif nextLetter == 'h':
		lastLetter = random.choice(hend)
	elif nextLetter == 'i':
		lastLetter = random.choice(iend)
	elif nextLetter == 'j':
		lastLetter = random.choice(jend)
	elif nextLetter == 'k':
		lastLetter = random.choice(kend)
	elif nextLetter == 'l':
		lastLetter = random.choice(lend)
	elif nextLetter == 'm':
		lastLetter = random.choice(mend)
	elif nextLetter == 'n':
		lastLetter = random.choice(nend)
	elif nextLetter == 'o':
		lastLetter = random.choice(oend)
	elif nextLetter == 'p':
		lastLetter = random.choice(pend)
	#elif nextLetter == 'q':
		#lastLetter = random.choice(qend)
	elif nextLetter == 'r':
		lastLetter = random.choice(rend)
	elif nextLetter == 's':
		lastLetter = random.choice(send)
	elif nextLetter == 't':
		lastLetter = random.choice(tend)
	elif nextLetter == 'u':
		lastLetter = random.choice(uend)
	elif nextLetter == 'v':
		lastLetter = random.choice(vend)
	elif nextLetter == 'w':
		lastLetter = random.choice(wend)
	elif nextLetter == 'x':
		lastLetter = random.choice(xend)
	elif nextLetter == 'y':
		lastLetter = random.choice(yend)
	elif nextLetter == 'z':
		lastLetter = random.choice(zend)
	#elif nextLetter == 'ou':
		#lastLetter = random.choice(uend)
	else:
		print("An error has occured")
	totalWord.append(lastLetter) #appends the last letter

	randWord = ''.join(map(str,totalWord)) #this joins the word in totalWord together so it can be displayed without spaces or commas.

	return randWord

print(wordGen())
