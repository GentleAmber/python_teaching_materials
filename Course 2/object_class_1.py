class TicketBooth:
  totalTicket = 100

  def sellTicket(self, num):
    print("")

ticketBooth1 = TicketBooth()
ticketBooth2 = TicketBooth()

ticketBooth1.sellTicket(2)
ticketBooth2.sellTicket(3)

print(f"ticketBooth1剩下：{ticketBooth1.totalTicket}张票，"
      f"ticketBooth2剩下：{ticketBooth2.totalTicket}张票")

print(ticketBooth1.totalTicket is ticketBooth2.totalTicket)