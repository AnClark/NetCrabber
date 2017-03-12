def quote_filter(string):
    output = []         # Result array
    buff = ""           # Buffer to concaternate string inside quotation mark
    qmark = False       # Mark if inside quotation mark

    # Linear scan source string
    for i in range(0, len(string) - 1):
        # Quotation marks control the concaternation
        if string[i] == '"':
            if not qmark:       # Meet a former qmark
                qmark = True
                buff = ""   # Re-init buffer
            else:               # Meet a latter qmark
                qmark = False
                output.append(buff)     # Submit result
        else:
            if qmark:
                buff += string[i]

    return output                


if __name__ == "__main__":
    print(quote_filter(
            """
id="aaa" src="bbb"
tag="axxca"
language="HTML"
"""
        ))
