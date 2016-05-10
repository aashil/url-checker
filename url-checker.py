import whois

web_site = raw_input("Enter the website you wish to check: ")
w = whois.whois(web_site)
exp_date = w.expiration_date[1]
print "This domain expires on " + str(exp_date)

