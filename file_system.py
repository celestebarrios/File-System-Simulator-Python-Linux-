class DirectoryTree:
# Defining class attributes with values []
    folder = []
    files = []

    # Creating init function
    def __init__(self, prev, folder_name):
        self.prev = prev
        self.folder_name = folder_name

# Instance of a class (not attribute)
square_one = DirectoryTree(prev=None, folder_name='square_one')
cur = square_one
path = 'square_one'

# Create file(s)
def touch(name):
    global cur
    if name in cur.files:
        print(' Duplicate file name found. Please enter new name. ')
    else:
        cur.files.append(name)
        print(' Created a new folder. ')


# Make directory (create folder)
def mkdir(name):
    global cur
    if name in cur.folder:
        print(' Duplicate folder name! Please try again.')
    else:
        folder = DirectoryTree(prev=cur, folder_name=name)
        cur.folder.append(folder)
        print(' Folder name created. ')

# Change directory
def cd(name):
    global cur, path
    if name == '..':
        if cur.prev is not None:
            path = path[:(len(path)-len(cur.folder_name))-1]
            cur = cur.prev
    # if name == '../..':
    #     if cur.prev is not None and cur.prev.prev is not None:
    #         path = path[:(len(path)-len(cur.folder_name))-2]
    #         cur = cur.prev.prev
    else:
        for i in cur.folder:
            if i.folder_name == name:    
                cur = i
                path = path + '/' + name
                return
        print(' No folder found. ')

# List directories
def ls():
    global cur
    for i in cur.files:
        print(i)
    for j in cur.folder:
        print(j.folder_name)

if __name__ == '__main__':
    while True:
        print(path, end='>')
        command = input().split(' ')
        if command[0] == 'touch':
            try:
                touch(command[1])
            except:
                print('Format error: create File Name. ')
        elif command[0] == 'mkdir':
            try:
                mkdir(command[1])
            except:
                print(' Format error: mkdir Folder Name. ')
        elif command[0] == 'cd':
            try:
                cd(command[1])
            except:
                print('Format error: cd DirectoryName or cd .. or cd ../..')
        elif command[0] == 'ls':
            ls()
        else:
            print('{} is not the correct command.')
