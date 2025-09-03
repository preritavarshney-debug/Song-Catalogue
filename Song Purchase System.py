from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime as dt
import mysql.connector as ms

root = Tk()
root.title("Song Purchasing System")
root.geometry("800x600")

conn=ms.connect(host="localhost", user="root", passwd="prerita", charset="utf8", db="songdb")
cur=conn.cursor()

#Main Frames
user_f = Frame(root)
admin_f = Frame(root)

#password for admin
password_f = Frame(root)

#Admin Subframes
add_song_f = Frame(root)
show_all_songs_f = Frame(root)
search_song_f = Frame(root)
modify_song_price_f = Frame(root)
modify_lyrics_status_f = Frame(root)
delete_song_f = Frame(root)
show_transactions_f = Frame(root)

#User Frames
show_all_songs_user_f = Frame(root)
claim_song_f = Frame(root)
cancel_song_f = Frame(root)
print_receipt_f = Frame(root)

#main window
def main_menu():
    admin_f.pack_forget()
    user_f.pack_forget()
    password_f.pack_forget()
    main_f.pack(pady=10)

#password window
def password_menu():
    main_f.pack_forget()
    for widget in password_f.winfo_children():
        widget.destroy()
    password_f.pack(pady=10)

    label = Label(password_f, text="Enter the password: ", bg="lightgreen", fg="black")
    label.pack(pady=10)
    entry = Entry(password_f, show="#")
    entry.pack(pady=10)

    def check_password():
        password = entry.get()
        if password == "prerita":
            admin_menu()
        else:
            messagebox.showinfo("Error", "Incorrect Password")

    submit_button = Button(password_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=check_password)
    submit_button.pack(pady=10)
    button5 = Button(password_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=main_menu)
    button5.pack(pady=10)

#admin menu
def admin_menu():
    main_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    password_f.pack_forget()
    for widget in password_f.winfo_children():
        widget.destroy()
    add_song_f.pack_forget()
    for widget in add_song_f.winfo_children():
        widget.destroy()
    show_all_songs_f.pack_forget()
    for widget in show_all_songs_f.winfo_children():
        widget.destroy()
    search_song_f.pack_forget()
    for widget in search_song_f.winfo_children():
        widget.destroy()
    modify_song_price_f.pack_forget()
    for widget in modify_song_price_f.winfo_children():
        widget.destroy()
    modify_lyrics_status_f.pack_forget()
    for widget in modify_lyrics_status_f.winfo_children():
        widget.destroy()
    delete_song_f.pack_forget()
    for widget in delete_song_f.winfo_children():
        widget.destroy()
    show_transactions_f.pack_forget()
    for widget in show_transactions_f.winfo_children():
        widget.destroy()

    button1 = Button(admin_f, text="Add a Song", activebackground="lightgreen", activeforeground="black", command=add_song)
    button1.pack(pady=10)
    button2 = Button(admin_f, text="Show All Songs", activebackground="lightgreen", activeforeground="black", command=show_all_songs)
    button2.pack(pady=10)
    button3 = Button(admin_f, text="Search a Song", activebackground="lightgreen", activeforeground="black", command=search_song)
    button3.pack(pady=10)
    button4 = Button(admin_f, text="Modify Song Price", activebackground="lightgreen", activeforeground="black", command=modify_song_price)
    button4.pack(pady=10)
    button5 = Button(admin_f, text="Modify Lyrics Status", activebackground="lightgreen", activeforeground="black", command=modify_lyrics_status)
    button5.pack(pady=10)
    button6 = Button(admin_f, text="Delete a Song", activebackground="lightgreen", activeforeground="black", command=delete_song)
    button6.pack(pady=10)
    button7 = Button(admin_f, text="Show All Transactions", activebackground="lightgreen", activeforeground="black", command=show_transactions)
    button7.pack(pady=10)
    button8 = Button(admin_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=main_menu)
    button8.pack(pady=10)
    admin_f.pack(expand=True, fill="both")
    
