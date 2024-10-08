import re


def is_email(email):
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def remove_duplicate_companies(companies):
    normalized = []

    for company in companies:
        # Capitalize first letter of each word
        normalized_name = " ".join([x.capitalize() for x in company.split(" ")])

        if normalized_name not in normalized:
            normalized.append(normalized_name)

    return normalized


def validate_format(input_string: str):
    commands = set(["refer me", "i can refer"])
    if input_string in commands:
        return True, "Special options provided."

    parts = input_string.split(",")

    if len(parts) != 2:
        return (
            False,
            "Input should contain exactly one comma separating 'Company' and 'Position'.",
        )

    company, position = parts
    company = company.strip()
    position = position.strip()

    if not company or not position:
        return False, "Both 'Company' and 'Position' must be provided."

    return True, "Format is correct."
