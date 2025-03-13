def spr1(dane: str) -> str:
   if dane and isinstance(dane[0], str) and dane[0].isdigit():
      return True
   else:
      return False

def spr2(dane: str) -> str:
   if dane and dane[0].isdigit():
      return True
   else:
      return False

if __name__ == '__main__':
   dane = input("Podaj dowolny znak: ")
   
   if spr1(dane):
      print("Znak jest liczbą")
   else:
      print("Znak nie jest liczbą")

   if spr2(dane):
      print("Znak jest liczbą")
   else:
      print("Znak nie jest liczbą")