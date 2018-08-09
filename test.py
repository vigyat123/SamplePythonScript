import commands

output = commands.getoutput('ls -al')
print output

num = output.count('d')
print num
