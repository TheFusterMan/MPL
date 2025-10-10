import re

class JsToPythonTranslator:
    def __init__(self):
        self.current_context_nesting = 0

    def getIndent(self):
        return "    " * self.current_context_nesting

    def translate(self, code_to_translate):
        lines_to_translate = code_to_translate.splitlines()
        translated_lines = []

        for line in lines_to_translate:
            # === Работа с функциями ===
            line = line.strip()

            # function (args) {
            match = re.match(r'^function\s{1}(\w+)\((.*?)\)\s{1}\{$', line)
            if match:
                func_name = match.group(1)
                func_args = match.group(2)

                translated_lines.append(f"{self.getIndent()}def {func_name}({func_args}):")
                self.current_context_nesting += 1
                continue

            # this - трудно реализовать                                                     :-(
            # match = re.match(r'^this\.(\w+)\s{1}\=\s{1}(.+?)\;$', line)
            # if match:
            #     var_name = match.group(1)
            #     var_value = match.group(2)
            #
            #     translated_lines.append(f"{self.getIndent()}self.{var_name} = {var_value}")
            #     continue

            # return
            match = re.match(r'^return\s{1}(.+?)\;$', line)
            if match:
                return_val = match.group(1)

                translated_lines.append(f"{self.getIndent()}return {return_val}")
                continue

            # }
            match = re.match(r'^\}$', line)
            if match:
                self.current_context_nesting -= 1
                continue

            # === Работа с переменными ===

            # let
            match = re.match(r'^let\s{1}(\w+)\s{1}\=\s{1}(.+?)\;$', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2)

                translated_lines.append(f"{self.getIndent()}{var_name} = {var_value}")
                continue

            # +=
            match = re.match(r'^(\w+)\s{1}\+\=\s{1}(.+?)\;$', line)
            if match:
                var_name = match.group(1)
                var_value = match.group(2)

                translated_lines.append(f"{self.getIndent()}{var_name} +=  {var_value}")
                continue

            # === Арифметический цикл ===
            match = re.match(r'^for \(let (\w+)\s{1}\=\s{1}(.+?)\;\s{1}\1\s{1}\<\s{1}(.+?)\;\s{1}\1\+\+\)\s{1}\{$', line)
            if match:
                var_name = match.group(1)
                start_value = match.group(2)
                end_value = match.group(3)

                translated_lines.append(f"{self.getIndent()}for {var_name} in range({start_value}, {end_value}):")
                self.current_context_nesting += 1
                continue

            # === Условный оператор ===

            # if
            match = re.match(r'^if\s{1}\((.+?)\)\s{1}\{$', line)
            if match:
                condition = match.group(1)

                translated_lines.append(f"{self.getIndent()}if {condition}:")
                self.current_context_nesting += 1
                continue

            # else
            match = re.match(r'^else\s{1}\{$', line)
            if match:
                translated_lines.append(f"{self.getIndent()}else:")
                self.current_context_nesting += 1
                continue

            # === Вывод ===
            match = re.match(r'^console\.log\((.+?)\)\;$', line)
            if match:
                text = match.group(1)

                translated_lines.append(f"{self.getIndent()}print({text})")
                continue

            # пустая строка / невалиднаня => пропускаем
            translated_lines.append("")

        self.printToFile(translated_lines)

    def printToFile(self, translated_code):
        with open('translated.py', 'w') as file:
            file.write("\n".join(translated_code))


if __name__ == '__main__':
    with open("input.js", 'r', encoding="utf-8") as f:
        code = f.read()

        translator = JsToPythonTranslator()
        translator.translate(code)

        print("Результирующий перевод сохранен в файл translated.py")