import sys

def usage():
    pass

def dump_header(file):
    file.write("#pragma once\n")
    file.write("\n")
    file.write("unsigned char %s[] = {\n"%array_name)


def dump_end(file):
    file.write("};")

def dump_data(file, data):
    for i in range(0, len(data)):
        ch = data[i]
        file.write("0x%02x, "%(ord(ch) & 0xff))
        if ((i+1) % 15 == 0):
            file.write("\n");
    file.write("\n");


if (len(sys.argv) < 4): 
    usage();

binary_file_name = sys.argv[1];
header_file_name = sys.argv[2]
array_name = sys.argv[3];

try:
    binary_file = open(binary_file_name, "rb")
    binary_data = binary_file.read()
    header_file = open(header_file_name, "wb")
    dump_header(header_file)
    dump_data(header_file, binary_data)
    dump_end(header_file)
except Exception, msg:
    print msg

