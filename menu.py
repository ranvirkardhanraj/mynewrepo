import time
import datetime
import sqlite3
import backup
import sms

def issue_book():
    prn=input('Enter the PRN of student :')
    bkno = input('Enter the issue book NUMBER :')
    isdt=str(datetime.date.today())
    con=sqlite3.connect("Data.db")
    cur=con.cursor()
    add="select prn from all_student"
    cur.execute(add)
    data=cur.fetchall()


    for i in data:

        for j in i:
            prn1=int(prn)
            if j==prn1:


                add1="select book_no from all_books"
                cur.execute(add1)
                data1=cur.fetchall()


                for m in data1:

                    for n in m:
                        bkno1=int(bkno)
                        if n==bkno1:
                            status1="Not"
                            prn1=str(prn)
                            bkno1=str(bkno)
                            add2="insert into issue_book(stu_prn,book_no,status,Date) values ("+prn1+","+bkno1+",'"+status1+"','"+isdt+"')"
                            con.execute(add2)
                            con.commit()
                            print('Data Saved...\n')
                            time.sleep(2)

                        else:
                            print("No book present of book no.:",bkno)
            else:
                print("no student is present of PRN:",prn)



def return_book():
    bkno=input("Enter Book Number:")
    con=sqlite3.connect("Data.db")
    cur=con.cursor()
    add="select book_no from all_books"
    cur.execute(add)
    data=cur.fetchall()

    cur.close()
    for d in data:

        for i in d:

            bkno1=int(bkno)
            if i==bkno1:


                news="Returned"
                newd=str(datetime.date.today())
                add1="update not_return_book set status='"+news+"',date='"+newd+"' where book_no="+bkno
                con.execute(add1)
                con.commit()
                con.close()
                print("update saved...")
                time.sleep(2)
            else:
                print("number of book",bkno," is not in librery")






def add_new_book():
    con1 = sqlite3.connect("Data.db")
    bkno = input("Enter the Book number :")
    bknm = input("Enter the name of Book :")
    auth = input("Enter the name of Author of Book :")
    pub = input("Enter the name of Publication of Book :")
    add = "insert into all_books(book_no,book_name,book_author,book_pub) values ("+ bkno +",'"+ bknm +"','"+ auth +"','"+ pub +"')"
    con1.execute(add)
    con1.commit()
    con1.close()
    print('DATA IS STORED...')
    time.sleep(3)

def add_new_stud():
    con1 = sqlite3.connect("Data.db")
    prn = input("Enter the PRN of student :")
    stnm = input("Enter the name of student :")
    mob = input("Enter the mobile number of student :")
    add="insert into all_student(prn,stu_name,stu_mob) values ("+prn+",'"+stnm+"',"+mob+")"
    con1.execute(add)
    con1.commit()
    con1.close()
    print('DATA SAVED...')
    time.sleep(3)

def show_all_books():
    con=sqlite3.connect("Data.db")
    cur=con.cursor()
    add="select * from all_books"
    cur.execute(add)
    data=cur.fetchall()
    for d in data:
        print('Book Number:',d[0])
        print('Book Name:',d[1])
        print('Book Author:',d[2])
        print('Book Publication:',d[3])
        time.sleep(2)
        print()
    cur.close()
    con.close()

def show_all_stud():
    con = sqlite3.connect("Data.db")
    cur = con.cursor()
    add = "select * from all_student"
    cur.execute(add)
    data = cur.fetchall()
    for d in data:
        print('Student PRN No.:', d[0])
        print('Student Name:', d[1])
        print('Student Mobile No.:', d[2])
        time.sleep(2)
        print()
    cur.close()
    con.close()

def not_ret_books():

    prn=input("Enter Student PRN no.:")
    bkno = input("Enter Book Number:")
    con = sqlite3.connect("Data.db")
    cur = con.cursor()
    add = "select book_no from all_books"
    cur.execute(add)
    data = cur.fetchall()

    cur.close()
    for d in data:

        for i in d:

            bkno1 = int(bkno)
            if i == bkno1:
                stat="Not Return"
                date1=str(datetime.date.today())
                add="insert into not_return_book(book_no,prn,status,date) values ("+bkno+","+prn+",'"+stat+"','"+date1+"')"
                con.execute(add)
                con.commit()
                con.close()
                print("Data saved...")
                time.sleep(2)
            else:
                print("No book of Number:",bkno)


