######################################################################################
#                                                                                    #
#                     Developed by Shreesha S                                        #
# For enhancements suggestions, bugs or hugs contact me at shreesha.suresh@gmail.com #
#                                                                                    #
######################################################################################

import requests, json

total = []
print "Enter first 7 character of USN: region code + college code + year + college code"
usn_code = raw_input("example: 1PE13IS >")

for i in range(1, 200):
	# Append the USN with suitable three digits at the end
	usn = usn_code + str(i).zfill(3)

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

		total_marks = split_words[-6].split(" &")[0].split(" ")[1]
		if len(total_marks) == 3:
			total.append(total_marks)
		data_file.write(total_marks)
		data_file.write("\n")
		data_file = open('data', 'r')
		data_file.read()
		# Clear the previous list elements
		split_words = []
	else:
		pass

mark_slab = { 'percent<50%': 0,
			'50%<=percent<60%': 0,
			'60%<=percent<70%': 0,
			'70%<=percent<80%': 0 ,
			'80%<=percent<90%': 0,
			'percent>90%': 0 }

for marks in total:
	# Number of students whose total marks is less 50%
	if int(marks) <= 450:
		mark_slab['percent<50%'] += 1
	# Number of students whose total marks is less than 60% but more than 50%
	elif int(marks) > 450 and int(marks) < 535:
		mark_slab['50%<=percent<60%'] += 1
	# Number of students whose total marks is less than 70% but more than 60%
	elif int(marks) >= 535 and int(marks) < 625:
		mark_slab['60%<=percent<70%'] += 1
	# Number of students whose total marks is less than 80% but more than 70%
	elif int(marks) >= 625 and int(marks) < 720:
		mark_slab['70%<=percent<80%'] += 1
	# Number of students whose total marks is less than 90% but more than 80%
	elif int(marks) >= 720 and int(marks) < 810:
		mark_slab['80%<=percent<90%'] += 1
	# Number of students whose total marks is more than 90%
	else:
		mark_slab['percent>90%'] += 1

# Print the number of students dictionary count in JSON format.
print json.dumps(mark_slab, indent=4)
