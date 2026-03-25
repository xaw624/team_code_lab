

mi_lista = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrama1 = [x for x in mi_lista if sorted(x)==sorted("eat".lower())]

anagrama2 = [ x for x in mi_lista if sorted(x)==sorted("tan".lower())]

anagrama3 = [ x for x in mi_lista if sorted(x)==sorted("bat".lower())]

print(anagrama1)
print(anagrama2)
print(anagrama3)