def search_book():
    print("1 - Search by Book Number")
    print("2 - Search by Book Name")
    print("3 - Search by Book Author")
    print("4 - Search by Book Publication")
    ch = int(input("Provide your choice : "))
    print()
    while True:
        if ch== 1:
            bkno=input('Enter the book Number: ')
            con=sqlite3.connect("Data.db")
            cur=con.cursor()
            add="select * from all_books where book_no="+bkno
            cur.execute(add)
            data=cur.fetchall()
            for d in data:
                print("Book Name:",d[1])
                print('Book Author:',d[2])
                print('Book Publication',d[3])
                time.sleep(2)
                print()
            cur.close()
            con.close()
            break


        elif ch== 2:
            bkn = input('Enter the book Name: ')
            con = sqlite3.connect("Data.db")
            cur = con.cursor()
            add = "select * from all_books where book_name='"+bkn+"'"
            cur.execute(add)
            data = cur.fetchall()
            for d in data:
                print("Book Number:", d[0])
                print('Book Author:', d[2])
                print('Book Publication', d[3])
                time.sleep(2)

            cur.close()
            con.close()
            break

        elif ch== 3:
            bka = input('Enter the book Author: ')
            con = sqlite3.connect("Data.db")
            cur = con.cursor()
            add = "select * from all_books where book_author='"+bka+"'"
            cur.execute(add)
            data = cur.fetchall()
            for d in data:
                print("Book Number:", d[0])
                print('Book Name:', d[1])
                print('Book Publication', d[3])
                time.sleep(2)
                print()
            cur.close()
            con.close()
            break
        elif ch== 4:
            bkpub = input('Enter the book Publication: ')
            con = sqlite3.connect("Data.db")
            cur = con.cursor()
            add = "select * from all_books where book_pub='"+bkpub+"'"
            cur.execute(add)
            data = cur.fetchall()
            for d in data:
                print("Book Number:", d[0])
                print('Book Name:', d[1])
                print('Book Author', d[2])
                time.sleep(2)
                print()
            cur.close()
            con.close()

        else:
            print('Enter valid No.:1/2/3/4')
            ch=int(input(":="))


# ask for book publication and search


def search_stud():
    # accept enrollment number of student and print his/her details
    print("1 - Search by Student PRN Number")
    print("2 - Search by Student Name")
    print("3 - Search by Student Mobile Number")
    ch = int(input("Provide your choice : "))
    while True:
        if ch==1:
            prn1=input("Enter student PRN No.: ")
            con=sqlite3.connect("Data.db")
            cur=con.cursor()
            add="select * from all_student where prn="+prn1
            cur.execute(add)
            data=cur.fetchall()
            for d in data:
                print('Student Name:',d[1])
                print('Student Mobile number:',d[2])
                time.sleep(2)
                print()
            cur.close()
            con.close()
            break

        elif ch==2:
            stu=input("Enter student Name: ")
            con=sqlite3.connect("Data.db")
            cur=con.cursor()
            add="select * from all_student where stu_name='"+stu+"'"
            cur.execute(add)
            data=cur.fetchall()
            for d in data:
                print('Student Name:',d[0])
                print('Student Mobile number:',d[2])
                time.sleep(2)
                print()
            cur.close()
            con.close()
            break

        elif ch==3:
            stum=input("Enter student Mobile No.: ")
            con=sqlite3.connect("Data.db")
            cur=con.cursor()
            add="select * from all_student where stu_mob="+stum
            cur.execute(add)
            data=cur.fetchall()
            for d in data:
                print('Student Name:',d[1])
                print('Student Mobile number:',d[0])
                time.sleep(2)
                print()
            cur.close()
            con.close()
            break

        else:
            ch=int(input('Enter valid choice 1/2/3\nAns:='))

