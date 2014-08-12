from sys import argv

script, filename = argv

print "Were going to erase %r" %filename

print "Openig file"
target = open(filename, 'w')

target.truncate()

print "no well be writing to the new file"

line1 = raw_input("Enter line 1:")
line2 = raw_input("Enter line 2:")
line3 = raw_input("Enter line 3:")

print "no well be writing the the old file \n"

target.write(line1)
target.write(line2)
target.write(line3)

target.close()

target = open(filename, 'r')
target.read()
