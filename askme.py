def askMe():
  name = input("Hi there, whats your name? ")
  
  place = input("Nice to meet you " + name
                + " and where are you from? ")
  
  age = input("Cool, I always fancied visiting " + place
              + ". So how old are you anyway? ")
  
  foo = "bar"
  print("Wow so you're " + age
        + " years old and from " + place
        + " and your name is " + name
        + ". Pretty neat!")
  

askMe()
