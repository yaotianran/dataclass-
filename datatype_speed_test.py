#!/usr/bin/env python3

# speed test

from dataclasses import dataclass
from typing import TypedDict
import collections
from time import time

@dataclass
class BaseInfo:
   base_real: str = None # called base所在位置的真实碱基种类，base_real ∈ {A，T，C，G, N}

   base_called: str = None # called base的碱基种类，base_called ∈ {A，T，C，G, N}
   read_flag: str = None # read_flag ∈ {'83'，'163', '99', '147'}
   gc_ratio: int = None # gc_ratio ⊂ [0, 1]
   base_upstream: str = None #     如果没有上游序列,则设置成''
   base_downstream: str = None #   如果没有下游序列,则设置成''
   cycle: int = None  # cycle ⊂ [1, 150]
   base_qual: int = None #  base_qual ⊂ [0, 49]
   base_qual_upstream: int = None #  base_qual_upstream ⊂ [-1, 49]   如果没有上游序列,则设置成99
   base_qual_downstream: int = None #  base_qual_downstream ⊂ [-1, 49], 如果没有下游序列,则设置成99

@dataclass(frozen=True)
class BaseInfo_frozen:
   base_real: str = None # called base所在位置的真实碱基种类，base_real ∈ {A，T，C，G, N}

   base_called: str = None # called base的碱基种类，base_called ∈ {A，T，C，G, N}
   read_flag: str = None # read_flag ∈ {'83'，'163', '99', '147'}
   gc_ratio: int = None # gc_ratio ⊂ [0, 1]
   base_upstream: str = None #     如果没有上游序列,则设置成''
   base_downstream: str = None #   如果没有下游序列,则设置成''
   cycle: int = None  # cycle ⊂ [1, 150]
   base_qual: int = None #  base_qual ⊂ [0, 49]
   base_qual_upstream: int = None #  base_qual_upstream ⊂ [-1, 49]   如果没有上游序列,则设置成99
   base_qual_downstream: int = None #  base_qual_downstream ⊂ [-1, 49], 如果没有下游序列,则设置成99


class BaseInfo_dict(TypedDict):
   base_real: str = None # called base所在位置的真实碱基种类，base_real ∈ {A，T，C，G, N}

   base_called: str = None # called base的碱基种类，base_called ∈ {A，T，C，G, N}
   read_flag: str = None # read_flag ∈ {'83'，'163', '99', '147'}
   gc_ratio: int = None # gc_ratio ⊂ [0, 1]
   base_upstream: str = None #     如果没有上游序列,则设置成''
   base_downstream: str = None #   如果没有下游序列,则设置成''
   cycle: int = None  # cycle ⊂ [1, 150]
   base_qual: int = None #  base_qual ⊂ [0, 49]
   base_qual_upstream: int = None #  base_qual_upstream ⊂ [-1, 49]   如果没有上游序列,则设置成99
   base_qual_downstream: int = None #  base_qual_downstream ⊂ [-1, 49], 如果没有下游序列,则设置成99

BaseInfo_tu = collections.namedtuple('BaseInfo_tu', ['base_real', 'base_called', 'read_flag', 'gc_ratio', 'base_downstream', 'base_upstream', 'cycle', 'base_qual', 'base_qual_upstream', 'base_qual_downstream', ])

N = 500000


t = time()
test = []
for _ in range(N):
   base_info = BaseInfo()
   base_info.base_real = 'A'
   base_info.base_called = 'T'
   base_info.read_flag = int(str(round(time() * 10000))[-1:])
   base_info.gc_ratio = int(str(round(time() * 10000))[-1:])
   base_info.base_upstream = 'GG'
   base_info.base_downstream = 'AG'
   base_info.cycle = int(str(round(time() * 10000))[-1:])
   base_info.base_qual = int(str(round(time() * 10000))[-1:])
   base_info.base_qual_upstream = int(str(round(time() * 10000))[-1:])
   base_info.base_qual_downstream = int(str(round(time() * 10000))[-1:])

   test.append(base_info)

print('ordinary collections.dataclass: ', time() - t)

t = time()
test = []
for _ in range(N):
   base_info = BaseInfo_dict(
      base_real = 'A',
      base_called = 'T',
      read_flag = int(str(round(time() * 10000))[-1:]),
      gc_ratio = int(str(round(time() * 10000))[-1:]),
      base_upstream = 'GG',
      base_downstream = 'AG',
      cycle = int(str(round(time() * 10000))[-1:]),
      base_qual = int(str(round(time() * 10000))[-1:]),
      base_qual_upstream = int(str(round(time() * 10000))[-1:]),
      base_qual_downstream = int(str(round(time() * 10000))[-1:]),
   )

   test.append(base_info)
print('typing.TypedDict: ', time() - t)

t = time()
test = []
for _ in range(N):
   base_info = BaseInfo_tu(
      base_real = 'A',
      base_called = 'T',
      read_flag = int(str(round(time() * 10000))[-1:]),
      gc_ratio = int(str(round(time() * 10000))[-1:]),
      base_upstream = 'GG',
      base_downstream = 'AG',
      cycle = int(str(round(time() * 10000))[-1:]),
      base_qual = int(str(round(time() * 10000))[-1:]),
      base_qual_upstream = int(str(round(time() * 10000))[-1:]),
      base_qual_downstream = int(str(round(time() * 10000))[-1:]),
   )

   test.append(base_info)
print('collections.namedtuple: ', time() - t)

t = time()
test = []
for _ in range(N):
   base_info = BaseInfo_frozen(
      base_real = 'A',
      base_called = 'T',
      read_flag = int(str(round(time() * 10000))[-1:]),
      gc_ratio = int(str(round(time() * 10000))[-1:]),
      base_upstream = 'GG',
      base_downstream = 'AG',
      cycle = int(str(round(time() * 10000))[-1:]),
      base_qual = int(str(round(time() * 10000))[-1:]),
      base_qual_upstream = int(str(round(time() * 10000))[-1:]),
      base_qual_downstream = int(str(round(time() * 10000))[-1:]),
   )

   test.append(base_info)
print('frozen collections.dataclass', time() - t)
