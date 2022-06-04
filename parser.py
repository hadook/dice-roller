

"""TODO class desc"""
class Parser:
    
    # returns a 3-element sublist of 'tokens' with the index element as the middle one
    @staticmethod
    def __get_neighbours(tokens: list[str], idx: int) -> list[str]:
        neighbours = []
        if idx == 0:
            neighbours.append(None)
        else:
            neighbours.append(tokens[idx - 1])
        neighbours.append(tokens[idx])
        if idx == len(tokens) - 1:
            neighbours.append(None)
        else:
            neighbours.append(tokens[idx + 1])
        return neighbours

