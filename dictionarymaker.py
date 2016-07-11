import random
import sys

def randomWordGen(arg1 = 5, arg2 = 'default'):
	totalLength = arg1
	excludeInput = "Default"
	excludeList = []
	if arg2.lower() == 'exclude':
		print("Input the letters you want to exclude here. Press enter without anything to proceed.")
		while excludeInput != '':
			excludeInput = input(' ')
			excludeList.append(excludeInput)
			if excludeInput == '':
				excludeList.remove('')
	totalWord = []
	allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z'] #all letters is used to start off the whole thing. Q has been removed.
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
	m = ['a','e','i','j','o','u','y']
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
	lend = ['a','b','c','d','e','f','g','i','l','m','n','o','p','s','t','u','v','x','y','z']
	mend = ['a','b','e','f','i','k','m','n','o','p','s','t','u','y','z']
	nend = ['a','b','c','d','e','f','g','h','i','k','n','o','p','s','t','u','v','x','y','z']
	oend = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
	pend = ['a','e','f','h','i','o','p','s','t','u','y','z']
	# see the above Q reminder.
	rend = ['a','b','c','d','e','g','i','k','m','n','o','p','r','s','t','u','v','x','y','z'] #Q has been removed from this list.
	send = ['a','b','c','e','g','h','i','k','m','o','p','t','u','y']
	tend = ['a','e','h','i','o','s','t','u','y']
	uend = ['a','b','c','d','e','f','g','h','k','l','m','n','p','r','s','t','v','w','x','z']
	vend = ['a','e','g','i','k','o','s','t','u','y','z']
	wend = ['a','e','i','o','u','y']
	xend = ['a','e','i','o','u','x','y']
	yend = ['a','b','c','d','e','g','i','k','o','p','s','t','u','v','x','z']
	zend = ['a','e','i','k','o','p','t','u','y']

	allLetters_exclude = [ex for ex in a if ex not in (excludeList)]
	a_exclude = [ex for ex in a if ex not in (excludeList)]
	b_exclude = [ex for ex in b if ex not in (excludeList)]
	c_exclude = [ex for ex in c if ex not in (excludeList)]
	d_exclude = [ex for ex in d if ex not in (excludeList)]
	e_exclude = [ex for ex in e if ex not in (excludeList)]
	f_exclude = [ex for ex in f if ex not in (excludeList)]
	g_exclude = [ex for ex in g if ex not in (excludeList)]
	h_exclude = [ex for ex in h if ex not in (excludeList)]
	i_exclude = [ex for ex in i if ex not in (excludeList)]
	j_exclude = [ex for ex in j if ex not in (excludeList)]
	k_exclude = [ex for ex in k if ex not in (excludeList)]
	l_exclude = [ex for ex in l if ex not in (excludeList)]
	m_exclude = [ex for ex in m if ex not in (excludeList)]
	n_exclude = [ex for ex in n if ex not in (excludeList)]
	o_exclude = [ex for ex in o if ex not in (excludeList)]
	p_exclude = [ex for ex in p if ex not in (excludeList)]
	r_exclude = [ex for ex in r if ex not in (excludeList)]
	s_exclude = [ex for ex in s if ex not in (excludeList)]
	t_exclude = [ex for ex in t if ex not in (excludeList)]
	u_exclude = [ex for ex in u if ex not in (excludeList)]
	v_exclude = [ex for ex in v if ex not in (excludeList)]
	w_exclude = [ex for ex in w if ex not in (excludeList)]
	x_exclude = [ex for ex in x if ex not in (excludeList)]
	y_exclude = [ex for ex in y if ex not in (excludeList)]
	z_exclude = [ex for ex in z if ex not in (excludeList)]
	aend_exclude = [ex for ex in aend if ex not in (excludeList)]
	bend_exclude = [ex for ex in bend if ex not in (excludeList)]
	cend_exclude = [ex for ex in cend if ex not in (excludeList)]
	dend_exclude = [ex for ex in dend if ex not in (excludeList)]
	eend_exclude = [ex for ex in eend if ex not in (excludeList)]
	fend_exclude = [ex for ex in fend if ex not in (excludeList)]
	gend_exclude = [ex for ex in gend if ex not in (excludeList)]
	hend_exclude = [ex for ex in hend if ex not in (excludeList)]
	iend_exclude = [ex for ex in iend if ex not in (excludeList)]
	jend_exclude = [ex for ex in jend if ex not in (excludeList)]
	kend_exclude = [ex for ex in kend if ex not in (excludeList)]
	lend_exclude = [ex for ex in lend if ex not in (excludeList)]
	mend_exclude = [ex for ex in mend if ex not in (excludeList)]
	nend_exclude = [ex for ex in nend if ex not in (excludeList)]
	oend_exclude = [ex for ex in oend if ex not in (excludeList)]
	pend_exclude = [ex for ex in pend if ex not in (excludeList)]
	rend_exclude = [ex for ex in rend if ex not in (excludeList)]
	send_exclude = [ex for ex in send if ex not in (excludeList)]
	tend_exclude = [ex for ex in tend if ex not in (excludeList)]
	uend_exclude = [ex for ex in uend if ex not in (excludeList)]
	vend_exclude = [ex for ex in vend if ex not in (excludeList)]
	wend_exclude = [ex for ex in wend if ex not in (excludeList)]
	xend_exclude = [ex for ex in xend if ex not in (excludeList)]
	yend_exclude = [ex for ex in yend if ex not in (excludeList)]
	zend_exclude = [ex for ex in zend if ex not in (excludeList)]

	if arg2.lower() == 'exclude':
		nextLetter = random.choice(allLetters_exclude)
	else:
		nextLetter = random.choice(allLetters)
	while len(totalWord) < int(totalLength) - 1: #must be - 1 for the end letter function down below.
		if arg2.lower() == 'exclude':
			if nextLetter == 'a':
				nextLetter = random.choice(a_exclude)
			elif nextLetter == 'b':
				nextLetter = random.choice(b_exclude)
			elif nextLetter == 'c':
				nextLetter = random.choice(c_exclude)
			elif nextLetter == 'd':
				nextLetter = random.choice(d_exclude)
			elif nextLetter == 'e':
				nextLetter = random.choice(e_exclude)
			elif nextLetter == 'f':
				nextLetter = random.choice(f_exclude)
			elif nextLetter == 'g':
				nextLetter = random.choice(g_exclude)
			elif nextLetter == 'h':
				nextLetter = random.choice(h_exclude)
			elif nextLetter == 'i':
				nextLetter = random.choice(i_exclude)
			elif nextLetter == 'j':
				nextLetter = random.choice(j_exclude)
			elif nextLetter == 'k':
				nextLetter = random.choice(k_exclude)
			elif nextLetter == 'l':
				nextLetter = random.choice(l_exclude)
			elif nextLetter == 'm':
				nextLetter = random.choice(m_exclude)
			elif nextLetter == 'n':
				nextLetter = random.choice(n_exclude)
			elif nextLetter == 'o':
				nextLetter = random.choice(o_exclude)
			elif nextLetter == 'p':
				nextLetter = random.choice(p_exclude)
			#elif nextLetter == 'q':
				#nextLetter = random.choice(q_exclude)
			elif nextLetter == 'r':
				nextLetter = random.choice(r_exclude)
			elif nextLetter == 's':
				nextLetter = random.choice(s_exclude)
			elif nextLetter == 't':
				nextLetter = random.choice(t_exclude)
			elif nextLetter == 'u':
				nextLetter = random.choice(u_exclude)
			elif nextLetter == 'v':
				nextLetter = random.choice(v_exclude)
			elif nextLetter == 'w':
				nextLetter = random.choice(w_exclude)
			elif nextLetter == 'x':
				nextLetter = random.choice(x_exclude)
			elif nextLetter == 'y':
				nextLetter = random.choice(y_exclude)
			elif nextLetter == 'z':
				nextLetter = random.choice(z_exclude)
			#elif nextLetter == 'ou':
				#nextLetter = random.choice(u_exclude)
			else:
				print("An error has occured")
			totalWord.append(nextLetter)
			
		else:
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
			totalWord.append(nextLetter)
			
	if arg2.lower() == 'exclude':	
		if nextLetter == 'a':
			lastLetter = random.choice(aend_exclude)
		elif nextLetter == 'b':
			lastLetter = random.choice(bend_exclude)
		elif nextLetter == 'c':
			lastLetter = random.choice(cend_exclude)
		elif nextLetter == 'd':
			lastLetter = random.choice(dend_exclude)
		elif nextLetter == 'e':
			lastLetter = random.choice(eend_exclude)
		elif nextLetter == 'f':
			lastLetter = random.choice(fend_exclude)
		elif nextLetter == 'g':
			lastLetter = random.choice(gend_exclude)
		elif nextLetter == 'h':
			lastLetter = random.choice(hend_exclude)
		elif nextLetter == 'i':
			lastLetter = random.choice(iend_exclude)
		elif nextLetter == 'j':
			lastLetter = random.choice(jend_exclude)
		elif nextLetter == 'k':
			lastLetter = random.choice(kend_exclude)
		elif nextLetter == 'l':
			lastLetter = random.choice(lend_exclude)
		elif nextLetter == 'm':
			lastLetter = random.choice(mend_exclude)
		elif nextLetter == 'n':
			lastLetter = random.choice(nend_exclude)
		elif nextLetter == 'o':
			lastLetter = random.choice(oend_exclude)
		elif nextLetter == 'p':
			lastLetter = random.choice(pend_exclude)
		#elif nextLetter == 'q':
			#lastLetter = random.choice(qend_exclude)
		elif nextLetter == 'r':
			lastLetter = random.choice(rend_exclude)
		elif nextLetter == 's':
			lastLetter = random.choice(send_exclude)
		elif nextLetter == 't':
			lastLetter = random.choice(tend_exclude)
		elif nextLetter == 'u':
			lastLetter = random.choice(uend_exclude)
		elif nextLetter == 'v':
			lastLetter = random.choice(vend_exclude)
		elif nextLetter == 'w':
			lastLetter = random.choice(wend_exclude)
		elif nextLetter == 'x':
			lastLetter = random.choice(xend_exclude)
		elif nextLetter == 'y':
			lastLetter = random.choice(yend_exclude)
		elif nextLetter == 'z':
			lastLetter = random.choice(zend_exclude)
		#elif nextLetter == 'ou':
			#lastLetter = random.choice(uend_exclude)
		else:
			print("An error has occured")
		totalWord.append(lastLetter)
	else:
		print("NONEXCLUDE MODE")
		wait = input("PRESS ENTER TO CONTINUE.")
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
		totalWord.append(lastLetter)
	
	randWord = ''.join(map(str,totalWord))
	return randWord

if __name__ == '__main__':
	try:
		print(randomWordGen(sys.argv[1], sys.argv[2]))
	except IndexError:
		print(randomWordGen(5,'Default'))