
def is_palindrome(chain: str):
    '''
    We use the lower function to convert any letter to lowercase, and in the function's return, we perform the validation using [::-1],
    which gives us the string reversed, and then we compare it with the original text.
    '''
    chain = chain.lower()
    return chain == chain[::-1]

def is_not_valid_transaction(transactions: list):
    '''
    We initialize the variables; one will be used to store invalid transactions, and the other will be used to check existing cards.
    '''
    invalid_transaction = []
    card_transactions = {}

    #we iterate each transaction
    for transaction in transactions:
        transaction_id, card_id, mount, city, timestamp = transaction
        
        #first validation by transaction amount
        if mount >= 10000:
            invalid_transaction.append(transaction_id)

        #we save the card ids only once in the list
        if card_id not in card_transactions:
            card_transactions[card_id] = []
        
        #Iteration of non-repeated cards where validation is performed based on countries and time between transactions
        for trans in card_transactions[card_id]:
            trans_id, trans_city, travel_time = trans
            if city != trans_city and timestamp - travel_time <= 30:
                invalid_transaction.append(transaction_id)
        
        #We append the card data
        card_transactions[card_id].append((transaction_id, city, timestamp))
    
    return list(set(invalid_transaction))

class UndergroundSystem():

    #store the information about check-ins and travel times between stations
    def __init__(self):
        self.check_in_data = {}
        self.travel_times = {}

    #store the data for check-in and the start of the journey
    def check_in(self, id: int, name: str, time: int):
        self.check_in_data[id] = (name, time)

    # check_out function 
    def check_out(self, id: int, stationame: str, time: int):
        # We look up the entry in the check_in_data object
        start_station, start_time = self.check_in_data.pop(id)
        # calculate travel time
        travel_time = time - start_time

        # search in the travel object and perform validations on the stations and accumulated time, updating the data
        if (start_station, stationame) not in self.travel_times:
            total_time, count = self.travel_times[(start_station, stationame)] = (0, 0)

        self.travel_times[(start_station, stationame)] = (total_time + travel_time, count + 1)
    # Calculate and update the average travel time using the formula: travel time divided by the total number of trips
    def get_average_time(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count
    
undergroundSystem = UndergroundSystem()

undergroundSystem.check_in(1, "A", 3)
undergroundSystem.check_out(1, "B", 8)

undergroundSystem.check_in(2, "B", 4)
undergroundSystem.check_out(2, "A", 10)

