######################################################################################
#                                                                                    #
#                     Developed by Shreesha S                                        #
# For enhancements suggestions, bugs or hugs contact me at shreesha.suresh@gmail.com #
#                                                                                    #
######################################################################################

import requests

for i in range(1, 130):
	# Append the USN with suitable three digits at the end
	usn = "1PE13IS"+str(i).zfill(3)

	data_file = open('data', 'a')
	# Send USN and SUBMIT as POST Request
	payload = {'rid':usn, 'submit':'SUBMIT'}
	response = requests.post("http://results.vtu.ac.in/vitavi.php", data=payload)
	# Extract the line which contains the results from the HTML response
	for line in response.iter_lines():
		if line[0:3] == '<B>':
			split_words = line.split(">")
		else:
			continue
		
	count = 0
	if len(split_words) != 0:
		# Write the USN to the file if HTML line with results is not empty
		data_file.write(usn)
		data_file.write(" ")
		for tags in split_words:
			# Extract the marks ignoring the HTML tags
			word = split_words[count].split("<")[0]
			if count % 2 == 0 and word != '' and len(word) <= 3:
				data_file.write(word)
				data_file.write(" ")
			count += 1

		data_file.write(split_words[-6].split(" &")[0].split(" ")[1])
		data_file.write("\n")
		data_file = open('data', 'r')
		data_file.read()
		# Clear the previous list elements
		split_words = []
	else:
		pass
