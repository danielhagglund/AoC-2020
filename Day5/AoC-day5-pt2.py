def find_row(card):
    max = 127
    min = 0
    for i in range (0,7):
        if card[i] == 'F':
            max = int(min+((max-min) / 2))
        elif card[i] == 'B':
            min = int(max-((max-min)/2))
    return max

def find_col(card):
    max = 7
    min = 0
    for i in range (7,10):
        if card[i] == 'L':
            max = int(min+((max-min) / 2))
        elif card[i] == 'R':
            min = int(max-((max-min)/2))
    return max


def find_seat(boardingcard):
    row = find_row(boardingcard)
    col = find_col(boardingcard)
    return row * 8 + col

def find_gap(seats):
    i = 0
    found = False
    while (not found) and (i < len(seats)):
        gap = seats[i+1] - seats[i]
        if gap == 2:
            found = True
        else:
            i = i+1
    
    return seats[i] + 1 


input_data = open("./Boardingcards.txt").read().splitlines()
test_boardingcards = ["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"] #567, 119, 820

highest = 0
seats = []
for boardingcard in input_data:
    seat_id = find_seat(boardingcard)
    seats.append(seat_id)
seats.sort()
myseat = find_gap(seats)
print(myseat)