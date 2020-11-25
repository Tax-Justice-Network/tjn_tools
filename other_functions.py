def myround(x, base=5,how="round"):
    """
    Round to closest number (defined by base)
    
    Input:
    - x: number
    - base: round to this number
    - how [round/ceil/floor]: round (round to closest number), floor (round down), ceil (round up)
    
    Output:
    - Rounded number
    
    """
    if how == "rount":
        return base * round(x/base)
    elif how == "ceil":
        return base * int((x+base)/base)
    elif how == "floor":
        return base * int(x/base)