def update_books():
    con1=sqlite3.connect("Data.db")
    bkno = input("Enter Book Number:")
    con = sqlite3.connect("Data.db")
    cur = con.cursor()
    add = "select book_no from all_books"
    cur.execute(add)
    data = cur.fetchall()

    cur.close()
    for d in data:

        for i in d:

            bkno1 = int(bkno)
            if i == bkno1:
                choice=int(input('What you want to update\n1 - book_number\n2 - book_name\n3 - book_author\n3 - book_publication\nAns:'))
                while True:
                    if choice==1:
                        ubookn=input('Enter new book No.:')
                        add = "update all_books set book_no='"+ubookn+"' where book_no="+bkno
                        add1= "update issue_book set book_no='"+ubookn+"' where book_no="+bkno
                        add2= "update not_return_book set book_no='"+ubookn+"' where book_no="+bkno
                        con1.execute(add)
                        con1.execute(add1)
                        con1.execute(add2)
                        con1.commit()
                        print("Data Updated...")
                        time.sleep(3)
                        con1.close()
                        break
                    elif choice==2:
                        ubookna=input('Enter new book name:')
                        add = "update all_books set book_name='"+ubookna+"' where book_no="+bkno

                        con1.execute(add)
                        con1.commit()
                        print('Data Updated...')
                        time.sleep(3)
                        con1.close()
                        break
                    elif choice==3:
                        ubooka=input('Enter new book Author:')
                        add = "update all_books set book_author='"+ubooka+"' where book_no="+bkno
                        con1.execute(add)
                        con1.commit()
                        print('Data Updated...')
                        time.sleep(3)
                        con1.close()
                        break
                    elif choice==4:
                        ubookpub=input('Enter new book publication:')
                        add = "update all_books set book_name='"+ubookpub+"' where book_no="+bkno
                        con1.execute(add)
                        con1.commit()
                        print('Data Updated...')
                        time.sleep(3)
                        con1.close()
                        break
                    else:
                        print("Enter valid No.\n1/2/3/4\nAns:")
            else:
                print("No book of number:",bkno)



def take_backup():
    # write logic to send email to him-self with 3 attachments
    # (all 3 files should be mailed..)

    i=0
    while i<20:
        print('_',end='')
        time.sleep(0.2)
        i=i+1
        if i==19:
            backup.backup()
            print('_', end='')
            time.sleep(0.2)
            print('_', end='')
            time.sleep(0.2)
    print(' Backup successfull........!!!!!!')
    time.sleep(3)

def get_mob_num(s_enr_num):
    obj = open("D:\\all_student.txt","r")
    stud_ls = obj.readlines()
    for one_stud_data in stud_ls:
        ls2 = one_stud_data.split("-")
        if ls2[0]==s_enr_num:
            return ls2[2][0:len(ls2[2])-1]


def send_sms():
    # write logic to send sms to students whose return-date is near-by
    # one-day before return-date

    c = open('D:\\issue_book.txt', 'r')
    is_bk_ls = c.readlines()
    c.close()

    for one_line in is_bk_ls:
        ls = one_line.split(",")
        if ls[3]=="NOT\n":
            s_mob = get_mob_num(ls[0])
            sms.sms(s_mob)



def delete_student():
    prn=input('Enter student PRN No.:for Delete the student:')
    con=sqlite3.connect("Data.db")
    add="delete from all_student where prn="+prn
    con.execute(add)
    con.commit()
    con.close()
    print('Student Data deleted...')
    time.sleep(2)

# driving logic here
while True:
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - To add New Book")
    print("4 - To add New Student")
    print("5 - To Search Book")
    print("6 - To Search Student")
    print("7 - Not Returned Books")
    print("8 - Show All Books")
    print("9 - Show All Students")
    print("10 - To Delete Student From Data Base")
    print("11 - To update book_data")
    print("* - Take Backup")
    print("# - To Send Remainder SMS")
    print("0 - EXIT")
    ch = input("Provide your choice : ")
    print()
    if ch == '1':
        issue_book()
    elif ch == '2':
        return_book()
    elif ch == '3':
        add_new_book()
    elif ch == '4':
        add_new_stud()
    elif ch == '5':
        search_book()
    elif ch == '6':
        search_stud()
    elif ch == '7':
        not_ret_books()
    elif ch == '8':
        show_all_books()
    elif ch == '9':
        show_all_stud()
    elif ch == '10':
        delete_student()
    elif ch=='11':
        update_books()
    elif ch == '*':
        take_backup()
    elif ch == '#':
        send_sms()
    elif ch == '0':
        exit(0)



