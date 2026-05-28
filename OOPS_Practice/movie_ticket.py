class MovieTicket:

    def __init__(self, movie_name, ticket_price, quantity):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.quantity = quantity

    def total(self):
        ticket_price = self.ticket_price * self.quantity
        if ticket_price > 1000:
            discount = ticket_price * 0.1
        else:
            discount = 0
        return ticket_price , discount
    @staticmethod
    def hall_name():
        print("Thank you for visiting ABC Movie Theatre")
    

movie_name = input("Enter What movie do you want to see : ")
ticket_price = int(input("Enter the price of the movie : "))
quantity = int(input("Enter the number of tickets you want to buy : "))

customer = MovieTicket(movie_name, ticket_price, quantity)

print(f"Movie : {customer.movie_name}")
print(f"Ticket Price : {customer.ticket_price}")
print(f"Ticket : {customer.quantity}")
print()
total , discount = customer.total()
final_price = total - discount
print(f"Total : {total}")
print(f"Discount : {discount}")
print(f"Final Price : {final_price}")
customer.hall_name()

        
