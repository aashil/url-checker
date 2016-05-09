
# coding: utf-8

# In[30]:

import whois


# In[31]:

web_site = raw_input("Enter the website you wish to check: ")


# In[32]:

w = whois.whois(web_site)


# In[33]:

exp_date = w.expiration_date[1]


# In[34]:

print "This domain expires on " + str(exp_date)

