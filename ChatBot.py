import json
import nltk

rev_idx = {}
visited = {}
#freq = {}
id_twt = {}
has_reply = {}

def jaqq(query,taggedline):# query ,taggedline are  list of nouns 
 #simlimit=0.001 #return true if query and taggedline more  similar than this threshold
 inter=0
 union=len(squery)+len(taggedline)
 for match in query:
		if match in taggedline:
			inter=inter+1
 #print query,union,inter
 return (inter/ float(un))


def intersect(p1, p2):
	p1 = sorted(p1, key=int)
	p2 = sorted(p2, key=int)
	len1 = len(p1)
	len2 = len(p2)
	ans = []
	i=0
	j=0
	while (i != len1) and (j != len2):
		if(p1[i] == p2[j]):
			ans.append(p1[i])
			i = i + 1
			j = j + 1
		elif long(p1[i]) < long(p2[j]):
			i = i + 1
		else:
			j = j + 1
	return ans

def search(tweet_id):
	try:
		#print " ".join((j[id_twt[tweet_id]]["Data_Text"].split(" "))[1:])
		txt = j[id_twt[tweet_id]]["Data_Text"]
		fin = []
		txt = txt.split(" ")
		#print txt
		for x in txt:
			if (x[0] == "@") or (x[0] == "#"):
				pass
			else:
				fin.append(x)
		print " ".join(fin)	
	except:
		print "Error in printing tweed " + tweet_id
		pass
	

def sort_by_freq(terms):
	d = {}
	for i in terms:
		d[str(i)] = len(rev_idx[str(i)])
	return sorted(d, key=d.get) 

def multi_Intersect(terms):
	result = []
	if terms == []:
		return result
	else: 
		terms = sort_by_freq(terms)
		result = sorted(rev_idx[terms[0]], key=int)
		terms = terms[1:]
		while (terms != []) and (result != []):
			result = intersect(result, sorted(rev_idx[terms[0]], key=int))
			terms = terms[1:]
		return result

################################--MAIN PROGRAM--##########################################

print "Initializing..."
	
f = open('stopwords.txt')

stop_list = []

for line in f:
	stop_list.append(line.split("\n")[0])

f.close()

with open('tweetCollection.json', 'r') as myfile:
	data = myfile.read()

t = {}
j = json.loads(data)

for i in range(len(j)):
	try:
		t[str(j[i]["Data_IdStr"])] = []				
		visited[str(j[i]["Data_IdStr"])] = "0"
		id_twt[str(j[i]["Data_IdStr"])] = i
		if(str(j[i]["Data_InReplyToStatusIdStr"]) != "None"):
			try:
				if str(j[i]["Data_InReplyToStatusIdStr"]) in has_reply: 
					has_reply[str(j[i]["Data_InReplyToStatusIdStr"])].append(str(j[i]["Data_IdStr"]))
				else:
					has_reply[str(j[i]["Data_InReplyToStatusIdStr"])] = []
					has_reply[str(j[i]["Data_InReplyToStatusIdStr"])].append(str(j[i]["Data_IdStr"]))
			except:
				pass
	except:
		print "Error in 1" + str(i)

for i in range(len(j)):
	try:
		if visited[str(j[i]["Data_IdStr"])] == "0" and str(j[i]["Data_Lang"]) == "en": 
			visited[str(j[i]["Data_IdStr"])] = "1"

			c = 0
			tex = ""
			try:
				tex = str(j[i]["Data_Text"])
				c = 1
			except:
				c = 0

			if c == 1:
				tex = tex.split(" ")
				for w in tex:
					if str(w) not in stop_list:
						if str(w) in rev_idx:
							rev_idx[str(w).lower()].append(str(j[i]["Data_IdStr"]))
							#freq[str(w).lower()] = freq[str(w).lower()] + 1
						else:
							rev_idx[str(w).lower()] = []
							rev_idx[str(w).lower()].append(str(j[i]["Data_IdStr"]))
							#freq[str(w).lower()] = 1


	except:	
		print "Error in 2 " + str(i)
	
'''
h = open('parent_list.txt','w')
for wd in rev_idx:
	if wd not in stop_list:
		for ids in rev_idx[wd]:
			if ids in has_reply:
				h.write(str(wd) + "\n")
				break	
h.close()
'''

#print len(rev_idx)

print "Hi I am TBot. Ask me anything !"
#print len(has_reply)

query = raw_input('Q : ')
query = query.lower()
while query != "q":
	idx_list = []
	'''
	tagged = nltk.pos_tag(query.split())
	nouns = [word for word,pos in tagged if pos=="NP" or pos=="NNP" or pos=="NN" or pos=="NNS"]
	idx_list = []
	for word in nouns:
		if (word.lower()) in rev_idx:
			idx_list.append(word.lower())
	'''

	qs = query.split(" ")
	for word in qs:
		if (word.lower()) not in stop_list:
			if (word.lower()) in rev_idx:
				idx_list.append(word.lower())

	'''
	for x in idx_list:
		print x.upper()
		res3 = multi_Intersect([str(x.lower())])
		print res3
		for x2 in res3:
			print search(str(x2))
	
	#res2 = multi_Intersect(idx_list)  #This uses intersection

	'''
	res2 = []
	for y in idx_list:
		for z in rev_idx[y]:
			res2.append(z)

	#print res2
	res_f = []
	for i in res2:
		if i in has_reply:
			res_f.append(i)
	#print "\n"
	#rint "FINAL RESULT"
	#print len(res_f)
	#print res_f
	for p in res_f:
		#search(str(p))
		#print "HAS REPLY"
		search(has_reply[str(p)][0])
		break
	
	query = raw_input('Q : ')
	query = query.lower()









