# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, 
# they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a 
# movie per day is 3 dollars, how much will you have to pay?
cost = 3*(3+5+1)
# 3 dollars times number of days combined over all the movies

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a 
# different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will 
# you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours 
# for Amazon.
total_payment = 400*6 + 380*4 + 350*10

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not 
# conflict with her current schedule.
enrolled if class_not_full == true AND no_schedule_conflict == true

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products
offer if premium member or (bought > 2 AND offer_not_expired == true)

# 5. Create a variable that holds a boolean value for each of the following conditions:

        # the password must be at least 5 characters
        long_enough = len(password) > 5
        # the username must be no more than 20 characters
        not_too_long = len(username) <= 20
        # the password must not be the same as the username
        not_same = password != username