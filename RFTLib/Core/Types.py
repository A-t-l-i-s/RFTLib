import os
import types
import typing

from .Object import *





__all__ = ("RFT_Types", "RFT_Typing")





class RFT_Types(RFT_Object):
	Union = 		types.UnionType


	Path = 			str | os.PathLike
	Array =			tuple | list
	Iterable = 		Array | range
	Group = 		Iterable | Union
	Number = 		int | float | complex
	Buffer = 		bytes | bytearray | memoryview
	Dictionary = 	dict | map









class RFT_Typing(RFT_Object):
	Any = 			typing.Any
	List = 			typing.List
	Tuple = 		typing.Tuple
	Union = 		typing.Union


	Path = 			typing.NewType("Path",RFT_Types.Path)
	Array = 		typing.NewType("Array",RFT_Types.Array)
	Iterable = 		typing.NewType("Iterable",RFT_Types.Iterable)
	Group = 		typing.NewType("Group",RFT_Types.Group)
	Number = 		typing.NewType("Number",RFT_Types.Number)
	Buffer = 		typing.NewType("Buffer",RFT_Types.Buffer)
	Dictionary = 	typing.NewType("Dictionary",RFT_Types.Dictionary)




