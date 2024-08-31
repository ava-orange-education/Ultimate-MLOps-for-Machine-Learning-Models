# Function to split email-id and mask first part
def mask_email(email):
    local_part, domain = email.split('@')
    masked_local = local_part.replace(local_part, len(local_part)*"*")
    return f"{masked_local}@{domain}"

# Let's try out the function
email = "john.doe@example.com"
masked_email = mask_email(email)
print(f"Original email: {email}")
print(f"Masked email: {masked_email}")

