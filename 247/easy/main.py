import random

with open('input.txt') as f:
    data = f.read().split('\n')[:-1]

pool = ' '.join(data).split()
families = [names.split() for names in data if len(names.split()) != 1]

def write(member, match):
    f.write('{member} -> {match}\n'.format(member=member, match=match))

with open('output.txt', 'w') as f:
    for family_members in families:
        for member in family_members:
            while True:
                match = random.choice(pool)
                if match not in family_members and match != member:
                    write(member, match)
                    pool = [x for x in pool if x is not match]
                    break
    for member in pool:
        while True:
            match = random.choice(pool)
            if match != member:
                write(member, match)
                pool = [x for x in pool if x is not match]
                break

