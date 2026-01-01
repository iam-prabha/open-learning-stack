# Linux & terminal commands

## what is shell?

- A shell is a command-line interpreter that provides a user interface for interacting with the operating system.

- Shell commands are used to perform various tasks such as file management, system configuration, and process control.
 
 ## commands
- `echo` (print text)
- `whereis` (locate files/programs)
- `ls` (list files)
- `ls -a` (list files including hidden files)
- `ls -l` (list files with details)
- `ls -lh` (list files with details and human-readable sizes)
- `pwd` (print working directory)
- `cd` (change/go to directory)
- `mkdir` (make directory)
- `mkdir -p` (make parent directories)
- `cat` (display file contents)
- `cat > file.txt` (create and write to a file)
- `man` (display manual pages)
- `mv` (move/rename files/directories) - `rm` (remove files/directories)
- `rm -r` (remove directories recursively)
- `sudo` (run command with superuser privileges)
- `df -h` (display disk usage)
- `head` (display first lines of a file)
- `head -n 10 file.txt` (display first 10 lines of a file)
- `tail` (display last lines of a file)
- `tail -n 10 file.txt` (display last 10 lines of a file)
- `diff` (compare files)
- `diff file1.txt file2.txt` (compare two files)
- `locate` (find files by name)
- `locate file.txt` (find file.txt)
- `find` (search for files)
- `find . -type f -name "*.txt"` (find all .txt files in current directory)
- `find . -type f -iname "*.txt"` (find all .txt files in current directory (case-insensitive))
- `chmod u=rwx,g=rx,o=r` (change file permissions. u=user,g=group,o=others, 
r=readable, w=writable, x=executable)
- `chmod 777` (short way to make file executable and each number refer to 7=user, 7=group, and 7=others)
- `chown` (change file ownership)
- `find . -perm 777` (find all files with permissions 777)
- `grep` (search for patterns in files)
- `grep -i "pattern" file.txt` (search for pattern in file.txt (case-insensitive))
- history (display command history)
- `jobs` (list background jobs)
- `wget` (download files from the web)
- `wget -O file.txt https://example.com/file.txt` (download file.txt from https://example.com/file.txt)
- `useradd user_name` (add a new user)
- `userdel user_name` (delete a user)
- `getent group user_name` (get group information for user_name)
- `getent passwd user_name` (get user information for user_name)
