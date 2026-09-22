def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]