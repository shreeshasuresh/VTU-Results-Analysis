#######################################################################################
#                                                                                     #
#                     Developed by Shreesha S                                         #
# For enhancements, suggestions, bugs or hugs contact me at shreesha.suresh@gmail.com #
#                                                                                     #
#######################################################################################

import requests, json
from bs4 import BeautifulSoup

import plotly.plotly as py
from plotly.graph_objs import *
import collections

total = []
print "Enter first 5 character of USN: Region Code + College Code + Year"
usn_code = raw_input("example: 1PE13 > ")
# List of branches
branch = ['CS', 'IS', 'EC', 'ME']
print "Wait till we crunch the numbers and get the data for you..."

# Create empty 2-D lists to store the marks of various students for 8 subjects
subject_total_ise = [[],[],[],[],[],[],[],[]]
subject_total_cse = [[],[],[],[],[],[],[],[]]
subject_total_ece = [[],[],[],[],[],[],[],[]]
subject_total_me = [[],[],[],[],[],[],[],[]]

try:
	for branch_code in branch:
		for i in range(1, 200):
			# Append the USN with suitable three digits at the end
			usn = usn_code + branch_code + str(i).zfill(3)

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
				subject = 0
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
						each_string = []
						each_string.append(each.string.strip())
						try: 
							if (count-3) % 5 == 0 and count >= 0 and int(each_string[0]) <= 125:
								subscript = subject % 8
								subject += 1
								if branch_code == 'IS':
									subject_total_ise[subscript].append(int(each_string[0]))
								elif branch_code == 'CS':
									subject_total_cse[subscript].append(int(each_string[0]))
								elif branch_code == 'EC':
									subject_total_ece[subscript].append(int(each_string[0]))
								elif branch_code == 'ME':
									subject_total_me[subscript].append(int(each_string[0]))
						except:
							pass
					
						data_file.write(each.string.strip())
						data_file.write(" ")
					
					# Break from this loop (don't print) if the student has written subjects of Backlog.
					elif each.string == "Semester:" and count > 9:
						break

				total_marks = text[-1].string.strip()
				if int(total_marks) > 300:
					total.append(total_marks)
				data_file.write("\n")
				soup = None
				
			else:
				pass
				
		total.sort()
		counter = collections.Counter(total)
		freq = counter.values()
		value = counter.keys()
		
		frequency_trace = Histogram(
							x = value,
							y = freq,
							name=branch_code
						)
		layout = Layout(
					title='PESIT-BSC 3rd Sem Frequency of Total Marks',
    				xaxis=XAxis(
        				title='Total Marks',
        			),
        			yaxis = YAxis(
       			 		title='No. of Students with same marks',
      		  		)
        		)
		frequency_data = Data([frequency_trace])
		fig = Figure(data=frequency_data, layout=layout)

		unique_url = py.plot(fig, filename = 'PESIT-BSC-3rd-Sem-Marks-Frequency', world_readable=False) 

	average_ise = []
	average_cse = []
	average_ece = []
	average_me = []
	for no_subject in range(0,8):
		average_ise.append(sum(subject_total_ise[no_subject])/len(subject_total_ise[no_subject]))
		average_cse.append(sum(subject_total_cse[no_subject])/len(subject_total_cse[no_subject]))
		average_ece.append(sum(subject_total_ece[no_subject])/len(subject_total_ece[no_subject]))
		average_me.append(sum(subject_total_me[no_subject])/len(subject_total_me[no_subject]))

	total_trace_ise = Scatter(
				x = ['10MAT31','10xx32','10xx33','10xx34','10xx35','10xx36','10xxL37','10xxL38'],
				y = average_ise,
				name='ISE'
			)
	total_trace_cse = Scatter(
				x = ['10MAT31','10xx32','10xx33','10xx34','10xx35','10xx36','10xxL37','10xxL38'],
				y = average_cse,
				name='CSE'
			)	
	total_trace_ece = Scatter(
				x = ['10MAT31','10xx32','10xx33','10xx34','10xx35','10xx36','10xxL37','10xxL38'],
				y = average_ece,
				name='ECE'
			)
	total_trace_me = Scatter(
				x = ['10MAT31','10xx32','10xx33','10xx34','10xx35','10xx36','10xxL37','10xxL38'],
				y = average_me,
				name='MECH'
			)
	layout = Layout(
			title='PESIT-BSC 3rd Semester Average Marks',
    		xaxis=XAxis(
        		title='Subject Codes',
        		),
        	yaxis = YAxis(
        		title='Average Marks',
        		)
        	)
	total_data = Data([total_trace_cse, total_trace_ise, total_trace_ece, total_trace_me])
	fig = Figure(data=total_data, layout=layout)

	unique_url = py.plot(fig, filename = 'PESIT-BSC-3rd-Sem-Average-Marks', world_readable=False)
	
except:
	print "Please enter a valid USN query."
