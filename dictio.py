


class ListChainee:
      def __init__(self):
          self.head=None


      def modifier(self,cle,value):
          instance=Cellule(cle,value)
          self.next=self.head
          self.head=instance


      def supprimer(self,cle):
          if self.next!=None:
              while self.next==None:
                self.next=self.next.next
              self.head=self.head.next
          else:
               self.value=None
               self.next=None



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



if __name__ == '__main__':
   l1=Table_Hashage()
   l1.modifier("ah",5)
   l1.modifier("ah",7)
   l1.recuperer("ah")
   l1.supprimer("ah")
   print(l1)

