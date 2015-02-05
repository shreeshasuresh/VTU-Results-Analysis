# VTU-Results-Analysis
This is a script to extract the results of any VTU college / course to help you analyse the data. 
The results are read from the [VTU results webpage](http://www.results.vtu.ac.in/vitavi.php) and written to a file _data.txt_.
___
## Steps to run this script:
1. Install Python 2.7 if not installed already
2. Clone this repository
3. In terminal go into the cloned repo: `cd VTU-Results-Analysis`
4. Run the script: `python script.py`
___
## Format of the data written in _data.txt_:
Each subject consists of three columns. First column is the external marks, second is the internal marks and the third column is subject total.
|USN|Subject 1|Subject 2|Subject 3|Subject 4|Subject 5|Subject 6|Subject 7|Subject 8|Total|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|1PE13IS0xx|70 19 89|75 20 95|60 15 75|67 17 84|80 20 100|70 18 88|45 22 67|48 25 73|671|
|....|....|....|....|....|....|....|....|....|....|
___
## Bugs to tackle:
* The marks of uncleared subjects (Backlogs) will be written to the file in place of Total.
* Extract the marks of USNs without hard-coding the initial digit in USN
* Allow extraction of results for various colleges without hard-coding
___
Use the data written in _data.txt_ file to do any analysis on it!
