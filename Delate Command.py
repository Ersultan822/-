class TextEditor:
    def __init__(self):
        self.text = input("Введите текст редактора: ")
        self.selection = ""

    def select_text(self, text):
        self.selection = text

    def delete(self):
        print(f"Удалено: '{self.selection}'")
        self.text = self.text.replace(self.selection, "")
        print(f"Текущий текст: '{self.text}'")

class DeleteCommand:
    def __init__(self, editor):
        self.editor = editor
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.editor.selection
        self.editor.delete()

    def undo(self):
        print("Отмена удаления")
        self.editor.text += self.deleted_text
        print(f"Текущий текст: '{self.editor.text}'")

if __name__ == "__main__":
    editor = TextEditor()
    selection_text = input("Введите текст для удаления: ")
    editor.select_text(selection_text)
    delete_cmd = DeleteCommand(editor)
    delete_cmd.execute()
    delete_cmd.undo()
