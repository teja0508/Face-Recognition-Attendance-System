import yagmail
import os

receiver = "lchandratejareddy97@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-09-30_19-13-43.csv"  # attach the file

# mail information
yag = yagmail.SMTP("chandratejalattupally@gmail.com", "Chandra12")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