#user menu
def user_menu():
    main_f.pack_forget()
    for widget in user_f.winfo_children():
        widget.destroy()
    show_all_songs_user_f.pack_forget()
    for widget in show_all_songs_user_f.winfo_children():
        widget.destroy()
    claim_song_f.pack_forget()
    for widget in claim_song_f.winfo_children():
        widget.destroy()
    cancel_song_f.pack_forget()
    for widget in cancel_song_f.winfo_children():
        widget.destroy()
    print_receipt_f.pack_forget()
    for widget in print_receipt_f.winfo_children():
        widget.destroy()

    button0 = Button(user_f, text="Show All Songs", activebackground="lightgreen", activeforeground="black", command=show_all_songs_user)
    button0.pack(pady=10)
    button1 = Button(user_f, text="Claim a Song", activebackground="lightgreen", activeforeground="black", command=claim_song)
    button1.pack(pady=10)
    button2 = Button(user_f, text="Cancel Song Purchase", activebackground="lightgreen", activeforeground="black", command=cancel_song)
    button2.pack(pady=10)
    button3 = Button(user_f, text="Print Receipt", activebackground="lightgreen", activeforeground="black", command=print_receipt)
    button3.pack(pady=10)
    button4 = Button(user_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=main_menu)
    button4.pack(pady=10)
    user_f.pack(expand=True, fill="both")

#exit function
def exit_program():
    cur.close()
    conn.close()
    root.destroy()

