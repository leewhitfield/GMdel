import imaplib, sys # imaplib for connecting to the webmail, sys for getting command-line arguments

eaddress = raw_input('Enter your email address: ') # Get the login information
epassword = raw_input('Enter your password: ')
idprefix = '(HEADER Message-ID "<' # This must be added to the start of the Msg-ID
idsuffix = '>")' # This must be added to the end of the Msg-ID
infile = open(sys.argv[1],'r') # Open the text file specified in the command line
imap = imaplib.IMAP4_SSL('imap.gmail.com',993) # Connect to the IMAP server
imap.login(eaddress, epassword)
imap.select('"[Gmail]/All Mail"') # Selects all mail, regardless of label/folder structure
for line in infile:
    line = line.replace("\n", "") # Remove the carriage return at the end of the imported string
    print(idprefix+line+idsuffix)
    typ, data = imap.search(None, idprefix+line+idsuffix) # Search for the Msg-ID from the current line of the file and move it to the trash.
    if data != ['']:
        imap.store(data[0], '+X-GM-LABELS', '\\Trash')
    else:
        print("Nothing to remove.")
infile.close
m.select('[Gmail]/Trash')  # Select all trash
m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
imap.expunge() # Commit all changes
imap.close()
imap.logout()