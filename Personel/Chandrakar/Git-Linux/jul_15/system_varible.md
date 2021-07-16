
Ans (O1) :-     System varible  :- system  varible is following command at a console/terminal. Basically these variables are defined in    				    Capital Letters.

        a)  echo $BASH_VERSION  : - Holds the version of this instance of bash.
        b)  echo $HOSTNAME      : - This is show our computer name.
        c)  echo $CDPATH        : - The search path for the cd command.
        d)  echo $HISTFILE      : - The name of the file in which command history is saved.
        e)  echo $HISTFILESIZE  : - The maximum number of lines contained in the history file.
        f)  echo $HISTSIZE      : - The number of commands to remember in the command history
        g)  echo $HOME          : - The home directory of the current user.
        h)  echo $IFS           : - The Internal Field Separator that is used for word splitting after expansion and to split lines into 					     words with the read builtin command
        i)  echo $LANG          : - Used to determine the locale category for any category not specifically selected with a variable   					     starting with LC_
        j)  echo $PATH          : - The search path for commands. It is a colon-separated list of directories in which the shell looks for 				     commands.
        k)  echo $PS1           : - Your prompt settings.
        l)  echo $TMOUT         : - The default timeout for the read builtin command.
        m)  echo $TERM          : - Your login terminal type.
        n)  echo $SHELL         : - Set path to login shell.
        o)  echo $DISPLAY       : - Set X display name
        p)  export EDITOR=/usr/bin/vim : - Set name of default text editor.



Ans (02) :-  User defined varible :- These are the variables created by user for storing, reading, accessing and manipulating data.

            Example               : -  var1=local
            
		echo $var1		// Output: local
		echo $SHLVL		//Output: 1
		bash <Enter>		//concept of nested shell
		echo $SHLVL		//Output: 2 //indicating nested  shell
		echo $var1		//no output will appear
		
Ans (03) :- Scrit system varible 
             
              #!/usr/bin/bash
	      echo $PATH
	      echo $HOME
	      echo $CDPATH
	      echo $HOSTNAME
	      
	      
	      		
		
		
		
		
