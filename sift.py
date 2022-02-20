import argparse
import threading
import sys
import os

class Watcher(threading.Thread):
    def __init__(self, pipe):
        super().__init__()
        self.stopped = False
        self.pipe = pipe
    
    def run(self):
        with open(self.pipe) as comm:
            while True:
                line = comm.readline().strip()
                if line != "":
                    print(line)
                else:
                    os.remove(args.file)
                    os.remove(args.file + "_out")
                    exit(0)

def create(args):
    os.mkfifo(args.file)
    os.mkfifo(args.file + "_out")
    thread = Watcher(args.file + "_out")
    thread.start()
    with open(args.file, 'w') as comm:
        for line in sys.stdin:
            comm.write(line)

def connect(args):
    with open(args.file) as comm:
        with open(args.file + "_out", 'w') as out:
            while True:
                line = comm.readline().strip()
                if line != "":
                    print(line)
                    answer = input("? (y) ")
                    if answer != "n":
                        out.write(line + "\n")
                        out.flush()
                else:
                    exit(0)

parser = argparse.ArgumentParser(description="Filter input manually")
sub = parser.add_subparsers()
sub_create = sub.add_parser("create", help="Create a filter")
sub_create.add_argument("-f", "--file", help="path to the file for filter communication")
sub_create.set_defaults(func=create)
sub_connect = sub.add_parser("connect", help="Connect to a filter")
sub_connect.add_argument("-f", "--file", help="path you used to create the filter")
sub_connect.set_defaults(func=connect)

args = parser.parse_args()
args.func(args)
