# attendance_Calculator_for_teams
Attendance calculator for teams that gets and calculates attendance depending upon the threshold

Files Prep:
	You require 2 files to calculate the attendance for a Teams meeting.
	# Attendance Calculation – Excel File
		The above file should include the details of all the students or users who are attending or who are scheduled to attend the meeting.
		This file can be reused and updated if the names of the students or users, match with the csv date files of multiple meetings.
		Example Filename: attendancecalculation.xlsx
 	https://user-images.githubusercontent.com/40388943/116095104-b9bef600-a6c5-11eb-8985-78939e4ead06.png
	# DD-MM-YYYY – CSV File
		The above date file can be obtained from a Teams meeting by downloading the attendance list. 
		The above file contains the details of the students or users who joined and left the meeting along with the respective timestamps.
		Example Filename: 11-09-2020.csv
 

**NOTE:**
	**The names in both the files should match and it is preferable that the names in both the files have the same case (UPPER/LOWER).**
	 <a href="#" class="text-inherit">Should save the csv file in UTF-8 Format, otherwise the application won’t work</a>
	 
	While saving or downloading the csv file from teams, 
	click on Tools -> Web Options -> Encoding and use the dropdown to save this document as Unicode (UTF-8). 

Running the Application:

 	1. Enter the start time and end time of a class meeting as per the specified format.
 	2. Enter the threshold percentage value (0-100).
        (A value of 0 indicates that a student or user need not even attend the meeting to be awarded attendance 
	whereas a value of 100 indicates that the student or user should be present throughout the meeting
	exactly from the start time till the end time. 
	A value of 75 – 90 is recommended.)
 	3. Upload the attendance calculation file and the date csv file in the format discussed earlier. 
 	(The final calculated attendance results will be stored in the attendance calculation excel file.)
 	4. After uploading, verify whether the path displayed is the correct path of the file.
 	5. After verifying the path, click the Submit button to calculate the meeting attendance. 
 	(You will be also shown a message in a command window once the process is completed.)
 	7.  The results can now be viewed in the attendance calculation file.
 
NOTE:
	**Please verify whether the entered start time and end time along with the time of day (AM/PM) correspond with that of the data in the date csv file obtained from Teams.
