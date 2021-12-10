import smtplib #library responsible for configuring the emial's credentials
import email.message 

""" IMPORTANT: 
gmail is a very secure tool. It prevents you from receiving code-sent emails.
For this script to work, you must enable the less secure app access option in your g-mail"""

def enviar_email():
    #body of the email you are going to write. Note that this is an HTML
    email_body = f"""
    <p>Hello,</p>  
    <p>this is a small Python project done through some research.</p>
    """
    #create email struct
    msg = email.message.Message()
    msg['Subject'] = "Email automation"
    msg['From'] = 'davypedro@mat.ci.ufpb.br'
    msg['To'] = 'davypedro@mat.ci.ufpb.br'
    password = 'write_your_password_here' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    #configuring gmail server properties
    server = smtplib.SMTP('smtp.gmail.com: 587') 
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    server.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Your email has been sent successfully')

#function call
enviar_email()

