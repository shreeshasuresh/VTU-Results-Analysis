#######################################################################################
#                                                                                     #
#                     Developed by Shreesha S                                         #
# For enhancements, suggestions, bugs or hugs contact me at shreesha.suresh@gmail.com #
#                                                                                     #
#######################################################################################

import requests, json
from bs4 import BeautifulSoup

total = []
print "Enter first 7 character of USN: region code + college code + year + college code"
usn_code = raw_input("example: 1PE13IS > ")
print "Wait till we crunch the numbers and get the data for you..."

try:
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
				soup = BeautifulSoup(line)
			else:
				continue

		# If USN is valid and the marks-data is properly returned
		if soup != None:
			# We want to ignore the initial 10 strings (count) as it is non-sense!
			count = -10
			# Get the string containg name and usn
			name_usn = soup.b.string.strip()
			name = name_usn.split("(")[0]
			# Write to file name and usn
			data_file.write(usn)
			data_file.write(" ")
			data_file.write(name)

			# Get the strings containing 
			text = soup.find_all('td')
			for each in text:
				count += 1
				# Go straight to the first subject ignoring the rest strings
				if count >= 0 and each.string != "Semester:" and each.string != None:
					if count % 5 == 0 or each.string.strip() == 'Total Marks:':
						data_file.write("\n\t")
					data_file.write(each.string.strip())
					data_file.write(" ")
				# Break from this loop (don't print) if the student has written subjects of Backlog.
				elif each.string == "Semester:" and count > 9:
					break

			""" Get the Total marks and print if it is more than 300...
			... and anything below that means that the total is of ...
			... the backlog subjects which is not what we want """
			total_marks = text[-1].string.strip()
			if total_marks > 300:
				total.append(total_marks)

			data_file.write("\n")
			soup = None
			
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

except:
	print "Please enter a valid USN query."""
