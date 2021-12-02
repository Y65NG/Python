def calculate(n1, n2):
    if n2 == 0:
        return [n1 + n2, n1 - n2, n1 * n2, 0]
    return [n1 + n2, n1 - n2, n1 * n2, n1 / n2]

def find(cards):
    global steps

    if len(cards) == 1:
        if abs(cards[0] - 24) < 0.000001:
            # print(cards)
            return True
        return False
    else: 
        status = False
        for a in range(len(cards) - 1):
            for b in range(a + 1, len(cards)):
                
                temp = cards[:]
                temp.pop(a)
                temp.pop(b - 1)
                # print(cards)
                results = calculate(cards[a], cards[b])
                for r in results:
                    new_cards = [r] + temp
                    # print('new_cards:', new_cards)
                    status = status | find(new_cards)
                    if status: 
                        steps.append(cards)
                        return True
                    # print(status)
    # print(status)
    return status   
                
steps = []
print(find([6,11,7,8]))
# print(list(reversed(steps)))

