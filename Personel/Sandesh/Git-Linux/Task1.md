1. Process Defination : Any running program or a command given to a Linux system is called a process or An instance of a running program 				 is called a process.


2. Process Proerties : A process in a multithreaded system is the changeable entity.
			It must be considered as an execution frame. It has traditional process attributes, such as:
			Process ID, process group ID, user ID, and group ID, Environment, parent process ID, Working directory


3. Process Types : There are 3 Type of Process in Linux/Unix are following

    		    1. Foreground processes (also referred to as interactive processes) – these are initialized and controlled through a  			       terminal session. In other words, there has to be a user connected to the system to start such processes; they 			       haven’t started automatically as part of the system functions/services.
    
                   2. Background processes (also referred to as non-interactive/automatic processes) – are processes not connected to a 			      terminal; they don’t expect any user input.
    
                   3. Daemons processes These are special types of background processes that start at system startup and keep running 			      forever as a service; they don’t die. They are started as system tasks (run as services), spontaneously. However, 			      they can be controlled by a user via the init process.
    

4. Ctrl C : terminates the currently-running program.

5. Ctrl Z : running program will be stopped and you will be returned to the command prompt.

6. Ctrl D : closes the terminal window or end terminal line input. 

7. Ps : The ps (i.e., process status) command is used to provide information about the currently running processes, including their       	process identification numbers (PIDs). 

8. bg : The bg (i.e., background ) put the recently suspended process in the background.

9. fg : The fg (i.e., foreground )  put the recently suspended process in the foreground.
    

10. clear :clear command used to clear terminal screen.


11. History: show you all of the last commands that have been recently used

12. kill: which is used to terminate processes manually. kill command sends a signal to a process which terminates the process.

13. Top: it provides a dynamic real-time view of the running system. Usually, this command shows the summary information of the system and 	  the list of processes or threads which are currently managed by the Linux Kernel
