# File-System-Simulator-Python-Linux
Avanan assessment!

In python we created four different tools to simulate Linux commands for mkdir,ls,cd,touch.

This program has driver code for any testing in the main function that runs user input for our methods based on our commands and whatever might come after that, however, for further testing a string based file is recommended. 

This code has some drawbacks with cd for the cd ../.. reads as cd .. which is not deemed correct at the time. 

Also cd .. can only run once before stating that the table does not exist.

//

A class was created for this directory tree with components prev and folder_name. "prev" acts as a previous node to the directory, "folder_name" acts as a name of folder. 

We also establish empty lists for the "folder" and "files" within the Class to  further allow commands in Linux. Drawbacks here are the lists inability to remove any duplicate files, however, simulates real system.

We instantiated a folder called square_one in the directory tree and used four different methods to call into action our commands.

Each function relying on different parameters and global variables (cur, path).

cur is the representation of the current node at run time, path is the literal path of the directory in the command line. 
