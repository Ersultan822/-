class TextEditor:
    def __init__(self):
        self.clipboard = ""
        self.selection = ""

    def select_text(self, text):
        self.selection = text
        print(f"Выделено: '{self.selection}'")

    def copy(self):
        self.clipboard = self.selection
        print(f"Скопировано: '{self.clipboard}'")

class CopyCommand:
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy()

    def undo(self):
        print("Отмена копирования")
        self.editor.clipboard = ""

if __name__ == "__main__":
    editor = TextEditor()
    text = input("Введите текст для выделения: ")
    editor.select_text(text)
    copy_cmd = CopyCommand(editor)
    copy_cmd.execute()
    copy_cmd.undo()
