from sys import argv

script, input_file = argv

def print_all(f):
  print f.read()

def rewind(f):
  f.seek(0)

def print_a_line(line_count, f):
  print line_count, f.readline()

current_file = open(input_file)

print "Pringting the entire file \n"
print_all(current_file)

print "Now ere rewidning"
rewind(current_file)

curr_line =1
print_a_line(curr_line , current_file)

currline = curr_line+1
print_a_line(curr_line , current_file)
