
class newfile:

    def __init__(self, location:str):
        self.location = location
        try:
            with open(self.location, "r") as file:
                file.read()
        except FileNotFoundError:
            with open(self.location, "w") as file:
                file.write("0")

    def read(self,size=None):
        with open(self.location, "r") as file:
            string = file.read(size)
        return string
    
    def readline(self, size=None):
        if size==None:
            with open(self.location, "r") as file:
                string = file.readline()
        else:
            with open(self.location, "r") as file:
                string = file.readline(size)
        return string
    
    def readlines(self, size=None) -> list:
        if size==None:
            with open(self.location, "r") as file:
                list = file.readlines()
        else:
            with open(self.location, "r") as file:
                list = file.readlines(size)
        return list
    
 
    def write(self, content:str, mode:str):
        """
        content: what to append or overwrite
        mode: "a" for append or "w" for overwriting
        """
        with open(self.location, mode) as file:
            file.write(content)
    
    def writelines(self, content:list, mode:str):
        """
        content: list to append or overwrite
        mode: "a" for append or "w" for overwriting
        """
        with open(self.location, mode) as file:
            file.writelines(content)

    #add readlines writelines

    def uniqueChars(self)->int:
        """
        Returns number of unique
        characters in a file
        excluding \\n
        """
        uniquechar = ""
        uniquechars=int(0)
        with open(self.location,"r") as file:
            string = file.read()
            for char in string:
                if char not in uniquechar and char != "\n":
                    uniquechar+=char
                    uniquechars+=1
        return uniquechars
    
if __name__ == "__main__":
    file = newfile("C:\\Users\\hthur\\OneDrive\\Documents\\quadratic formula node 2.txt")
    print(file.readlines())