class A:
      wt=60
      
      def __init__(self,wt):
                  self.wt=wt
                  

class B(A):
      ht=6
      def __init__(self, wt):
              super().__init__(wt)


