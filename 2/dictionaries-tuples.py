a_dic = {}
v_dic = {
    "abx": "A string",
    "another": "another string",
    "yetnoter": "another string",
}
v_dic["abx"] = "another new string"
v_dic["aa"] = v_dic
print(v_dic["aa"])
# print(v_dic[0])

tup = ()
tup = ("abc1", "abc1", "abc2")
tup1 = (
    ("another3", "another4"),
    ("more5", "more6"),
)

print(tup)
tup += tup1
print(tup)

the_list = []
abc = ["another", "another"]
the_list.append(abc)
print(the_list)
the_list.append(tup)
print(the_list)

