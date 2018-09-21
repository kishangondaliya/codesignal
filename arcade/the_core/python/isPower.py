def isPower(n):
   i = 2
   if n == 1:
      return True
   while i < 1000:
      z = i
      while z < n:
         z *= i
         if z == n:
            return True
      i += 1
   return False
