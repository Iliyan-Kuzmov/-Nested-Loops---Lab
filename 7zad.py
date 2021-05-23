movie = input()
student_ticket = 0
standard_ticket = 0
kid_ticket = 0

while movie != 'Finish':
    free_seats = int(input())
    sold_ticket = 0

    ticket_type = input()
    while ticket_type != 'End':
        sold_ticket += 1
        if ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'kid':
            kid_ticket += 1

        if sold_ticket == free_seats:
            break
        ticket_type = input()

    print(f'{movie} - {sold_ticket / free_seats * 100:.2f}% full.')
    movie = input()

total = standard_ticket + student_ticket + kid_ticket
print(f'Total tickets: {total}')
print(f'{student_ticket / total * 100:.2f}% student tickets.')
print(f'{standard_ticket / total * 100:.2f}% standard tickets.')
print(f'{kid_ticket / total * 100:.2f}% kids tickets.')

