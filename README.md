# VTU-Results-Analysis
This is a script to extract the results of any VTU college / branch to help you analyse the data. 
The results are read from the [VTU results webpage](http://www.results.vtu.ac.in/vitavi.php) and written to a file _data.txt_.
___
## Steps to run this script:
1. Install Python 2.7 if not installed already
2. Clone this repository
3. In terminal go into the cloned repo: `cd VTU-Results-Analysis`
4. Run the script: `python script.py`.

___
## Format of the data written in _data.txt_:

```
USN Student_Name
	Subject_Name External Internal Total Pass/Fail
	...
	Total Marks Marks
...
```

Example:

```
1PE13IS125 FOO BAR 
	Engineering Mathematics-III (10MAT31) 40 15 55 P 
	Electronic Circuits (10CS32) 50 15 65 P 
	Logic Design (10CS33) 69 16 85 P 
	Discrete Mathematical Structures (10CS34) 40 17 57 P 
	Data Structures with C (10CS35) 45 15 60 P 
	Object Oriented Programming with C++ (10CS36) 45 24 69 P 
	Data Structures with C/C++ Lab (10CSL37) 49 23 72 P 
	Electronic Circuits & Logic Design Lab (10CSL38) 42 22 64 P 
	Total Marks: 527 
```

___
## Bugs to tackle / Enhancements:
* Total not calculated for those students who have active backlogs.
* Provide college-wise / subject-wise analysis.

___
Use the data written in _data.txt_ file to do any analysis on it! For suggestions or to report bugs contact me at shreesha.suresh@gmail.com
