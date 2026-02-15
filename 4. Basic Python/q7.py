class StrMpl:
    def get_String(self):
        self.text=input("Enter string: ")

    def prnt_Text(self):
        print(self.text.upper())

obj=StrMpl()
obj.get_String()
obj.prnt_Text()