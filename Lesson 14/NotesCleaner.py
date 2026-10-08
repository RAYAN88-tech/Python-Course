# Part 1 - read(n)

word = int(input(" How many characters to preview?"))
file = open("Class-Notes.txt", 'r')
print(file.read(word))
file.close()

# Part 2 - readlines()

file = open("Class-Notes.txt", 'r')
store = file.readlines()
file.close()
print("Total lines", len(store))
for i in range(len(store)):
    print(i + 1, ":", store[i].strip())

# Part 3 - Filter lines
filter = input("Enter the word you want to skip")
file = open("Class-Notes.txt", 'r')
for line in file:
    if line.startswith(filter):
        print("Skip -> ", line.strip())
    else:
        print("keep -> ", line.strip())
file.close()

# Part 4 - Odd Lines
file = open("Class-Notes.txt", 'r')
lines = file.readlines()
file.close()

out = open("odd-lines.txt", 'w')
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
