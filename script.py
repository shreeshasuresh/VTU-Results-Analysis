######################################################################################
#                                                                                    #
#                     Developed by Shreesha S                                        #
# For enhancements suggestions, bugs or hugs contact me at shreesha.suresh@gmail.com #
#                                                                                    #
######################################################################################

import requests

for i in range(10, 100):
	usn = "1PE13IS0"+str(i)
	data_file = open('data', 'a')
	data_file.write(usn)
	data_file.write(" ")
	payload = {'rid':usn, 'submit':'SUBMIT'}
	response = requests.post("http://results.vtu.ac.in/vitavi.php", data=payload)
	for line in response.iter_lines():
		if line[0:3] == '<B>':
			split_words = line.split(">")
			
	count = 0
	try:
		for i in split_words:
			count += 1
			word = split_words[count].split("<")[0]
			if count % 2 == 0 and word != '' and len(word) <= 3:
				data_file.write(word)
				data_file.write(" ")
	except:
		pass
	data_file.write(split_words[-6].split(" &")[0].split(" ")[1])
	data_file.write("\n")
	data_file = open('data', 'r')
	data_file.read()
