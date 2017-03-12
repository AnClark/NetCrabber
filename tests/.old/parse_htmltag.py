def extract_html_tag(tag_string):
    output = []
    blank_char = ('', ' ')
    quote_char = '"'

    # Each attributes is based on an equal mark. Just follow the basement, then we can get all possible attributes
    # Find out all equal marks
    eqv_mark_position = []
    for i in range(0, len(tag_string) - 1):
        if tag_string[i] == '=':
            eqv_mark_position.append(i)

    # Extend to both sides from eqv mark
    attrib_raw = []
    for i in range(0, eqv_mark_position.__len__() - 1):
        j = k = eqv_mark_position[i]
        while tag_string[j] not in blank_char:
            j -= 1
        while tag_string[k:k+1] != '" ':
            k += 1

        attrib_raw.append(tag_string[j+1 : k])

    # Parse each attrib raw data
    for i in range(0, attrib_raw.__len__() - 1):
        a = attrib_raw[i].split("=")
        b = {
            'attrib': a[0],
            'value': a[1].replace('"','')
        }
        output.append(b)

    return output



if __name__ == "__main__":
    print(extract_html_tag('<div id="basic_item" class="navbar col-md-4" onclick="test_click()">'))