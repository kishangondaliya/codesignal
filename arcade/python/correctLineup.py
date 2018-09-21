def correctLineup(athletes):
    return [val for item in [a for a  in zip([e for i, e in enumerate(athletes) if i % 2 !=0],[e for i, e in enumerate(athletes) if i % 2 ==0])] for val in item]