#add song
def add_song():
    admin_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    add_song_f.pack(pady=10)

    label_sid = Label(add_song_f, text="Enter the Song ID: ", bg="lightgreen", fg="black")
    label_sid.pack()
    entry_sid = Entry(add_song_f)
    entry_sid.pack(pady=10)

    label_sn = Label(add_song_f, text="Enter the Song Name: ", bg="lightgreen", fg="black")
    label_sn.pack()
    entry_sn = Entry(add_song_f)
    entry_sn.pack(pady=10)

    label_price = Label(add_song_f, text="Enter the Price: ", bg="lightgreen", fg="black")
    label_price.pack()
    entry_price = Entry(add_song_f)
    entry_price.pack(pady=10)

    label_lyrics = Label(add_song_f, text="Enter Lyrics Status:", bg="lightgreen", fg="black")
    label_lyrics.pack()
    entry_lyrics = Entry(add_song_f)
    entry_lyrics.pack(pady=10)

    label_genre = Label(add_song_f, text="Enter Genre:", bg="lightgreen", fg="black")
    label_genre.pack()
    entry_genre = Entry(add_song_f)
    entry_genre.pack(pady=10)

    def add_song_db():
        sid = int(entry_sid.get())
        sn = entry_sn.get()
        price = float(entry_price.get())
        lyrics = entry_lyrics.get()
        genre = entry_genre.get()

        sql = "INSERT INTO song VALUES(%s, %s, %s, %s, %s)"
        val = (sid, sn, price, lyrics, genre)
        cur.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Success", "Song added successfully")

    submit_button = Button(add_song_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=add_song_db)
    submit_button.pack(pady=10)
    button5 = Button(add_song_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button5.pack(pady=10)
    
#show all songs
def show_all_songs():
    admin_f.pack_forget()
    for widget in show_all_songs_f.winfo_children():
        widget.destroy()
    show_all_songs_f.pack(expand=True, fill="both")

    sql = "SELECT * FROM song"
    cur.execute(sql)
    res = cur.fetchall()
    tree = ttk.Treeview(show_all_songs_f)
    tree['columns'] = ("Song ID", "Song Name", "Price", "Lyrics", "Genre")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Song ID", anchor=CENTER, width=50)
    tree.column("Song Name", anchor=CENTER, width=110)
    tree.column("Price", anchor=CENTER, width=50)
    tree.column("Lyrics", anchor=CENTER, width=50)
    tree.column("Genre", anchor=CENTER, width=50)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Song ID", text="Song ID", anchor=CENTER)
    tree.heading("Song Name", text="Song Name", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("Lyrics", text="Lyrics", anchor=CENTER)
    tree.heading("Genre", text="Genre", anchor=CENTER)

    if not res:
        messagebox.showinfo("Error", "No songs found")
    else:
        for i in res:
            tree.insert(parent="", index="end", text="", values=i)
        tree.pack(fill="both", expand=True)
    button5=Button(show_all_songs_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button5.pack(pady=10)

#search song
def search_song():
    admin_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    search_song_f.pack(pady=10)

    label_sid = Label(search_song_f, text="Enter the Song ID to search: ", bg="lightgreen", fg="black")
    label_sid.pack(pady=10)
    entry_sid = Entry(search_song_f)
    entry_sid.pack(pady=10)

    def search_song_db():
        sid = entry_sid.get()
        sql = "select * from song where sid = %s"
        val = (sid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Song not found")
        else:
            for i in res:
                song_details = f"Song Details:\nSong ID: {i[0]}\nSong Name: {i[1]}\nPrice: {i[2]}\nLyrics: {i[3]}\nGenre: {i[4]}"
                label_song_details = Label(search_song_f)
                label_song_details.pack(pady=10)
                label_song_details.config(text=song_details)

    submit_button = Button(search_song_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=search_song_db)
    submit_button.pack(pady=10)
    button5 = Button(search_song_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button5.pack(pady=10)

#modify song price
def modify_song_price():
    admin_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    modify_song_price_f.pack(pady=10)

    label_sid = Label(modify_song_price_f, text="Enter the Song ID whose price to modify: ", bg="lightgreen", fg="black")
    label_sid.pack(pady=10)
    entry_sid = Entry(modify_song_price_f)
    entry_sid.pack(pady=10)
    label_nf = Label(modify_song_price_f, text="Enter the new price: ", bg="lightgreen", fg="black")
    label_nf.pack(pady=10)
    entry_nf = Entry(modify_song_price_f)
    entry_nf.pack(pady=10)

    def modify_song_price_db():
        sid = entry_sid.get()
        new_price = float(entry_nf.get())
        sql = "select * from song where sid = %s"
        val = (sid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Song not found")
        else:
            song_details = f"\nOld Record\nSong ID: {res[0][0]}\nSong Name: {res[0][1]}\nPrice: {res[0][2]}\nLyrics: {res[0][3]}\nGenre: {res[0][4]}"
            label_song_details = Label(modify_song_price_f)
            label_song_details.pack(pady=10)
            label_song_details.config(text=song_details)

            sql = "update song set price = %s where sid = %s"
            val = (new_price, sid)
            cur.execute(sql, val)
            conn.commit()

            sql = "select * from song where sid = %s"
            val = (sid,)
            cur.execute(sql, val)
            res = cur.fetchall()
            song_details = f"\n\n\nNew Record\nSong ID: {res[0][0]}\nSong Name: {res[0][1]}\nPrice: {res[0][2]}\nLyrics: {res[0][3]}\nGenre: {res[0][4]}"
            label_song_details = Label(modify_song_price_f)
            label_song_details.pack(pady=10)
            label_song_details.config(text=song_details)

    submit_button = Button(modify_song_price_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=modify_song_price_db)
    submit_button.pack(pady=10)
    button5 = Button(modify_song_price_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button5.pack(pady=10)

#modify lyrics status
def modify_lyrics_status():
    admin_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    modify_lyrics_status_f.pack(pady=10)

    label_sid = Label(modify_lyrics_status_f, text="Enter the Song ID whose lyrics status to modify: ", bg="lightgreen", fg="black")
    label_sid.pack(pady=10)
    entry_sid = Entry(modify_lyrics_status_f)
    entry_sid.pack(pady=10)
    label_lf = Label(modify_lyrics_status_f, text="Enter the current status: ", bg="lightgreen", fg="black")
    label_lf.pack(pady=10)
    entry_lf = Entry(modify_lyrics_status_f)
    entry_lf.pack(pady=10)

    def modify_lyrics_status_db():
        sid = entry_sid.get()
        status = entry_lf.get()
        sql = "select * from song where sid = %s"
        val = (sid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Song not found")
        else:
            song_details = f"\nOld Record\nSong ID: {res[0][0]}\nSong Name: {res[0][1]}\nPrice: {res[0][2]}\nLyrics: {res[0][3]}\nGenre: {res[0][4]}"
            label_song_details = Label(modify_lyrics_status_f)
            label_song_details.pack(pady=10)
            label_song_details.config(text=song_details)

            sql = "update song set lyrics = %s where sid = %s"
            val = (status, sid)
            cur.execute(sql, val)
            conn.commit()

            sql = "select * from song where sid = %s"
            val = (sid,)
            cur.execute(sql, val)
            res = cur.fetchall()
            song_details = f"\n\n\nNew Record\nSong ID: {res[0][0]}\nSong Name: {res[0][1]}\nPrice: {res[0][2]}\nLyrics: {res[0][3]}\nGenre: {res[0][4]}"
            label_song_details = Label(modify_lyrics_status_f)
            label_song_details.pack(pady=10)
            label_song_details.config(text=song_details)

    submit_button = Button(modify_lyrics_status_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=modify_lyrics_status_db)
    submit_button.pack(pady=10)
    button5 = Button(modify_lyrics_status_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button5.pack(pady=10)

#delete song
def delete_song():
    admin_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    delete_song_f.pack(pady=10)

    label_sid = Label(delete_song_f, text="Enter the Song ID to delete: ", bg="lightgreen", fg="black")
    label_sid.pack(pady=10)
    entry_sid = Entry(delete_song_f)
    entry_sid.pack(pady=10)

    def delete_song_db():
        sid = entry_sid.get()
        sql = "select * from song where sid = %s"
        val = (sid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Song not found")
        else:
            confirm = messagebox.askyesno("Confirm", "Do you want to delete the song?")
            if not confirm:
                admin_menu()
                return
            sql = "delete from song where sid = %s"
            cur.execute(sql, val)
            conn.commit()
            messagebox.showinfo("Success", "Song deleted successfully")

    button_delete = Button(delete_song_f, text="Delete", activebackground="lightgreen", activeforeground="black", command=delete_song_db)
    button5 = Button(delete_song_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button_delete.pack(pady=10)
    button5.pack(pady=10)

#show transactions
def show_transactions():
    admin_f.pack_forget()
    for widget in admin_f.winfo_children():
        widget.destroy()
    show_transactions_f.pack(expand=True, fill="both")

    sql = "SELECT * FROM transaction"
    cur.execute(sql)
    res = cur.fetchall()
    tree = ttk.Treeview(show_transactions_f)
    tree["columns"] = ("Trans ID", "Song ID", "User Name", "Contact", "Date Of Booking")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Trans ID", anchor=CENTER, width=100)
    tree.column("Song ID", anchor=CENTER, width=100)
    tree.column("User Name", anchor=CENTER, width=100)
    tree.column("Contact", anchor=CENTER, width=100)
    tree.column("Date Of Booking", anchor=CENTER, width=100)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Trans ID", text="Transaction ID", anchor=CENTER)
    tree.heading("Song ID", text="Song ID", anchor=CENTER)
    tree.heading("User Name", text="User Name", anchor=CENTER)
    tree.heading("Contact", text="Contact", anchor=CENTER)
    tree.heading("Date Of Booking", text="Date Of Booking", anchor=CENTER)

    if not res:
        messagebox.showinfo("Error", "No transactions found")
    else:
        for i in res:
            tree.insert(parent="", index="end", text="", values=i)
        tree.pack(fill="both", expand=True)
    button5=Button(show_transactions_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=admin_menu)
    button5.pack(pady=10)

#show all songs for user
def show_all_songs_user():
    user_f.pack_forget()
    for widget in show_all_songs_user_f.winfo_children():
        widget.destroy()
    show_all_songs_user_f.pack(expand=True, fill="both")

    sql = "SELECT * FROM song"
    cur.execute(sql)
    res = cur.fetchall()
    tree = ttk.Treeview(show_all_songs_user_f)
    tree['columns'] = ("Song ID", "Song Name", "Price", "Lyrics", "Genre")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Song ID", anchor=CENTER, width=50)
    tree.column("Song Name", anchor=CENTER, width=110)
    tree.column("Price", anchor=CENTER, width=50)
    tree.column("Lyrics", anchor=CENTER, width=50)
    tree.column("Genre", anchor=CENTER, width=50)

    tree.heading("#0", text="", anchor=CENTER)
    tree.heading("Song ID", text="Song ID", anchor=CENTER)
    tree.heading("Song Name", text="Song Name", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("Lyrics", text="Lyrics", anchor=CENTER)
    tree.heading("Genre", text="Genre", anchor=CENTER)

    if not res:
        messagebox.showinfo("Error", "No songs found")
    else:
        for i in res:
            tree.insert(parent="", index="end", text="", values=i)
        tree.pack(fill="both", expand=True)
    button5=Button(show_all_songs_user_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=user_menu)
    button5.pack(pady=10)

#claim song
def claim_song():
    user_f.pack_forget()
    for widget in user_f.winfo_children():
        widget.destroy()
    claim_song_f.pack(pady=10)

    label_sid = Label(claim_song_f, text="Enter the Song ID: ", bg="lightgreen", fg="black")
    label_sid.pack(pady=10)
    entry_sid = Entry(claim_song_f)
    entry_sid.pack(pady=10)

    label_un = Label(claim_song_f, text="Enter the User Name: ", bg="lightgreen", fg="black")
    label_un.pack(pady=10)
    entry_un = Entry(claim_song_f)
    entry_un.pack(pady=10)

    label_contact = Label(claim_song_f, text="Enter the Contact: ", bg="lightgreen", fg="black")
    label_contact.pack(pady=10)
    entry_contact = Entry(claim_song_f)
    entry_contact.pack(pady=10)

    def claim_song_db():
        sid = entry_sid.get()
        un = entry_un.get()
        contact = entry_contact.get()
        if (len(contact) != 10):
            messagebox.showinfo("Error", "Invalid contact number")
            return
        dob = dt.datetime.now().strftime("%Y-%m-%d")
        sql = "SELECT * FROM song WHERE sid = %s"
        val = (sid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Song not found")
        else:
            song_details = f"Song Name: {res[0][1]}\nPrice: {res[0][2]}"
            label_song_details = Label(claim_song_f)
            label_song_details.pack(pady=10)
            label_song_details.config(text=song_details)

            confirm = messagebox.askyesno("Confirm", "Do you want to claim the song?")
            if not confirm:
                user_menu()
                return
            sql = "INSERT INTO transaction(sid, pname, contact, dob) VALUES(%s, %s, %s, %s)"
            val = (sid, un, contact, dob)
            cur.execute(sql, val)
            conn.commit()
                
            sql = "SELECT tid FROM transaction WHERE sid = %s and pname = %s and contact = %s"
            val = (sid, un, contact)
            cur.execute(sql, val)
            res = cur.fetchall()
            messagebox.showinfo("Success", "Claimed song successfully. Transaction ID: "+ str(res[0][0]))

    submit_button = Button(claim_song_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=claim_song_db)
    submit_button.pack(pady=10)
    button5 = Button(claim_song_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=user_menu)
    button5.pack(pady=10)

#cancel song
def cancel_song():
    user_f.pack_forget()
    for widget in user_f.winfo_children():
        widget.destroy()
    cancel_song_f.pack(pady=10)

    label_tid = Label(cancel_song_f, text="Enter the Transaction ID: ", bg="lightgreen", fg="black")
    label_tid.pack(pady=10)
    entry_tid = Entry(cancel_song_f)
    entry_tid.pack(pady=10)

    def cancel_song_db():
        tid = entry_tid.get()
        sql = "SELECT * FROM transaction WHERE tid = %s"
        val = (tid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Transaction not found")
        else:
            confirm = messagebox.askyesno("Confirm", "Do you want to cancel the ticket?")
            if not confirm:
                user_menu()
                return
            sql = "DELETE FROM transaction WHERE tid = %s"
            val = (tid,)
            cur.execute(sql, val)
            conn.commit()
            messagebox.showinfo("Success", "Song purchase cancelled successfully")
    
    submit_button = Button(cancel_song_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=cancel_song_db)
    submit_button.pack(pady=10)
    button5 = Button(cancel_song_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=user_menu)
    button5.pack(pady=10)

#print receipt
def print_receipt():
    user_f.pack_forget()
    for widget in user_f.winfo_children():
        widget.destroy()
    print_receipt_f.pack(pady=10)

    label_tid = Label(print_receipt_f, text="Enter the Transaction ID: ", bg="lightgreen", fg="black")
    label_tid.pack(pady=10)
    entry_tid = Entry(print_receipt_f)
    entry_tid.pack(pady=10)

    def print_it():
        tid = entry_tid.get()
        sql = "SELECT * FROM transaction WHERE tid = %s"
        val = (tid,)
        cur.execute(sql, val)
        res = cur.fetchall()
        if not res:
            messagebox.showinfo("Error", "Transaction not found")
        else:
            sql = "SELECT t.tid, s.sname, t.pname, t.contact, t.dob FROM song as s, transaction as t WHERE tid = %s and t.sid = s.sid"
            val = (tid,)
            cur.execute(sql, val)
            res = cur.fetchall()

            label_tid = Label(print_receipt_f, text="Transaction ID: "+str(res[0][0]))
            label_tid.pack(pady=10)
            label_sname = Label(print_receipt_f, text="Song Name: "+str(res[0][1]))
            label_sname.pack(pady=10)
            label_uname = Label(print_receipt_f, text="User Name: "+str(res[0][2]))
            label_uname.pack(pady=10)
            label_contact = Label(print_receipt_f, text="Contact: "+str(res[0][3]))
            label_contact.pack(pady=10)
            label_dob = Label(print_receipt_f, text="Date of Booking: "+str(res[0][4]))
            label_dob.pack(pady=10)

    submit_button = Button(print_receipt_f, text="Submit", activebackground="lightgreen", activeforeground="black", command=print_it)
    submit_button.pack(pady=10)
    button5 = Button(print_receipt_f, text="Return Back", activebackground="lightgreen", activeforeground="black", command=user_menu)
    button5.pack(pady=10)

main_f=Frame(root)
main_f.pack(side="top", expand=True, fill="both")

button_create = Button(main_f, text="Admin Menu", activebackground="lightgreen", activeforeground="black", command=password_menu)
button_create.pack(pady=10)

button_create = Button(main_f, text="User Menu", activebackground="lightgreen", activeforeground="black", command=user_menu)
button_create.pack(pady=10, anchor=CENTER)

button_exit = Button(main_f, text="Exit", activebackground="lightgreen", activeforeground="black", command=exit_program)
button_exit.pack(pady=10, anchor=CENTER)
root.mainloop()
