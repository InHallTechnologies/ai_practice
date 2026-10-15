from pydantic import BaseModel, Field

class TextInfoParser(BaseModel):
    num_vowels:int = Field(description="This represents the number of vowels in int format")
    num_consonants: int = Field(description="This represents the number of consonants in int format") 
    vowels:list[str] = Field(description="This contains a list of vowels")
    consonants:list[str] = Field(description="This contains a list of consonants")

    def __str__(self):
        return f"""
            num of vowels: {self.num_vowels}\n
            num of consonants: {self.num_vowels}\n
            vowels: {self.vowels}\n
            consonants: {self.consonants}\n
        """