# sift
A tool to filter manually on the terminal

Basically, it takes its standard in, and acts as a server that you can then connect to, and manually choose what to send to standard out.

To use:
1. run `input | ./sift.py create --path path/to/temp/file | output`
2. run `./sift.py create --path path/to/temp/file` (needs to be the same path)
3. use, default is to keep
