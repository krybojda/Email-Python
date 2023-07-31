import smtplib

temat = 'TEST'
var = 100
message = f"Witaj!\n\nTo jest przykładowa wiadomość e-mail. Zmienna wynosi: {var}."

def send_email(to_email, subject, message):
    # Dane do logowania do serwera SMTP
    smtp_server = 's1.ct8.pl'
    smtp_port = 587
    smtp_username = '...'
    smtp_password = '...'

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


## Wysyłanie emaili ze zmiennych
z_listy = ['email1@gmail.com',  'email2@gmail.com', 'email3@gmail.com']

## Wczytywanie listy e-maili z pliku
email_plik = 'plik.txt'
with open(email_plik, 'r') as file:
    z_pliku = file.read().splitlines()

## Wczytywanie treści wiadomości z pliku
tresc_plik = 'tresc.txt'  # ścieżka do pliku z treścią wiadomości
with open(tresc_plik, 'r', encoding='utf-8') as file:
    message2 = file.read()

#send_email(z_listy, temat, message)  #tresc ze zmiennej, emaile z listy
#send_email(z_listy, temat, message2) #tresc z pliku, emaile z listy
#send_email(z_pliku, temat, message)  #tresc ze zmiennej, email z pliku
send_email(z_pliku, temat, message2) #tresc z pliku, emaile z pliku


