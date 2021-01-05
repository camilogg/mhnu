def snake_case_to_camel_case(value: str):
    # split underscore using split
    str_values = value.split('_')

    # joining result
    res = str_values[0] + ''.join(
        ele.title() if ele != 'ID' else ele for ele in str_values[1:]
    )

    return res
