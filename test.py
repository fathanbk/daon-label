# # import pandas as pd

# # test = pd.DataFrame(
# #             {
# #                 "A": 1.0,
# #                 "B": pd.Timestamp("20130102"),
# #                 "C": pd.Series(1, index=list(range(4)), dtype="float32"),
# #                 "D": pd.array([3] * 4, dtype="int32"),
# #                 "E": pd.Categorical(["test", "train", "test", "train"]),
# #                 "F": "foo",
# #             }
# #         )

# # print(test)

# a = [2.7, 5.4, 3.5, 6.7, 4.3, 4.1]
# # a.sort()
# print(a.split(3))

from enum import Enum

class Season(Enum):
  SPRING = 1
  SUMMER = 2
  AUTUMN = 3
  WINTER = 4

# printing enum member as string
print(Season.SPRING)

# printing name of enum member using "name" keyword
print(Season.SPRING.name)

# printing value of enum member using "value" keyword
print(Season.SPRING.value)

# printing the type of enum member using type()
print(type(Season.SPRING))

# printing enum member as repr
print(repr(Season.SPRING))

# printing all enum member using "list" keyword
print(list(Season))