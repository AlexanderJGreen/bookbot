def word_count(contents):
       words = contents.split()
       count = len(words)
       return count

def count_characters(contents):
    char_count = {}
    for char in contents:
     #   print(char)
       char = char.lower()
       if char in char_count:
            char_count[char] += 1
       else:
            char_count[char] = 1   
    return char_count

def sorted_character_counts(char_count):
     result = []
     for char, count in char_count.items():
          new_entry = {"character": char, "count": count}
          result.append(new_entry)
     result.sort(key=lambda item: item["count"], reverse=True)
     return result

