
# Read - 'r'
# Write - 'w'
# Append - 'a'
# Read binary/image - 'rb'
# Write binary/image - 'wb'

f = open('Intro', 'r')
# Read everything from file:
print(f.read())
# Read first line from file:
print(f.readline())

# Write in file:
f1 = open('New', 'w')
f1.write("This is new file")

# To append in the file:
f2 = open('New', 'a')
f2.write("\nAppend text")

# To read binary / Image:
f3 = open('s.png', 'rb')
for i in f3:
    print(i)

# To write binary / Image:
f3 = open('s.png', 'rb')
f4 = open('Image.png', 'wb')
for i in f3:
    f4.write(i)
