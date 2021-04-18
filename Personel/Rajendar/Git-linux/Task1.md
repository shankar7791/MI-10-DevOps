Process definition : a process is the instance of a computer program that is being executed by one or many threads.
Process Properties :. Process ID

When a process is created, a unique id is assigned to the process which is used for unique identification of the process in the system.
2. Program counter

A program counter stores the address of the last instruction of the process on which the process was suspended. The CPU uses this address when the execution of this process is resumed.
3. Process State

The Process, from its creation to the completion, goes through various states which are new, ready, running and waiting. We will discuss about them later in detail.
4. Priority

Every process has its own priority. The process with the highest priority among the processes gets the CPU first. This is also stored on the process control block.
5. General Purpose Registers

Every process has its own set of registers which are used to hold the data which is generated during the execution of the process.
6. List of open files

During the Execution, Every process uses some files which need to be present in the main memory. OS also maintains a list of open files in the PCB.
7. List of open devices

OS also maintain the list of all open devices which are used during the execution of the process.

Process types : 1) CPU Bound Processes 2) I/O Bound Processes. 
1)Independent Processes 2)Cooperative Processe 
1) Single Level Thread.

ctrl c : Interrupt (kill) the current foreground process running in in the terminal.

ctrl z : The ctrl-z sequence suspends the current process.

ctrl d : The ctrl-d sequence closes the terminal window or end terminal line input.

ps : ps command is used to list the currently running processes and their PIDs along with some other information depends on different options.

fg : he fg command switches a job running in the background into the foreground.

bg : It resumes execution of a suspended process as if they had been started with &. Use bg command to restart a stopped background process.

clear : The clear command is used to remove all previous commands and output from consoles and terminal windows in Unix-like operating systems.

History : In Linux, there is a very useful command to show you all of the last commands that have been recently used

kill : kill command sends a signal to a process which terminates the process.

Top : top command is used to show the Linux processes. It provides a dynamic real-time view of the running system. Usually, this command shows the summary information of the system and the list of processes or threads which are currently managed by the Linux Kernel

