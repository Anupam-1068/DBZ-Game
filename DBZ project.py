import csv
import os
def write_data():
    f=open("d.csv","w")
    r=csv.writer(f,delimiter=',',lineterminator='\n')
    r.writerow(["Charachter Name","Level","Experience Point"])
    n=int(input("How many records: "))
    for i in range(n):
        while(True):
                adm=input("Enter Charachter Name:(8-15 Letters) ")
                if len(adm)>=8 and len(adm)<=15:
                    break
                else:
                    adm=input("Enter Charachter Name:(8-15 Letters) ")
        while(True):
                level=int(input("Enter Level(minimum Level 20,Maximum Level 100): "))
                if level>=20 and level<=100:
                    break
                else:
                    level=int(input("Enter Level(minimum Level 20,Maximum Level 100): "))
        while(True):
                xp=int(input("Enter Experience Points(minimum 20000,Maximum Level 100000000): "))
                if xp>=20000 and xp<=1000000000:
                    break
                else:
                    xp=int(input("Enter Experience Points(minimum 20000,Maximum 100000000): "))
        
        rec=[adm,level,xp]
        r.writerow(rec)
    f.close()

def read_data():
    f=open("d.csv","r")
    rec=csv.reader(f)
    for i in rec:
        print(i[0],i[1],i[2],sep="\t\t\t")
        print("------------------------------------------------------------------------------")
    f.close()
def sea(x,y,searc):   #Part of search module
    f=open("d.csv","r")
    rec=csv.reader(f)
    flag=0
    for i in rec:
        print(i[0],i[1],i[2],sep="\t\t\t")
        flag=1
    if flag==0:
        print(searc," not found")
    f.close()    
def search_data():
    searc=input('''
            1)Search Using NAME
            2)Search Using LEVEL
            3)Search Using EXPERIENCE POINT
            ''')
    if searc=="1":
        seaid=input("Enter Name to be searched :")
        sea(seaid,0,searc)
    elif searc=="2":
        seaname=input("Enter Level to be searched :")
        sea(seaname,1,searc)
    elif searc=="3":
        seaamt=input("Enter Experience Points to be searched :")
        sea(seaamt,2,searc)
    else:
        print("Invalid input")
        cont="Y"
def delete_data():
    delete=input('''
            1)Delete Using NAME
            2)Delete Using LEVEL
            3)Delete Using EXPERIENCE POINT
            ''')
    f=open("d.csv","r")
    rec=csv.reader(f)
    for i in rec:
        print(i[int(delete)-1])
    f.close()
    if delete=="1":
        remove_data0()
    elif delete=="2":
        remove_data1()
    elif delete=="3":
        remove_data2()
    else:
        print("Invalid input")
        cont="Y"
    
def append_data():
    f=open("d.csv","a")
    r=csv.writer(f,delimiter=',',lineterminator='\n')
    n=int(input("How many records: "))
    for i in range(n):
        while(True):
                adm=input("Enter Charachter Name:(8-15 Letters) ")
                if len(adm)>=8 and len(adm)<=15:
                    break
                else:
                    adm=input("Enter Charachter Name:(8-15 Letters) ")
        while(True):
                level=int(input("Enter Level(minimum Level 20,Maximum Level 100): "))
                if level>=20 and level<=100:
                    break
                else:
                    level=int(input("Enter Level(minimum Level 20,Maximum Level 100): "))
        while(True):
                xp=int(input("Enter Experience Points(minimum 20000,Maximum Level 100000000): "))
                if xp>=20000 and xp<=1000000000:
                    break
                else:
                    xp=int(input("Enter Experience Points(minimum 20000,Maximum 100000000): "))
        rec=[adm,level,xp]
        r.writerow(rec)
    f.close()
def remove_data0():
 f=open("d.csv","r")
 g=open("temp.csv","w")
 r=csv.writer(g,delimiter=',',lineterminator='\n')
 pn=input("Enter Charachter name to be deleted: ")
 rec=csv.reader(f)
 header=next(rec)
 r.writerow(header)
 for i in rec:
     if i[0]!=pn:
         r.writerow(i)
 f.close()
 g.close()
 os.remove("d.csv")
 os.rename("temp.csv","d.csv")
 print("Record Deleted")
def remove_data1():
 f=open("d.csv","r")
 g=open("temp.csv","w")
 r=csv.writer(g,delimiter=',',lineterminator='\n')
 pn=input("Enter Charachter Level to be deleted: ")
 rec=csv.reader(f)
 header=next(rec)
 r.writerow(header)
 for i in rec:
     if i[1]!=pn:
         r.writerow(i)
 f.close()
 g.close()
 os.remove("d.csv")
 os.rename("temp.csv","d.csv")
 print("Record Deleted")
def remove_data2():
 f=open("d.csv","r")
 g=open("temp.csv","w")
 r=csv.writer(g,delimiter=',',lineterminator='\n')
 pn=input("Enter Charachter Experience Points to be deleted: ")
 rec=csv.reader(f)
 header=next(rec)
 r.writerow(header)
 for i in rec:
     if i[2]!=pn:
         r.writerow(i)
 f.close()
 g.close()
 os.remove("d.csv")
 os.rename("temp.csv","d.csv")
 print("Record Deleted")
def update_data():
 f=open("d.csv","r")
 g=open("temp.csv","w")
 r=csv.writer(g,delimiter=',',lineterminator='\n')
 while(True):
                adm=input("Enter Charachter Name To Be Updated:(8-15 Letters) ")
                if len(adm)>=8 and len(adm)<=15:
                    break
                else:
                    adm=input("Enter Charachter Name To Be Updated:(8-15 Letters) ")
 rec=csv.reader(f)
 header=next(rec)
 r.writerow(header)
 for i in rec:
    if i[0]==adm:
         while(True):
                i[0]=input("Enter  Updated Charachter Name:(8-15 Letters) ")
                if len(i[0])>=8 and len(i[0])<=15:
                    break
                else:
                    i[0]=input("Enter Updated Charachter Name:(8-15 Letters) ")
         while(True):
                i[1]=int(input("Enter Updated Level(minimum Level 20,Maximum Level 100): "))
                if i[1]>=20 and i[1]<=100:
                    break
                else:
                    i[1]=int(input("Enter Updated Level(minimum Level 20,Maximum Level 100): "))
         while(True):
                i[2]=int(input("Enter Updated Experience Points(minimum 20000,Maximum Level 100000000): "))
                if i[2]>=20000 and i[2]<=1000000000:
                    break
                else:
                    i[2]=int(input("Enter Updated Experience Points(minimum 20000,Maximum 100000000): "))
         r.writerow(i)
    else:
         r.writerow(i)
 f.close()
 g.close()
 os.remove("d.csv")
 os.rename("temp.csv","d.csv")
a=input("Enter Username")
b=input("Enter Password")
print("New ID has been created")
write_data()
ch='y'
while(ch=="y" or ch=="Y"):
    m=input('''------------------------------MENU DRIVE---------------------------------------
        Choose from options given below:
        
        1)Display
        2)Delete
        3)Append
        4)Search
        5)Update
        6)Exit
            ''')
    if m=="1": 
        read_data()
    elif m=="2":
        print("***************************************Deleting Data***************************")
        delete_data()
    elif m=="3":
        print("***************************************Appending Data***************************")
        append_data()
    elif m=="4":
        print("****************************************searching data***************************")
        search_data()
    elif m=="5":
        print("*****************************************Updating Data***************************")
        update_data()
    ch=input("Do You Want To Continue? Press y to CONTINUE or e to EXIT ")
