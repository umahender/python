from sys import argv
if len(argv)==4:
    try:
        fp1 = open(argv[1], "r")
        fp2 = open(argv[2], "r")
        fp3 = open(argv[3], "w+")

        for i in fp1:
            fp3.write(i)
        for i in fp2:
            fp3.write(i)
        print(argv[3])
        fp3.seek(0,0)
        for i in fp3:
            print(i,end="")
        fp1.close()
        fp2.close()
        fp3.close()
    except Exception:
        print("\n Enter valid file names")
