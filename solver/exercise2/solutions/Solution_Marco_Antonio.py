

mi_lista = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrama1 = [print (x) for x in mi_lista if sorted(x.lower())==sorted("eat".lower())]

anagrama2 = [print (x) for x in mi_lista if sorted(x.lower())==sorted("tan".lower())]

anagrama3 = [print (x) for x in mi_lista if sorted(x.lower())==sorted("bat".lower())]

