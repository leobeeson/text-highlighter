import re


def remove_emojis(text: str, emojis_to_remove: list[str]) -> str:    
    pattern: str = convert_emojis_to_unicode(emojis_to_remove)
    clean_text: str = re.sub(pattern, "", text)
    return clean_text


def convert_emojis_to_unicode(emojis_to_remove: list[str]) -> str:
    unicodes: str = "|".join([emoji.encode("unicode-escape").decode("ASCII") for emoji in emojis_to_remove])
    pattern: str = f"[{unicodes}]"
    return pattern
