# from dataclasses import dataclass
# from abc import ABC, abstractmethod
# @dataclass
# class Caller:
#     name: str
# class ConnectionException(Exception):
#     pass
# class CommsHandlerABC(ABC):
    
#     @abstractmethod
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         """Implement connect method"""
#     @abstractmethod
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         """Implement hangup method"""
#     @abstractmethod
#     def clear_all(self) -> None:
#         """Implement clear_all method"""
        
# class CommsHandler(CommsHandlerABC):
    
#     def __init__(self):
#         self.active_connections = []
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         if user1 == user2:
#             raise ConnectionException(f"{user1.name} cannot connect with {user2.name}")
#         if any(user in self.active_connections for user in [user1, user2]):
#             raise ConnectionException("Connection in use. Please try later")
#         self.active_connections.extend([user1, user2])
#         return f"Connection established between {user1.name} and {user2.name}"
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         if user1 == user2:
#             raise ConnectionException(f"{user1.name} cannot hangup with {user2.name}")
#         if user1 in self.active_connections and user2 in self.active_connections:
#             self.active_connections.remove(user1)
#             self.active_connections.remove(user2)
#             return f"{user1.name} and {user2.name} are disconnected"
#         raise ConnectionException(f"{user1.name} and {user2.name} not found in the communication channel")
#     def clear_all(self) -> None:
#         self.active_connections.clear()
        
# # Main code
# def main():
#     comms = CommsHandler()
#     functions = {"connect": comms.connect, "hangup": comms.hangup}
#     # Create users
#     n = int(input().strip())
#     users = []
#     for _ in range(n):
#         name = input().strip()
#         u = Caller(name)
#         assert u.name == name
#         users.append(u)
#     # Perform operations
#     instructions_count = int(input().strip())
#     result_str = ""
#     for _ in range(instructions_count):
#         instructions = input().strip().split()
#         ul, u2 = map(int, instructions[1:])
#         # import pdb;pdb.set_trace()
#         try:
#             result_str += "Success: " + functions[instructions[0]](users[ul], users[u2]) + "\n"
#             print("-------", result_str)
#         except ConnectionException as ce:
#             result_str += "Error: " + str(ce) + "\n"
#             print("========", result_str)
#     comms.clear_all()
    
# if __name__ == "__main__":
#     main()

# class CommunicationException(Exception):
#     pass

# class Caller:
#     def __init__(self, name):
#         self.name = name

# class CommsHandlerABC:
#     def connect(self, user1: Caller, user2: Caller) -> str:
#         raise NotImplementedError
    
#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         raise NotImplementedError
    
#     def clear_all(self) -> None:
#         raise NotImplementedError

# class CommsHandler(CommsHandlerABC):
#     def __init__(self):
#         self.connected_users = set()

#     def connect(self, user1: Caller, user2: Caller) -> str:
#         if user1 is user2:
#             raise CommunicationException(f"{user1.name} cannot connect with {user2.name}")

#         if self._is_line_in_use():
#             raise CommunicationException("Connection in use. Please try later!!")

#         self.connected_users.add(user1)
#         self.connected_users.add(user2)
#         return f"Connection established between {user1.name} and {user2.name}"

#     def hangup(self, user1: Caller, user2: Caller) -> str:
#         if user1 is user2:
#             raise CommunicationException(f"{user1.name} cannot hangup with {user2.name}")

#         if user1 not in self.connected_users or user2 not in self.connected_users:
#             import pdb;pdb.set_trace()
#             raise CommunicationException(f"{user1.name} and {user2.name} not found in the communication channel")

#         self.connected_users.discard(user1)
#         self.connected_users.discard(user2)
#         return f"{user1.name} and {user2.name} are disconnected"

#     def clear_all(self) -> None:
#         self.connected_users.clear()

#     def _is_line_in_use(self):
#         return len(self.connected_users) >= 2

# # Sample Input
# n = 3
# users = ['Hana', 'Luca', 'Lev']
# instructions = [
#     ("connect", 0, 1),
#     ("hangup", 0, 1),
#     ("connect", 1, 2),
#     ("hangup", 1, 2),
# ]

