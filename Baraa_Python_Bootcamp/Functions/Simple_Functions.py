# Task:
# Build an application where:
# 1. Receive an email from the user
# 2. Validate the email
# 3. If it is invalid, Log an error in a file.
# 4. If it is valid, Clean and Structure the email.
# 5. Log each step of the program

# Action Function
def write_log(message):
    # Task: Store application log messages in a file in drive E
    with open(r"E:\2026_Courses\12_Python\Baraa_Python_Bootcamp\Mini_Function_Project\app.log", "a") as file:
        file.write(message + "\n")
        
# Validation Function
def is_valid_email(email):
    return "@" in email and "." in email

# Transformation Function
def clean_and_split_email(email):
    #Task: Clean an email and split it into username and domain
    cln_email = email.strip().lower()
    username, domain = email.split("@")
    return {"username": username, 
            "domain": domain
            }

# Orchestrator Function
def process_user_email(email):
    write_log("App Started")
    # We receive an email from a user
    #email = input("Please enter Your Email: ")
    # We must check if it is valid
    #is_valid_email(email)
    # If it is not valid, we log the problem
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    # If it is valid, we clean it and store structured information
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("App Stopped")
    # And, we log what happened
 
# We receive an email from a user   
email = input("Please enter Your Email: ")
process_user_email(email)     


