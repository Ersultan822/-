class TextEditor:
    def __init__(self):
        self.selection = input("Введите текст для форматирования: ")

    def format(self, style):
        print(f"Отформатировано '{self.selection}' в {style}")

class FormatCommand:
    def __init__(self, editor, style):
        self.editor = editor
        self.style = style

    def execute(self):
        self.editor.format(self.style)

    def undo(self):
        print(f"Отмена форматирования '{self.editor.selection}'")

if __name__ == "__main__":
    editor = TextEditor()
    style = input("Введите стиль форматирования (жирный/курсив/размер шрифта): ")
    format_cmd = FormatCommand(editor, style)
    format_cmd.execute()
    format_cmd.undo()
