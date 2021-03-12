import ast

txt = "{'Amazon': 'WEE', 'Youtube': 'WEEE'}"

x = ast.literal_eval(txt)

print(x)
