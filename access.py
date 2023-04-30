import gspread
from oauth2client.service_account import ServiceAccountCredentials

myscope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    mycreds = ServiceAccountCredentials.from_json_keyfile_name('loyal-prism-385305-06dae9dd18f6.json', myscope)

    myclient = gspread.authorize(mycreds)



    mysheet = myclient.open(sh1).worksheet(sh2)
    # l1 = ["e1@example.com", "e2@example.com", "e3@example.com"]
    l2 = get_email_list(mysheet)
    # print(l2)
    l3 = compare_emails(l1, l2)