'''
Run the following commands to experiment with altering your command line environment:

copy code
$ cd
$ PS1="\u@\w$ "
ubuntu@~$ echo "Hello world"
Hello world
ubuntu@~$

Once we exit our Terminal the changes disappear 

echo 'export PS1="this is a test$ "' >> ~/.bashrc
The line above saves the changes permanently in bashrc, >> 

Note that we are using single quotes in this command to surround the argument since part of the argument includes double quotes -- if we used double quotes, bash would have trouble with the command.

The redirection operator (>>) is used to append text to a file. If the target file doesn't exist, then it will be created. If you only use one > and the output file already exists, it will be overwritten.
IMPORTANT, use >> to dont overwrite the file.

'''