# # Create CommsHandler instance
# comms_handler = CommsHandler()

# # Process instructions
# for instr, user1_idx, user2_idx in instructions:
#     user1 = Caller(users[user1_idx])  # Use user1_idx to index users list
#     user2 = Caller(users[user2_idx])  # Use user2_idx to index users list
    
#     if instr == "connect":
#         result = comms_handler.connect(user1, user2)
#         print("Success:", result)
#     elif instr == "hangup":
#         result = comms_handler.hangup(user1, user2)
#         print("Success:", result)



# import requests

# def bestinGenre(genre):
#     # Initialize variables to keep track of the highest-rated series and the lowest name alphabetically.
#     highest_rating = -1
#     lowest_name = None

#     # Initialize the page number to 1 for pagination.
#     page = 1

#     while True:
#         # Send a GET request to the API with the genre and page number as query parameters.
#         response = requests.get(f"https://jsonmock.hackerrank.com/api/tvseries?genre={genre}&page={page}")
#         data = response.json()

#         # Iterate through the TV series data.
#         for series in data['data']:
#             rating = series['imdb_rating']
#             name = series['name']

#             # Check if the current series has a higher rating or a lower name alphabetically.
#             if rating > highest_rating or (rating == highest_rating and name < lowest_name):
#                 highest_rating = rating
#                 lowest_name = name

#         # Check if there are more pages to fetch.
#         if page < data['total_pages']:
#             page += 1
#         else:
#             break

#     return lowest_name  # Return the lowest alphabetically sorted name with the highest rating.

# # Test the function with the "Action" genre.
# genre = "Action"
# result = bestinGenre(genre)
# print(result)  # Output should be "Game of Thrones"

# simulated_data = {
#     "page": 1,
#     "per_page": 10,
#     "total": 4,
#     "total_pages": 1,
#     "data": [
#         {
#             "name": "Game of Thrones",
#             "imdb_rating": 9.3
#         },
#         {
#             "name": "Avatar: The Last Airbender",
#             "imdb_rating": 9.2
#         },
#         {
#             "name": "Hagane no renkinjutsushi",
#             "imdb_rating": 9.1
#         },
#         {
#             "name": "Shingeki no kyojin",
#             "imdb_rating": 8.9
#         }
#     ]
# }

# def bestinGenre(genre):
#     shows = simulated_data["data"]
#     highest_rating = 0
#     best_show = {}  # Initialize best_show as an empty dictionary

#     for show in shows:
#         rating = show["imdb_rating"]
#         if rating > highest_rating or (rating == highest_rating and show["name"] < best_show.get("name", "")):
#             highest_rating = rating
#             best_show = show

#     return best_show.get("name", "")

# # Sample input
# genre = "Animation"

# # Call the function with the sample input
# result = bestinGenre(genre)
# print(result)


import requests

def bestinGenre(genre):
    # Initialize variables to keep track of the highest-rated series and the lowest name alphabetically.
    highest_rating = 1
    lowest_name = None

    # Initialize the page number to 1 for pagination.
    page = 1

    while True:
        # Send a GET request to the API with the genre and page number as query parameters.
        response = requests.get(f"https://jsonmock.hackerrank.com/api/tvseries?genre={genre}&page={page}")
        data = response.json()

        # Iterate through the TV series data.
        for series in data['data']:
            rating = series['imdb_rating']
            name = series['name']

            # Check if the current series has a higher rating or a lower name alphabetically.
            if rating > highest_rating or (rating == highest_rating and name < lowest_name):
                highest_rating = rating
                lowest_name = name

        # Check if there are more pages to fetch.
        if page < data['total_pages']:
            page += 1
        else:
            break

    return lowest_name  # Return the lowest alphabetically sorted name with the highest rating.

# Test the function with the "Action" genre.
genre = "Animation"
result = bestinGenre(genre)
print(result)  # Output should be "Game of Thrones"


