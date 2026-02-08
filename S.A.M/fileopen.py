#search for files in the whole computer and open it
#for "python" use endswith(".py")
#same applies for word ppt exxcel jpg 
import os
def cdrive(fileloc,filename,ftype):
    c=fileloc.lower()
    if c=="c":
        whole_dir=os.walk(r"C:\Users\acer")
    else:
        whole_dir=os.walk(r"D:\\")
    for i,j,k in whole_dir:
        for file in k:
            
            if file.lower().endswith("." + ftype) and file.lower().startswith(filename):
                print("the file exists")
                os.startfile(os.path.join(i,file))
                return

# fname=input("whats the file name: ").lower()
# ftype=input("whats the file type: ").lower()
# cdrive(fname,ftype)