class Solution:
    def uniqueLetterString(self, S: str) -> int:
        s_length = len(S)
        index_dict = collections.defaultdict(list)
        for index, char in enumerate(S):
            index_dict[char].append(index)
        # index_dict = defaultdict(<class 'list'>, {'L': [0], 'E': [1, 2, 7], 'T': [3], 'C': [4], 'O': [5], 'D': [6]})

        
        results = 0
        for char, occurences in index_dict.items():
            # char: E
            # occurences: [1,2,7]
            for occurence_index, char_index in enumerate(occurences):
                # occurence_index: 0 => 1 => 2
                # char_index => 1 => 2 => 7
                
                is_first_occurence = occurence_index == 0
                left = -1
                if is_first_occurence:
                    left = char_index
                else:
                    prev_char_index = occurences[occurence_index-1]
                    left = char_index - prev_char_index - 1
                
                is_last_occurence = occurence_index == len(occurences) - 1
                right = -1
                if is_last_occurence:
                    right = s_length - char_index - 1 
                else:
                    next_char_index = occurences[occurence_index+1]
                    right = next_char_index - char_index - 1
                # Unique contribution is actually just a rectangle, times left + 1 and right + 1 give the result
                results += (left + 1) * (right + 1)
        return results