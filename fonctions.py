def var_name(var):
    """Fonction permettant de récupérer le nom de la variable passée en paramètre."""
    for name,value in globals().items() :
        if value is var :
            return name
        
def analyse_primaire(DataFrame):
    """Fonction exécutant les fonctions/propriétés head/dtypes/shape/describe du DataFrame passé en paramètre"""
    nom = var_name(DataFrame)
    fonctions = ['head', 'dtypes', 'shape', 'describe']
    for x in fonctions:
        if callable(object.__getattribute__(DataFrame, x)):
            if x == 'describe':
                print(f"{nom}.{x}(describe = 'all')")
                display(object.__getattribute__(DataFrame, x)(include = 'all'))
            else:
                print(f"{nom}.{x}()")
                display(object.__getattribute__(DataFrame, x)())
        else:
            print(f"{nom}.{x}")
            display(object.__getattribute__(DataFrame, x))