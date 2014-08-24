import json	

f = open('tweetdb.txt')
count = 0
res_list = []
for line in f:
	mydata = {}
	try:
		j = json.loads(line)
		
		try:
			mydata["Timestamp"] = j["Timestamp"]
		except:
			mydata["Timestamp"] = ""
			pass

		try:
			d = json.loads(j["Data"])
			#mydata["Data"] = {}
			'''
			try:
				mydata["Data"]["Coordinates"] = d["Coordinates"]
			except:
				mydata["Data"]["Coordinates"] = ""
				pass
			'''

			try:
				mydata["Data_InReplyToScreenName"] = d["InReplyToScreenName"]
			except:
				mydata["Data_InReplyToScreenName"] = ""
				pass

			try:
				#u = json.loads(d["User"])
				u = d["User"]
				#print u.keys()
				#mydata["Data"]["User"] = {}
				try:
					mydata["Data_User_Name"] = u["Name"]
				except:
					mydata["Data_User_Name"] = ""
					pass

				try:
					mydata["Data_User_IdStr"] = u["IdStr"]
				except:
					mydata["Data_User_IdStr"] = ""
					pass

				try:
					mydata["Data_User_ScreenName"] = u["ScreenName"]
				except:
					mydata["Data_User_ScreenName"] = ""
 					pass

			except:
				pass

			try:
				mydata["Data_InReplyToStatusIdStr"] = d["InReplyToStatusIdStr"]
			except:
				mydata["Data_InReplyToStatusIdStr"] = ""
				pass

			try:
				mydata["Data_Lang"] = d["Lang"]
			except:
				mydata["Data_Lang"] = ""
				pass

			try:
				mydata["Data_IdStr"] = d["IdStr"]
			except:
				mydata["Data_IdStr"] = ""
				pass

			try:
				mydata["Data_InReplyToUserIdStr"] = d["InReplyToUserIdStr"]
			except:
				mydata["Data_InReplyToUserIdStr"] = ""
				pass

			try:
				mydata["Data_Text"] = d["Text"]
			except:
				mydata["Data_Text"] = ""
				pass
		except:
			pass
		
		res_list.append(mydata)
		
		'''
		# This is for debugging purposes
		count = count + 1
		if count == 5:
			break
		'''

	except:
		pass

#print json.dumps(res_list, ensure_ascii=False)
f.close()

with open('tweetCollection.json', 'w') as outfile:
	json.dump(res_list, outfile)
