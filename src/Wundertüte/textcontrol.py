# in textcontrol.py
import re


class TextControl():
    @staticmethod
    def create_framework(lucky_bags):
        with open('output.txt', 'a') as file:
            f = open('output.txt', 'r+')
            f.truncate(0)
            for i in range(0, lucky_bags):
                zeile = f'Luckybag {i+1}:\n'
                file.write(zeile)

    @staticmethod
    def add_data(line, text, id=None):
        file_path = "output.txt"

        if id is None:
            raise ValueError('Invalid ID')
        # Lese alle Zeilen aus der Datei
        with open(file_path, 'r') as file:
            lines = file.readlines()

        text = f"[{id};{text}]"

        lines[line - 1] = lines[line - 1].rstrip('\n') + ' ' + text + '\n'

        # Schreibe alle aktualisierten Zeilen zurück in die Datei
        with open(file_path, 'w') as file:
            file.writelines(lines)

    @staticmethod
    def remove_data(id):
        file_path = "output.txt"
        if id is None:
            raise ValueError

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            pattern = re.compile(rf'\[{id};.*?\]')
            lines[i] = re.sub(pattern, '', line)

        with open(file_path, 'w') as file:
            file.writelines(lines)

    @staticmethod
    def get_line_data(line):
        file_path = "output.txt"
        # Lese alle Zeilen aus der Datei
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Überprüfe, ob die Zeile existiert
        if 1 <= line <= len(lines):
            # Suche nach Text in eckigen Klammern in der gewünschten Zeile
            data_in_brackets = re.findall(r'\[\d+;(.*?)\]', lines[line - 1])

            # Gib das gefundene Daten-Array zurück
            return data_in_brackets
        else:
            return None

    @staticmethod
    def get_id_for_data_in_line(line, data):
        file_path = "output.txt"
        # Lese alle Zeilen aus der Datei
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Überprüfe, ob die Zeile existiert
        if 1 <= line <= len(lines):
            # Suche nach der ID für den angegebenen Text in eckigen Klammern in der gewünschten Zeile
            pattern = re.compile(rf'\[(\d+);{re.escape(data)}\]')
            match = re.search(pattern, lines[line - 1])

            # Wenn ein Übereinstimmung gefunden wurde, gib die ID zurück
            if match:
                return int(match.group(1))
            else:
                return None
        else:
            return None

    @staticmethod
    def replace_data(id, new_text):
        file_path = "output.txt"
        # Lese alle Zeilen aus der Datei
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Durchsuche alle Zeilen nach dem Text in eckigen Klammern
        for line_num, line in enumerate(lines, start=1):
            pattern = re.compile(rf'\[{id};.*?\]')
            match = re.search(pattern, line)

            # Wenn eine Übereinstimmung gefunden wurde, ersetze den Text
            if match:
                lines[line_num - 1] = re.sub(pattern,
                                             f"[{id};{new_text}]", line)
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                return
