from abc import ABC, abstractmethod

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class TextEditor:
    def __init__(self):
        self.text = ""
        self.selection = ""
        self.clipboard = ""

    def select_text(self, text):
        self.selection = text
        print(f"Выделено: '{self.selection}'")

    def copy(self):
        self.clipboard = self.selection
        print(f"Скопировано: '{self.clipboard}'")

    def paste(self):
        self.text += self.clipboard
        print(f"Вставлено: '{self.clipboard}'")
        print(f"Текущий текст: '{self.text}'")

    def delete(self):
        print(f"Удалено: '{self.selection}'")
        self.text = self.text.replace(self.selection, "")
        print(f"Текущий текст: '{self.text}'")

    def format(self, style):
        print(f"Отформатировано '{self.selection}' в {style}")

class CopyCommand(ICommand):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.copy()

    def undo(self):
        print("Отмена копирования")
        self.editor.clipboard = ""

class PasteCommand(ICommand):
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

class DeleteCommand(ICommand):
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

class FormatCommand(ICommand):
    def __init__(self, editor, style):
        self.editor = editor
        self.style = style

    def execute(self):
        self.editor.format(self.style)

    def undo(self):
        print(f"Отмена форматирования '{self.editor.selection}'")

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Нечего отменять")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
        else:
            print("Нечего повторять")

if __name__ == "__main__":
    editor = TextEditor()
    manager = CommandManager()

    while True:
        print("\nВыберите команду:")
        print("1. Copy")
        print("2. Paste")
        print("3. Delete")
        print("4. Format")
        print("5. Undo")
        print("6. Redo")
        print("0. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            text = input("Введите текст для выделения: ")
            editor.select_text(text)
            manager.execute_command(CopyCommand(editor))

        elif choice == "2":
            if not editor.clipboard:
                editor.clipboard = input("Буфер пуст. Введите текст для буфера: ")
            manager.execute_command(PasteCommand(editor))

        elif choice == "3":
            text = input("Введите текст для удаления: ")
            editor.select_text(text)
            manager.execute_command(DeleteCommand(editor))

        elif choice == "4":
            text = input("Введите текст для форматирования: ")
            editor.select_text(text)
            style = input("Введите стиль (жирный/курсив/размер шрифта): ")
            manager.execute_command(FormatCommand(editor, style))

        elif choice == "5":
            manager.undo()

        elif choice == "6":
            manager.redo()

        elif choice == "0":
            print(f"Текущий текст: '{editor.text}'")
            break

        else:
            print("Некорректный выбор")
