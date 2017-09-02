# Python Email Slicer Program

# get user email address
userInput = input("Enter your email address?: ").strip()

# slice out the user name
userName = userInput[:userInput.index("@")]

# slice out the domain name
domainName = userInput[userInput.index("@")+1:userInput.index(".")]

# format the message
output = "User name = %s"
         "Domain name = %s" % (userName,domainName)

# display output message
print(output)
