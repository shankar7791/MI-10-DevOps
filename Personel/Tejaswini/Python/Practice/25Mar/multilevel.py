class MusicalInstrument:
    num_of_major_keys = 12
 
 
class StringInstrument(MusicalInstrument):
    type_of_wood = 'Tonewood'
 
 
class Guitar(StringInstrument):
    def __init__(self):
        self.num_of_strings = 6
        print(f"\nThe guitar consists of {self.num_of_strings} strings," +
              f"it is made of {self.type_of_wood} and can play {self.num_of_major_keys} keys.\n")
 
guitar = Guitar()