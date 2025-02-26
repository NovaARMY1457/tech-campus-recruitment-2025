Solutions Considered
I looked at a few ways to solve this:

Regex Matching: Use patterns to find dates. Flexible but too complex for this.
Line-by-Line Check: Look at each line and grab ones starting with the date. Simple and fast.
Chunk Reading: Read the file in big pieces. Good for huge files but trickier to set up.
Database Query: Use a database to filter logs. Great for big data, but overkill here.

Final Solution Summary
I picked the Line-by-Line Check because it’s easy, quick, and works well since the logs start with dates. No fancy tools needed—just straightforward code.

Steps to Run
Setup: Make sure Python is on your computer. Have a log file (e.g., logs_2024.log) with lines starting with dates like 2024-02-25.
Save: Put the code in a file called extract_logs.py.
Open Terminal: Go to the folder with the file (e.g., cd your/folder/path).
Run: Type python extract_logs.py 2024-02-25 to get logs for that date.
Check: Look in the output folder for a file like output_2024-02-25.txt with your logs.
