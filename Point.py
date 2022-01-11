class Point:
   def __init__(self, name, latitute, longitude):
      if(type(name) is not str):
         raise ValueError("City name should be String")
      self.name = name
      if (10 > latitute < 0 or
      20 > longitude < 10):
         raise ValueError("ValueError")
      self.latitute = latitute
      self.longitude = longitude


   def get_lan_long(self):
      return (self.latitute, self.longitude)