# send_mail
You can send email using python

If you get smtplib.SMTPServerDisconnected Error, login to your gmail, go to account settings, security tab,
Scroll down to Signing in to Google section, turn off the 2-Step verification and use your phone to sign in to OFF.
Scroll down to bottom Less Secure App Access and set it to ON

If still getting SMTP error, try adding port number ib the code:
connection = smtplib.SMTP("smtp.gmail.com", port=587)

Also each domain has different account security settings and smtp string  ex: for yahoo,  (smtp.mail.yahoo.com),
for hotmail, (smtp.live.com).
