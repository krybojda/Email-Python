import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox

temat = 'TEST'
var = 100
message = f"Witaj!\n\nTo jest przykładowa wiadomość e-mail. Zmienna wynosi: {var}."

# Dane do logowania do serwera SMTP
smtp_server = 's1.ct8.pl'
smtp_port = 587
smtp_username = '...'
smtp_password = '...'


def wykonaj():
    print("Wiadomość zostanie wysłana do: "+jakimail.get())
    print("Ilość: "+ile.get())
    ilosc = int(ile.get())
    adres = jakimail.get()
    for i in range(ilosc):
        print(i+1)
    
        #send_email(adres, temat, message)  #tresc ze zmiennej
        send_email(adres, temat, message2) #tresc z pliku

    window.destroy()



window = tk.Tk()
window.title("Program do wysyłania e-maila")
window.geometry("350x200")
window.maxsize(350, 200)
window.configure(background='lightblue')


title = tk.Label(window, text="Wysyłanie e-maili", font=("Times_New_Roman, 15"), bg="lightblue")
title.grid(column=0, row=0, padx=20, pady=20, columnspan=4)

nazwa1 = tk.Label(window, text="E-mail:", anchor="w", justify="left", width=8, font=("Arial, 14"), bg="lightblue")
nazwa1.grid(column=1, row=1, padx=0, pady=5, sticky=tk.W)

jakimail = StringVar()
mail = tk.Entry(window, width=20, textvariable=jakimail, font=("Arial, 14"))
mail.grid(column=2, row=1, padx=0, pady=5)

nazwa2 = tk.Label(window, text="Ile:", anchor="w", justify="left", width=8, font=("Arial, 14"), bg="lightblue")
nazwa2.grid(column=1, row=2, padx=0, pady=5, sticky=tk.W)

ile = StringVar()
ilerazy = tk.Entry(window, width=3, textvariable=ile, font=("Arial, 14"))
ilerazy.grid(column=2, row=2, padx=0, pady=5, sticky=tk.W)

przycisk= tk.Button(window, text="Wyślij", width=10, height=1, command=wykonaj)
przycisk.grid(column=0, row=3, columnspan=2, padx=15, pady=10, sticky=tk.EW)


def send_email(to_email, subject, message):

    # Tworzenie wiadomości e-mail
    from_email = smtp_username
    email_body = f"Subject: {subject}\n\n{message}"

    try:
        # Logowanie do serwera SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)

            # Wysyłanie wiadomości
            server.sendmail(from_email, to_email, email_body.encode('utf-8'))
            print("Wiadomość e-mail została wysłana!")

            
    except Exception as e:
        print("Wystąpił błąd podczas wysyłania wiadomości e-mail.")
        print(e)


## Wczytywanie treści wiadomości z pliku
tresc_plik = 'tresc.txt'  # ścieżka do pliku z treścią wiadomości
with open(tresc_plik, 'r', encoding='utf-8') as file:
    message2 = file.read()


window.mainloop()




