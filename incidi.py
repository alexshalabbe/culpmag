   def aTag(index):
       return f'<a href="#">Link {index}</a>'

   result = ''
   for i in range(5):
       result += aTag(i)

   print(result)
   