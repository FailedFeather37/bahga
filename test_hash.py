import string
import random
import sys


class ListChainee:
      def __init__(self):
          self.head=None

      #def modifier(self, cle, value):
      #instance = Cellule(cle, value)
      #self.next = self.head
      #self.head = instance


      def modifier(self, cle, value):
        instance = Cellule(cle, value)
        if self.head is None:
            self.head = instance
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = instance


      def supprimer(self,cle):
          if self.next!=None:
              while self.next==None:
                self.next=self.next.next
              self.head=self.head.next
          else:
               self.value=None
               self.next=None


      def longueur(self):
          count = 0
          current = self.head
          while current is not None:
              count += 1
              current = current.next
          return count


class Cellule:
      def __init__(self,cle,value):
          self.cle=cle
          self.value=value
          self.next=None



class Table_Hashage:
      def __init__(self,value=None):
          self.table=[ListChainee() for _ in range(8)]

      def __repr__(self):
          return(str(self.table))

      def modifier(self,cle,value):
          self.hash=hash(cle)
          self.hash=self.hash % 8
          self.table[self.hash].modifier(cle, value)

      def supprimer(self,cle):
          self.hash=hash(cle)
          self.hash=self.hash % 8
          self.table[self.hash].supprimer(cle)


      def recuperer(self,cle):
          hash_cle=hash(cle)
          hash_cle=hash_cle % 8
          print("fonction recuperer --> clé :", self.table[hash_cle].head.cle," value :",self.table[hash_cle].head.value)


      def longueur(self):
          for i, liste_chainee in enumerate(self.table):
              print(f"Longueur de la liste chainée {i}: {liste_chainee.longueur()}")


def remplissage_key():
    l=[]
    p=""
    for x in range(10000):
        for i in range(4):
            a=random.SystemRandom().choice(string.ascii_letters)
            p+=a
        l.append(p)
        p=""
    return(l)


def remplissage_value():
    l=[]
    p=""
    number_of_strings = 5
    for x in range(10000):
        a=random.SystemRandom().choice(string.digits)
        p+=a
        l.append(p)
        p=""
    return(l)


liste_exec_key=remplissage_key()
liste_exec_number=remplissage_value()
l1=Table_Hashage()
for i in range(len(liste_exec_key)):
    l1.modifier(liste_exec_key[i],liste_exec_number[i])
print(l1)
l1.longueur()