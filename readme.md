Step 1: Automate the Script Execution

   Windows Task Scheduler:
   Open Task Scheduler.
   Create a new task and set the script to run every 10 minutes.
       
        
 
 Linux Cron Job:

Open the crontab editor:
crontab -e

Add the following line:

*/10 * * * * python3 /path/to/your_script.py
