from Globals import *
import Element

elem1 = Element.Element(ElementState.dead, (0, 0))
elem2 = Element.Element(ElementState.dead, (0, 1))

elems = {

	id(elem1): elem1,
	id(elem2): elem2


}

for elemId, elem in elems.items():
	print(elemId, elem)