# andela-lite-exercises

# notes

Inheritance:
- An "__init__" function when inheriting should follow this example;
       * super class situation

               class confined(object):
                    def __init__(c, d, e):
                      self.c = c
                      self.d = d
                      self.e = e
               class free(confined):
                    def __init__(a, b, c, d, e):
                      super(free, user).__init__(c, d, e)
                      self.a = a
                      self.b = b
