# 0x05. Processes and signals

## Learning Objectives


- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Tasks

_**0. What is my PID**_  
Write a Bash script that displays its own PID.

_**1. List your processes**_  
Write a Bash script that displays a list of currently running processes.

_**2. Show your Bash PID**_  
Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.

_**3. Show your Bash PID made easy**_  
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

_**4. To infinity and beyond**_  
Write a Bash script that displays `To infinity and beyond` indefinitely.

_**5. Kill me now**_
We killed our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.

Write a Bash script that kills `4-to_infinity_and_beyond` process.

_**6. Kill me now made easy**_  
Write a Bash script that kills `4-to_infinity_and_beyond` process.

_**7. Highlander**_  
Write a Bash script that displays:

- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a `SIGTERM` signal

Make a copy of your `6-kill_me_now_made_easy` script, name it `67-kill_me_now_made_easy`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

_**8. Beheaded process**_  
Write a Bash script that kills the process `7-highlander`.
