Process Defination : In computing, a process is the instance of a computer program that is being executed by one or many threads. It contains the program code and its activity. Depending on the operating system (OS), a process may be made up of multiple threads of execution that execute instructions concurrently.


Process Proerties :A process in a multithreaded system is the changeable entity.
It must be considered as an execution frame. It has traditional process attributes, such as:
Process ID, process group ID, user ID, and group ID
Environment
Working directory


Process Types : Background process ,Forehead Process 

Ctr c : terminate or kill the current foreground process by request most process 

Ctr Z :Ctrl+Z – suspend the current foreground process. This sends the SIGTSTP signal to the process. You can get the process back to the foreground later using the fg process_name (or %bgprocess_number like %1, %2 and so on) command. Ctrl+C – interrupt the current foreground process, by sending the SIGINT signal to it

Ctrl D :stop all existing process 


Ps : show all process that going on.

bg :The bg command is part of Linux/Unix shell job control. The command may be available as both internal and external command. It resumes execution of a suspended process as if they had been started with &. Use bg command to restart a stopped background process.02-Feb-2014

fg :The fg command switches a job running in the background into the foreground. The bg command restarts a suspended job, and runs it in the background. If no job number is specified, then the fg or bg command acts upon the currently running job.


clear : clear terminal window (to look clear ).


History: show all previous commands that user used.

kill: this command use for terminate the on going process 


Top:It provides a dynamic real-time view of the running system. Usually, this command shows the summary information of the system and the list of processes or threads which are currently managed by the Linux Kernel.
