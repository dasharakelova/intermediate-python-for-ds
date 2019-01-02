europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
print(europe.keys())
print(europe['norway'])
europe['italy'] = 'rome'
print('italy' in europe)
del(europe['norway'])
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
print([france][capital])
data = {'capital':'rome', 'population':59.83}
europe['italy'] = data

