class Facts:
    def __init__(self):
        self.facts = {}
    def add(self, fact, x):
        if fact not in self.facts:
            self.facts[fact] = {x}
        else: self.facts[fact].add(x)
    def includes(self,fact,x):
        return x in self.facts[fact] 
    def __getitem__(self, x):
        return self.facts[x]

facts = Facts()
facts.add('man', 'socrates')

def mortal(x):
    if facts.includes("man","socrates"):
        return True
    return False
print(mortal("socrates"))