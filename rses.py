# Discretization Alogorithm

import pandas as pd
import json

df = pd.read_csv("data.txt", header=None)
rses_array = df.values.tolist()
rses_array_removed_lastcol = df.iloc[:, :-1].values.tolist()
# print(rses_array)
print(rses_array_removed_lastcol)

col_num = df.shape[1]
row_num = df.shape[0]
# print(col_num)
col_arr = [[] for i in range(col_num)]
# print(col_arr)
for row_num, row_val in enumerate(rses_array_removed_lastcol):
    for col_num, col_val in enumerate(row_val):
        col_arr[col_num].append(col_val)
new_col_arr = []
for col in col_arr:
    new_col_arr.append(sorted(set(col)))
# print(new_col_arr)

# REMOVE THE LAST COLUMN
new_col_arr = new_col_arr[:-1]
# print(new_col_arr)

variables = ["p", "q", "r", "s", "t", "u", "v"]
var_arr = []
for col_idx, col in enumerate(new_col_arr):
    var = variables[col_idx]
    col_arr = []
    for idx in range(len(col)-1):
        col_arr.append({f"{var}{idx+1}": (col[idx], col[idx+1])})
    var_arr.append(col_arr)

print("\nRANGE:")
for col in var_arr:
    print(col)

# full_arr = []
# for i in range(len(rses_array_removed_lastcol)-1):
#     for j in range(1, len(rses_array_removed_lastcol)):
#         temp_arr = []
#         if i != j:
#             print(f"\n(X{i+1}, X{j+1}) =>", rses_array_removed_lastcol[i], rses_array_removed_lastcol[j], "=>")
#             for r in range(len(var_arr)):
#                 print("\nvar_arr[r]", var_arr[r])
#                 print("rses_array_removed_lastcol[i][r]", rses_array_removed_lastcol[i][r], "rses_array_removed_lastcol[j][r]", rses_array_removed_lastcol[j][r])
#                 low_idx = rses_array_removed_lastcol[i][r]
#                 high_idx = rses_array_removed_lastcol[j][r]
#                 if low_idx > high_idx:
#                     low_idx, high_idx = high_idx, low_idx
#                 # print("low_idx", low_idx, "high_idx", high_idx)
#                 if low_idx == high_idx:
#                     print("break")
#                     break
#                 else:
#                     print("low_idx", low_idx, "high_idx", high_idx)
#                     for dictobj in var_arr[r]:
#                         for key, value in dictobj.items():
#                             print(key, value)
#                             print(low_idx, high_idx)
#                             print(type(value[0])
#                             print(type(low_idx))
#                             if int(value[0]) == (int(low_idx)):
#                                 print(f"{value[0]} == {low_idx}")
#                                 print(f"V1: {value[0]}")
#                                 temp_arr.append(key)
#                                 print(temp_arr)
#                             if int(value[1]) == (int(high_idx)):
#                                 print(f"{value[1]} == {high_idx}")
#                                 print(f"V1: {value[1]}")
#                                 temp_arr.append(key)
#                                 print(temp_arr)

#         print("FINAL: ", temp_arr)
        #     full_arr.append(sorted(set(temp_arr)))
        #     print(f"(X{i+1}, X{j+1}) =>", sorted(set(temp_arr)))

# print(full_arr)