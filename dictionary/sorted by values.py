def sorted_by_values(d,reverse=False):
    return dict(sorted(d.items(),key=lambda x:x[1],reverse=reverse))
print("original dictionery:")
colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
print(colors)
print("/nsort acendindin order by values:")
print(sorted_by_values(colors))
print("/nsort decending order by valuse:")
print(sorted_by_values(colors,True))