# gen-search.py

#Let's define a generator that would search
#for some keyword in a huge text file line-by-line.

def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    for line in f:
        if keyword in line:
            # If keyword found, return it
            yield line
    f.close()

the_generator = search('Python', 'directory.txt')
# Nothing happened

print(next(the_generator))
#generator started
#Anton Pythonio 111-222-333

print(next(the_generator))	 	 
#generator started	 	 
#Fritz Pythonmann 128-256-512

print(next(the_generator))
#generator started
#Guido Pythonista 123-456-789

