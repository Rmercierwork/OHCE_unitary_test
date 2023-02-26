import datetime

class OHCE:
    def __init__(self):
        self._now = datetime.datetime.now()

    def set_time(self, time_str):
        self._now = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

    def greeting(self):
        hour = self._now.hour
        if 5 <= hour < 12:
            greeting = "Bonjour, vous vous levez tôt"
        elif 12 <= hour < 18:
            greeting = "Bonjour"
        elif 18 <= hour < 22:
            greeting = "Bonsoir, ne travaillez pas trop longtemps"
        else:
            greeting = "Vous êtes toujours réveillé ? Pensez à aller dormir"
        return greeting

    def is_palindrome(self, text):
        text = text.replace(" ", "").lower()
        return text == text[::-1]

    def reverse_text(self, text):
        return text[::-1]

    def goodbye(self):
        now = datetime.datetime.now()
        hour = now.hour
        if 5 <= hour < 12:
            goodbye = "Bonne journée"
        elif 12 <= hour < 18:
            goodbye = "Bonne après-midi"
        elif 18 <= hour < 22:
            goodbye = "Bonne soirée"
        else:
            goodbye = "Bonne nuit. Vous allez enfin dormir :)"
        return goodbye

    def run(self):
        print(self.greeting())
        text = input("Entrez un texte : ")
        reversed_text = self.reverse_text(text)
        if self.is_palindrome(text):
            print("Bien dit !")
        print("Le texte renversé est : ", reversed_text)
        print(self.goodbye())

if __name__ == "__main__":
    ohce = OHCE()
    ohce.run()
