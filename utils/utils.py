class UnInitializedComponent:
    def __init__(self, cname):
        self.class_name = cname
        
    def __getattr__(self, func_name):
        def method(*args, **kwargs):
            print(f"[Warning] Called {func_name} on a {self.class_name}.")
        return method

def safe_init(cls, name):
    try:
        return cls()
    except Exception as e:
        print(f"{e}. {name} couldn't be initialized")
        return UnInitializedComponent(name)

def hex_to_decimal(hex_string):
    return int(hex_string, 16)

def in_range(value, start, stop):
    step = 1 if start <= stop else -1
    adjusted_stop = stop + 1 if step > 0 else stop - 1
    is_in_range = value in range(start, adjusted_stop, step)
    # print(f"{value} is {'' if is_in_range else 'not'} in range of {start} and {stop}")
    return is_in_range

def map_range(value, min_val, max_val):
    return min_val + (max_val - min_val) * round(value, 1)
