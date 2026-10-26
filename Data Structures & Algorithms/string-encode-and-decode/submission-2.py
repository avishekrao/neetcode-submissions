class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            string_length = len(string)
            encoded_string += (str(string_length) + "#" + string) 
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        while True:
            hashtag_index = s.find("#")
            if hashtag_index == -1:
                break
            string_character_count = int(s[:hashtag_index])
            string_to_be_added = s[hashtag_index + 1 : hashtag_index + 1 +
            string_character_count] #sliced string
            decoded_strings.append(string_to_be_added)
            s = s[hashtag_index + 1 + string_character_count:]
        return decoded_strings