import os

def main():
    i = 0
    path = "E:/Pictures/Family"
    
    for filename in os.listdir(path):
        my_dest = "fam"+str(i)+".jpg"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest)
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main() 