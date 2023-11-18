import re


class textcontrol():

    @staticmethod
    def create_framework(lucky_bags):
        with open('outputs.txt', 'a') as file:
            f = open('outputs.txt', 'r+')
            f.truncate(0)
            for i in range(0, lucky_bags):
                zeile = f'Luckybag {i+1}:\n'
                file.write(zeile)

    @staticmethod
    def add_data(line, text, id=None):
        file_path = 'outputs.txt'
        if id == None:
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
    def remove_data(line, id):
        file_path = 'outputs.txt'
        if id == None:
            raise ValueError
        # Lese alle Zeilen aus der Datei
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Überprüfe, ob die Zeile existiert
        if 1 <= line <= len(lines):
            # Suche nach Text in eckigen Klammern in der gewünschten Zeile und lösche ihn
            pattern = re.compile(rf'\[{id};.*?\]')
            lines[line - 1] = re.sub(pattern, '', lines[line - 1])

            # Schreibe alle aktualisierten Zeilen zurück in die Datei
            with open(file_path, 'w') as file:
                file.writelines(lines)
            print(
                f"Text in eckigen Klammern für Zeile {line} und ID {id} gelöscht.")
        else:
            print(f"Die Zeile {line} existiert nicht in der Datei.")


if __name__ == '__main__':
    textcontrol.create_framework(11)
    textcontrol.add_data(7, "Test")
    textcontrol.add_data(7, "Test")
    input()
    textcontrol.remove_data(7, 1)
