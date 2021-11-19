def solution(new_id):
    valid = ['-', '_', '.']
    for l in new_id:
        if not l.isalpha() and not l.isdigit() and l not in valid:
            new_id = new_id.replace(l, '')
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    if len(new_id) == 0:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    if len(new_id) <= 3:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
        
    return new_id.lower()
