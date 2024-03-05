# 比较了dataclass，typedict，namedtuple和frozen dataclass的创建速度

typedict速度最快，如果将typedict的创建速度设为1

- typing.TypedDict ：1
- collections.namedtuple ：1.10 ~ 1.15
- ordinary collections.dataclass：1.15 ~ 1.20
- frozen collections.dataclass：1.3 ~ 1.4

注意，只有collections.namedtuple和frozen collections.dataclass为hashable，即可以作为字典的key
