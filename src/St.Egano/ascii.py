def ascii_convert(number):
    try:
        # Konvertiere die Zahl in ein einzelnes Zeichen
        text = chr(number)
        return text
    except ValueError as e:
        # Behandle den Fall, wenn die Zahl nicht gültig ist
        return f"Fehler: {e}"
