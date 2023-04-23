from ..Require import *

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
	Module = 		types.ModuleType









class RFT_Typing(RFT_Object):
	Annotated = 				typing.Annotated
	Any = 						typing.Any
	Callable = 					typing.Callable
	ClassVar = 					typing.ClassVar
	Concatenate = 				typing.Concatenate
	Final = 					typing.Final
	ForwardRef = 				typing.ForwardRef
	Generic = 					typing.Generic
	Literal = 					typing.Literal
	Optional = 					typing.Optional
	ParamSpec = 				typing.ParamSpec
	Protocol = 					typing.Protocol
	Tuple = 					typing.Tuple
	Type = 						typing.Type
	TypeVar = 					typing.TypeVar
	TypeVarTuple = 				typing.TypeVarTuple
	Union = 					typing.Union

	AbstractSet = 				typing.AbstractSet
	ByteString = 				typing.ByteString
	Container = 				typing.Container
	ContextManager = 			typing.ContextManager
	Hashable = 					typing.Hashable
	ItemsView = 				typing.ItemsView
	Iterable = 					typing.Iterable
	Iterator = 					typing.Iterator
	KeysView = 					typing.KeysView
	Mapping = 					typing.Mapping
	MappingView = 				typing.MappingView
	MutableMapping = 			typing.MutableMapping
	MutableSequence = 			typing.MutableSequence
	MutableSet = 				typing.MutableSet
	Sequence = 					typing.Sequence
	Sized = 					typing.Sized
	ValuesView = 				typing.ValuesView
	Awaitable = 				typing.Awaitable
	AsyncIterator = 			typing.AsyncIterator
	AsyncIterable = 			typing.AsyncIterable
	Coroutine = 				typing.Coroutine
	Collection = 				typing.Collection
	AsyncGenerator = 			typing.AsyncGenerator
	AsyncContextManager = 		typing.AsyncContextManager

	Reversible = 				typing.Reversible
	SupportsAbs = 				typing.SupportsAbs
	SupportsBytes = 			typing.SupportsBytes
	SupportsComplex = 			typing.SupportsComplex
	SupportsFloat = 			typing.SupportsFloat
	SupportsIndex = 			typing.SupportsIndex
	SupportsInt = 				typing.SupportsInt
	SupportsRound = 			typing.SupportsRound

	ChainMap = 					typing.ChainMap
	Counter = 					typing.Counter
	Deque = 					typing.Deque
	Dict = 						typing.Dict
	DefaultDict = 				typing.DefaultDict
	List = 						typing.List
	OrderedDict = 				typing.OrderedDict
	Set = 						typing.Set
	FrozenSet = 				typing.FrozenSet
	NamedTuple = 				typing.NamedTuple
	TypedDict = 				typing.TypedDict
	Generator = 				typing.Generator

	BinaryIO = 					typing.BinaryIO
	IO = 						typing.IO
	Match = 					typing.Match
	Pattern = 					typing.Pattern
	TextIO = 					typing.TextIO

	AnyStr = 					typing.AnyStr
	LiteralString = 			typing.LiteralString
	Never = 					typing.Never
	NoReturn = 					typing.NoReturn
	NotRequired = 				typing.NotRequired
	ParamSpecArgs = 			typing.ParamSpecArgs
	ParamSpecKwargs = 			typing.ParamSpecKwargs
	Required = 					typing.Required
	Self = 						typing.Self
	Text = 						typing.Text
	TypeAlias = 				typing.TypeAlias
	TypeGuard = 				typing.TypeGuard
	Unpack = 					typing.Unpack


	Path = 						typing.NewType("Path", RFT_Types.Path)
	Array = 					typing.NewType("Array", RFT_Types.Array)
	Group = 					typing.NewType("Group", RFT_Types.Group)
	Number = 					typing.NewType("Number", RFT_Types.Number)
	Buffer = 					typing.NewType("Buffer", RFT_Types.Buffer)
	Dictionary = 				typing.NewType("Dictionary", RFT_Types.Dictionary)
	Module = 					typing.NewType("Module", RFT_Types.Module)




