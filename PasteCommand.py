class TextEditor:
    def __init__(self):
        self.text = ""
        self.clipboard = ""

    def set_clipboard(self, text):
        self.clipboard = text

    def paste(self):
        self.text += self.clipboard
        print(f"Вставлено: '{self.clipboard}'")
        print(f"Текущий текст: '{self.text}'")

class PasteCommand:
    def __init__(self, editor):
        self.editor = editor
        self.pasted_text = ""

    def execute(self):
        self.pasted_text = self.editor.clipboard
        self.editor.paste()

    def undo(self):
        print("Отмена вставки")
        self.editor.text = self.editor.text.replace(self.pasted_text, "")
        print(f"Текущий текст: '{self.editor.text}'")

if __name__ == "__main__":
    editor = TextEditor()
    clipboard_text = input("Введите текст в буфер для вставки: ")
    editor.set_clipboard(clipboard_text)
    paste_cmd = PasteCommand(editor)
    paste_cmd.execute()
    paste_cmd.undo()
