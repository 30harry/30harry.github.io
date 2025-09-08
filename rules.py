
constants = {}
variables = {}
functions = {}

def define_constant(name, description=""):
    if name in constants:
        raise ValueError('Constant already defined: %s' % name)
    constants[name] = {"name": name, "description": description}

def define_variable(name, description="", aliases=[]):
    if name in variables:
        raise ValueError('Variable already defined: %s' % name)
    variables[name] = {"name": name, "description": description, "aliases": aliases}

def define_function(name, description="", aliases=[]):
    if name in constants:
        raise ValueError('Function already defined: %s' % name)
    functions[name] = {"name": name, "description": description, "variants": [], "aliases": aliases}

def define_function_variant(name, variant, description=""):
    if name not in functions:
        raise ValueError('Function not defined: %s' % name)
    variants = functions[name]["variants"]
    if variant in variants:
        raise ValueError('Function variant already defined: %s' % variant)
    variants.append({"name": variant, "description": description})


def display_rules():
    for name, values in constants.items():
        print("CONSTANT", name, values["description"])

    for name, values in variables.items():
        print("VARIABLE", name, ":", values["description"])
        for alias in values["aliases"]:
            print("  ALIAS", alias)

    for name, values in functions.items():
        print("FUNCTION", name, ":", values["description"])
        for alias in values["aliases"]:
            print("  ALIAS", alias)
        for variant in values["variants"]:
            print("  VARIANT", variant["name"], ":", variant["description"])

define_constant('TRUE')
define_constant('FALSE')

define_variable('PLAYER_STAT', 'Modified players stat')
define_variable('OPPONENT_STAT', 'Modified opponets stat')
define_variable('ATTACKER_STAT', 'Modified attackers stat')
define_variable('DEFENDER_STAT', 'Modified defenders stat')

define_function('STAT', 'Modified players stat')
define_function_variant('STAT', 'STAT([true])', 'Modified players stat')
define_function_variant('STAT', 'STAT([false])', 'Modified opponent stat')

display_rules()
