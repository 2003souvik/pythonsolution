class abc:
    def view(self):
        print("Hii")
class child(abc):
    def yoo(self):
      print("yoo")
ob=abc()
ob.view()
ob.yoo()
