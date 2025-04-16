''' 
As discussed previously in this chapter, the PATH variable determines which files can be executed without specifying their path explicitly. Run through the commands in this exercise to see this principle in action.

Set the current PATH variable to another variable so we can revert to it later:

$ OLDPATH=$PATH
$ echo $OLDPATH
/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/aws/bin:/home/ubuntu/bin
Temporarily change PATH and try to run a program that is no longer located in the directories specified in PATH:

$ cd /usr/local
$ ls
bin etc games include lib man sbin share src
$ PATH="" ls
-bash: ls: No such file or directory
$ ls
bin etc games include lib man sbin share src
Note: The contents of local folder may be different in your case.

Now, create an executable in your home directory by entering the following:

cd ~
touch test.sh
echo '#!/bin/bash' >> test.sh 
echo 'echo "Hello world"' >> test.sh
chmod +x test.sh # Make sure test.sh has the executable permission
Run the executable, first by specifying the path, then by running it like a command:

$ ./test.sh
Hello world
$ test.sh
-bash: test.sh: command not found
Now, change PATH more permanently for your current session, and try to run test.sh again:

$ PATH=$PATH:$HOME
$ echo $PATH
/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/aws/bin:/home/ubuntu/bin:/home/ubuntu
$ test.sh
Hello world
$ cd /
$ test.sh
Hello world
Exit out of Terminal and then open it up again. Try running test.sh again:

$ test.sh
-bash: test.sh: command not found

'''