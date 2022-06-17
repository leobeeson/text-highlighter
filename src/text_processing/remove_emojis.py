def remove_emojis(text: str, emojis_to_remove: list[str]) -> str:
    for emoji in emojis_to_remove:
        while True:
            emoji_position = text.find(emoji)
            if emoji_position == -1:
                break
            text = text[:emoji_position] + text[emoji_position + 1:]
    return text
