def capital_indexes(string):
  
  indexes = []
  
  for i, s in enumerate(string):
      if s.isupper():
          indexes.append(i)
          
  print(indexes)
    
capital_indexes("HeLlO")    
