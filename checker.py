import re
REQUIRED_FIELDS = {
    "Name": [
        r"\bname\b",
        r"\bfull name\b"
    ],
    "Email": [
        r"\bemail\b",
        r"\be-mail\b"
    ],
    "Phone Number": [
        r"\bphone\b",
        r"\bmobile\b",
        r"\bcontact number\b"
    ],
    "Address": [
        r"\baddress\b"
    ],
    "Education": [
        r"\beducation\b",
        r"\bqualification\b",
        r"\bdegree\b"
    ],
    "Skills": [
        r"\bskills\b",
        r"\btechnical skills\b"
    ],
    "Experience": [
        r"\bexperience\b",
        r"\bwork experience\b"
    ]
}
def check_missing_information(text):
    """
    Checks which required fields are present
    and which fields are missing.
    """
    text = text.lower()
    found_fields = []
    missing_fields = []
    for field, patterns in REQUIRED_FIELDS.items():
        found = False
        for pattern in patterns:
            if re.search(pattern, text):
                found = True
                break
        if found:
            found_fields.append(field)
        else:
            missing_fields.append(field)
    return found_fields, missing_fields