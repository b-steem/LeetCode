def gcdOfStrings(self, str1: str, str2: str) -> str:
    first_char = str1[0]
    div = ""
    max_str = str1 if len(str1) > len(str2) else str2
    min_str = str1 if len(str1) <= len(str2) else str2
    divisor_found = False

    for i in range(len(max_str)):
        min_idx = (i % len(min_str)) - 1    # convert to zero based index
        div_idx = -1 if len(div) == 0 else (i % len(div)) - 1
        if max_str[i] != min_str[min_idx]:
            return ""

        elif divisor_found and div_idx > -1 and max_str[i] != div[div_idx]:    # we already know min_str == max_str
            return ""

        elif max_str[i] == first_char:
            divisor_found = True

        else:
            div += max_str[i]

    return div