# 比较了dataclass，typedict，namedtuple和frozen dataclass的创建速度

typedict速度最快，如果将typedict的创建时间设为1，那么其他类型的创建时间如下

- typing.TypedDict ：1
- collections.namedtuple ：1.10 ~ 1.15
- ordinary collections.dataclass：1.15 ~ 1.20
- frozen collections.dataclass：1.3 ~ 1.4

可见frozen collections.dataclass比typing.TypedDict慢30% ～ 40%

注意，只有collections.namedtuple和frozen collections.dataclass为hashable，即可以作为字典的key
