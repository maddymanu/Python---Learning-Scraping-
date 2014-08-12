print "were trying to practise evrythin again \n"

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
'''

print poem

def secret_formula(started):
  jelly_beans = started*500
  jars = jelly_beans/50
  crates = jars/10
  return jelly_beans, jars, crates

starting_point = 10000
beans, jars, crates = secret_formula(starting_point)
print "We have %d %d %d" %(beans, jars, crates)
