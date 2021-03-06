#!/usr/env python

# Hi!  Wikichomp does 3 things: grabs articles from wikipedia, decoheres an acronym and recurses with user directions
# wikichomp should only do 1 thing:  grab articles and place the dictarray in the acro_dicts folder
# decoherence should be it's own script
# and recursor too
# currently implemented in python2.7 

import re
import sys
import random
import urllib2
import string
import json
import pdb

#linkable words that are part of wikipedia boilerplate
wiki_words_reserved = ['isbn','random article','help','issn','related changes','recent changes','info','all articles with unsourced statements','Community portal','Main page','special pages','Removed','Cite','Disclaimers','upload file','about wikipedia','talk page','categories','featured content']

#TODO: develop a kickass regex (or a bloom filter) which encompasses many variations of reserved words!
#

def disambiguouizer(ambiguous_wiki, ambiguous_term):
	#in the event of an amiguous term, the disambiguouizer lets user select the proper meaning
	refertochomp = ambiguous_wiki.find('may refer to') + 18
	endchomp = ambiguous_wiki.find("disambigbox") - 11
	disambuslice = re.findall('a href=".+">.+<.+>, .+</li>\n', ambiguous_wiki[refertochomp:endchomp])
	disambuchoices =[]
	#print endchomp
	for each in disambuslice:
		targt = each.split('"')[1]
		descr = each.split(',')[1].split('<')[0]
		title = each.split('"')[3]
		disambuchoices.append([title, descr,targt])
	print ambiguous_term + " may refer to;\n"
	selection = 0
	for each in disambuchoices:
		print str(selection) + ". " + each[0] + ", " + each[1]
		selection+= 1
	userchoice = -1
	while 0 >  userchoice or userchoice > selection:
		userchoice = int(input('you choose(0-' + str(selection) + '): \t'))
	ambiguous_term = disambuchoices[userchoice][2].split('/')[-1]
	acronymizer(ambiguous_term)

def acronymizer(wikitarget):
	if '(' in wikitarget:
		properly_capped = wikitarget.split('(')[0].replace(' ', '_').title() \
									+"("+ wikitarget.split('(')[1]
		wikitarget = wikitarget.split('(')[0]
	else:
		properly_capped = wikitarget.replace(' ', '_').title()
	properly_capped = properly_capped.replace('&','%26')
	print "http://en.wikipedia.org/wiki/" + properly_capped + "\n\n"
	req = urllib2.Request("http://en.wikipedia.org/wiki/" + properly_capped, \
		              headers={'User-Agent': 'Mozilla/5.0 (Fuck You Wikipedia; Me; emdash)'})
	wiki_dump = urllib2.urlopen(req).read().lower()
	if wiki_dump.count('isambiguation') > 10:
		#10 seems to be more instances of 'disambiguous' references than non disambiarticales contain
		disambiguouizer(wiki_dump, wikitarget)
	relevance_regex = re.compile('<a href="/wiki/.*?" title=".*?">.*?</a>')
	relephants = re.findall(relevance_regex,wiki_dump)

	#construct vocabulary which contains lists of relevant terms for every letter of the acronymed word
	vocabulary = []
	for each in relephants:
		vocabulary.append(re.sub(".*>","",each[:-4])) 
	for bang in range(0,vocabulary.count('')):
		vocabulary.remove('')
	vocab = sorted(vocabulary, key=str.lower)

	#form a dictionary from vocabulary
	acro_term = wikitarget.lower().translate(string.maketrans("",""), string.punctuation) #got from http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
	acronym_dict = []
	for element in acro_term:
		if element == '_' or element == ' ':
			acronym_dict.append('')
			continue
		acronym_equiv = []
		for each in vocab:
			if each[0] == element:
				acronym_equiv.append(each)
		acronym_dict.append(acronym_equiv)


	for element in wiki_words_reserved:
		for letter_dict in acronym_dict:
			while element in letter_dict:
				letter_dict.remove(element)
	for tick in range(len(acronym_dict)):
	    if acronym_dict[tick] == []:
		acronym_dict[tick].append(acro_term[tick])
    
	print acro_term + " acronymized:"
	acro_records = open("acro_dicts/" + acro_term, 'w')
	acro_records.write(json.dumps(acronym_dict))
	acro_records.close()

	running_acronym = []
	selection = 0
	# now generate a random acronym from the dictionary
	# && recursify
	for each in acronym_dict:
		if each in ['','.']:
			print each
		else:
			running_acronym.append(random.choice(each))
			print str(selection) + ".\t" + running_acronym[-1][0].title() + " \t" + running_acronym[-1].capitalize()
			selection+= 1
	userchoice = -1
	print "\n" + acro_term + " acronymized!"
	while 0 >  userchoice or userchoice > selection:
		userchoice = int(input('you choose(0-' + str(selection-1) + '): \t'))
	term = running_acronym[userchoice]
	#for each in acronym_dict:
	#	if each == '':
	#		print
	#	else:
	#		print random.choice(each)
	acronymizer(term)


if len(sys.argv) != 2:
	term = raw_input("\n\n\nwhat do you want to make an acronym for? ")
else:
	term = sys.argv[1]
acronymizer(term)
