from systemdesign.lottery_system.models import Prize, User
from systemdesign.lottery_system.services import DrawServiceImpl, LotteryServiceImpl, PrizeServiceImpl, TicketServiceImpl


def main():
    lottery_service = LotteryServiceImpl()
    ticket_service = TicketServiceImpl()
    prize_service = PrizeServiceImpl()
    draw_service = DrawServiceImpl()

    # Create a new lottery
    lottery = lottery_service.create_lottery("New Year Lottery", "2024-12-31")

    # Create users
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob", "bob@example.com")

    # Users purchase tickets
    ticket1 = ticket_service.purchase_ticket(user1, lottery)
    ticket2 = ticket_service.purchase_ticket(user2, lottery)

    # Add prizes to the lottery
    prize_service.add_prize(lottery, Prize(1, "First Prize", 1000))
    prize_service.add_prize(lottery, Prize(2, "Second Prize", 500))

    # Perform the draw
    winning_ticket = draw_service.perform_draw(lottery)
    if winning_ticket:
        print(f"The winning ticket is {winning_ticket.ticket_id} purchased by {winning_ticket.user.name}")
    else:
        print("No tickets sold for this lottery.")

if __name__ == "__main__":
    main()
