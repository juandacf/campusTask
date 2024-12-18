data = {
    'persona1': {
        'nombre': 'Juan',
        'edad': 25
    },
    'persona2': {
        'nombre': 'Ana',
        'edad': 30
    }
}

for k,v in data.items():
    for l,b in v.items():
        if(l=='nombre'):
            print(b)