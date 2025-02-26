"""
Given:
    string 'message' containing only lowercase Letters and whitespace

Return:
    'can_trust_message()' that returns True if the message contains every letter
    of the english alphabet at least once, false o.t.
"""

from typing import Dict


def can_trust_message(message: str) -> bool:
    # we do idx + 1 here because what if the whitespace is at idx 0?
    # well check_whitespace returns the idx of 0 which is False
    # when it should be true
    ch_map: Dict = {ch: idx + 1 for idx, ch in enumerate(message)}

    check_whitespace: bool = ch_map.get(" ", False)

    # if true check for 27 characters (alphabet + 1)
    if check_whitespace:
        return len(ch_map) == 27

    return len(ch_map) == 26


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
