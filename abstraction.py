from abc import ABC, abstractmethod
class movies(ABC):
    def paySlip(amount):
        print("Your total is: ", amount)
#this function is telling us to pass in an argument, but we wont tell you how or what kind of data it will be
    @abstractmethod
    def payment(self, amount):
        pass

#we are using a giftcard to pay for the movie ticket
class GiftCardPayment(movies):
#here we've defined how to implement the payment function from its parent paySlip class.
    def payment(amount):
        #lets us know what our balance is after payment
        print('Your purchase amount of {} brings your gift card balance to $16.25'.format(amount))

#calling functions based on amount
obj = GiftCardPayment
obj.paySlip("$8.75")
obj.payment("$8.75")