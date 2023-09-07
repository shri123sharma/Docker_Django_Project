# # # # # # # # # # # # # # def countBalancedWords(n, d):
# # # # # # # # # # # # # #     MOD = 10**9 + 7
    
# # # # # # # # # # # # # #     # Initialize a 2D DP array
# # # # # # # # # # # # # #     dp = [[0] * 26 for _ in range(n + 1)]
    
# # # # # # # # # # # # # #     # Base case: one character words are always balanced
# # # # # # # # # # # # # #     for i in range(26):
# # # # # # # # # # # # # #         dp[1][i] = 1
    
# # # # # # # # # # # # # #     # Fill the DP array
# # # # # # # # # # # # # #     for length in range(2, n + 1):
# # # # # # # # # # # # # #         for i in range(26):
# # # # # # # # # # # # # #             for j in range(max(0, i - d), min(26, i + d + 1)):
# # # # # # # # # # # # # #                 dp[length][i] = (dp[length][i] + dp[length - 1][j]) % MOD
    
# # # # # # # # # # # # # #     # Calculate the total number of balanced words of length n
# # # # # # # # # # # # # #     total_balanced_words = sum(dp[n]) % MOD
    
# # # # # # # # # # # # # #     return total_balanced_words

# # # # # # # # # # # # # # # Read input values
# # # # # # # # # # # # # # n = int(input().strip())
# # # # # # # # # # # # # # d = int(input().strip())

# # # # # # # # # # # # # # # Calculate and print the result
# # # # # # # # # # # # # # result = countBalancedWords(n, d)
# # # # # # # # # # # # # # print(result)


# # # # # # # # # # # # # def countBalancedWords(n, d):
# # # # # # # # # # # # #     MOD = 10**9 + 7
    
# # # # # # # # # # # # #     # Initialize a 2D DP array
# # # # # # # # # # # # #     dp = [[0] * 26 for _ in range(n + 1)]
    
# # # # # # # # # # # # #     # Base case: one character words are always balanced
# # # # # # # # # # # # #     for i in range(26):
# # # # # # # # # # # # #         dp[1][i] = 1
    
# # # # # # # # # # # # #     # Fill the DP array
# # # # # # # # # # # # #     for length in range(2, n + 1):
# # # # # # # # # # # # #         for i in range(26):
# # # # # # # # # # # # #             for j in range(max(0, i - d), min(26, i + d + 1)):
# # # # # # # # # # # # #                 dp[length][i] = (dp[length][i] + dp[length - 1][j]) % MOD
    
# # # # # # # # # # # # #     # Calculate the total number of balanced words of length n
# # # # # # # # # # # # #     total_balanced_words = sum(dp[n]) % MOD
    
# # # # # # # # # # # # #     return total_balanced_words

# # # # # # # # # # # # # # Read input values
# # # # # # # # # # # # # n = int(input().strip())
# # # # # # # # # # # # # d = int(input().strip())

# # # # # # # # # # # # # # Calculate and print the result
# # # # # # # # # # # # # result = countBalancedWords(n, d)
# # # # # # # # # # # # # print(result)

# # # # # # # # # # # # def countBalancedWords(n, d):
# # # # # # # # # # # #     MOD = 10**9 + 7
    
# # # # # # # # # # # #     # Initialize a 2D DP array
# # # # # # # # # # # #     dp = [[0] * 26 for _ in range(n + 1)]
    
# # # # # # # # # # # #     # Base case: one character words are always balanced
# # # # # # # # # # # #     for i in range(26):
# # # # # # # # # # # #         dp[1][i] = 1
    
# # # # # # # # # # # #     # Fill the DP array
# # # # # # # # # # # #     for length in range(2, n + 1):
# # # # # # # # # # # #         for i in range(26):
# # # # # # # # # # # #             for j in range(max(0, i - d), min(26, i + d + 1)):
# # # # # # # # # # # #                 dp[length][i] = (dp[length][i] + dp[length - 1][j]) % MOD
    
# # # # # # # # # # # #     # Calculate the total number of balanced words of length n
# # # # # # # # # # # #     total_balanced_words = sum(dp[n]) % MOD
    
# # # # # # # # # # # #     return total_balanced_words

# # # # # # # # # # # # # Read input values
# # # # # # # # # # # # n, d = map(int, input().split())

# # # # # # # # # # # # # Calculate and print the result
# # # # # # # # # # # # result = countBalancedWords(n, d)
# # # # # # # # # # # # print(result)


# # # # # # # # # # # # from django.shortcuts import render
# # # # # # # # # # # # from app.exceptions import ObjectNotFoundException, InvalidDataException, ServiceException
# # # # # # # # # # # # class CustomExceptionMiddleware:
# # # # # # # # # # # #     def __init__(self, get_response):
# # # # # # # # # # # #         self.get_response = get_response
# # # # # # # # # # # #     def __call__(self, request):
# # # # # # # # # # # #         try:
# # # # # # # # # # # #             response = self.get_response(request)
# # # # # # # # # # # #         except ObjectNotFoundException as error:
# # # # # # # # # # # #             return render(request, ‘errors/404.html’, {‘error’: error})
# # # # # # # # # # # #         except InvalidDataException as error:
# # # # # # # # # # # #             return render(request, ‘errors/400.html’, {‘error’: error})
# # # # # # # # # # # #         except ServiceException as error:
# # # # # # # # # # # #             return render(request, ‘errors/500.html’, {‘error’: error})
# # # # # # # # # # # #         except Exception as error:
# # # # # # # # # # # #             return render(request, ‘errors/500.html’, {‘error’: error})
# # # # # # # # # # # #         return response
    
# # # # # # # # # # # #     MIDDLEWARE = [
# # # # # # # # # # # #     # ...
# # # # # # # # # # # #     ‘app.middleware.CustomExceptionMiddleware’,
# # # # # # # # # # # #     # ...
# # # # # # # # # # # # ]

# # # # # # # # # # # def reversed_args(f):
# # # # # # # # # # #     def g(*args):
# # # # # # # # # # #         return f(*args[::-1])
# # # # # # # # # # #     return g

# # # # # # # # # # # # Test cases
# # # # # # # # # # # def pow_func(a, b):
# # # # # # # # # # #     return a ** b

# # # # # # # # # # # def cmp_func(a, b):
# # # # # # # # # # #     if a < b:
# # # # # # # # # # #         return -1
# # # # # # # # # # #     elif a == b:
# # # # # # # # # # #         return 0
# # # # # # # # # # #     else:
# # # # # # # # # # #         return 1

# # # # # # # # # # # def join_with(separator, *args):
# # # # # # # # # # #     return separator.join(args)

# # # # # # # # # # # def capitalize_first_and_join(*args):
# # # # # # # # # # #     return ''.join(arg.capitalize() for arg in args)

# # # # # # # # # # # # Creating reversed versions of the functions
# # # # # # # # # # # reversed_pow = reversed_args(pow_func)
# # # # # # # # # # # reversed_cmp = reversed_args(cmp_func)
# # # # # # # # # # # reversed_join = reversed_args(join_with)
# # # # # # # # # # # reversed_capitalize_and_join = reversed_args(capitalize_first_and_join)

# # # # # # # # # # # # Testing the reversed functions
# # # # # # # # # # # print(reversed_pow(2, 3))  # Output: 9
# # # # # # # # # # # print(reversed_cmp(1, 2))  # Output: 1
# # # # # # # # # # # print(reversed_join(",", "you", "are", "the", "best", "coder"))  # Output: "coder, best, the, are, you"
# # # # # # # # # # # print(reversed_capitalize_and_join("first", "second", "third"))  # Output: "THIRDSecondfirst"

# # # # # # # # # # def reversed_args(f):
# # # # # # # # # #     def g(*args):
# # # # # # # # # #         reversed_args = args[::-1]  # Reverse the arguments using slicing
# # # # # # # # # #         return f(*reversed_args)    # Call the original function with reversed arguments
# # # # # # # # # #     return g

# # # # # # # # # # # Sample functions
# # # # # # # # # # def pow(a, b):
# # # # # # # # # #     return a ** b

# # # # # # # # # # def cmp(a, b):
# # # # # # # # # #     if a < b:
# # # # # # # # # #         return -1
# # # # # # # # # #     elif a == b:
# # # # # # # # # #         return 0
# # # # # # # # # #     else:
# # # # # # # # # #         return 1

# # # # # # # # # # def join_with(separator, *args):
# # # # # # # # # #     return separator.join(args)

# # # # # # # # # # def capitalize_first_and_join(*args):
# # # # # # # # # #     capitalized_args = [arg.capitalize() for arg in args]
# # # # # # # # # #     return ''.join(capitalized_args)

# # # # # # # # # # # Creating reversed functions using reversed_args
# # # # # # # # # # reversed_pow = reversed_args(pow)
# # # # # # # # # # reversed_cmp = reversed_args(cmp)
# # # # # # # # # # reversed_join_with = reversed_args(join_with)
# # # # # # # # # # reversed_capitalize_first_and_join = reversed_args(capitalize_first_and_join)

# # # # # # # # # # # Sample inputs
# # # # # # # # # # input_data = [
# # # # # # # # # #     ("pow", 2, 3),
# # # # # # # # # #     ("cmp", 1, 2),
# # # # # # # # # #     ("join_with", "coder", "best", "the", "are", "you"),
# # # # # # # # # #     ("capitalize_first_and_join", "first", "second", "third")
# # # # # # # # # # ]

# # # # # # # # # # # Processing and printing results
# # # # # # # # # # for data in input_data:
# # # # # # # # # #     func_name, *args = data
# # # # # # # # # #     func = globals()[func_name]  # Get the function object from its name
# # # # # # # # # #     reversed_func = globals()["reversed_" + func_name]  # Get the reversed function object
# # # # # # # # # #     result = reversed_func(*args)
# # # # # # # # # #     print(result)

# # # # # # # # # def reversed_args(f):
# # # # # # # # #     def g(*args):
# # # # # # # # #         reversed_args = args[::-1]
# # # # # # # # #         return f(*reversed_args)
# # # # # # # # #     return g

# # # # # # # # # # Sample functions
# # # # # # # # # def pow(a, b):
# # # # # # # # #     return a ** b

# # # # # # # # # def cmp(a, b):
# # # # # # # # #     if a < b:
# # # # # # # # #         return -1
# # # # # # # # #     elif a == b:
# # # # # # # # #         return 0
# # # # # # # # #     else:
# # # # # # # # #         return 1

# # # # # # # # # def join_with(separator, *args):
# # # # # # # # #     return separator.join(args)

# # # # # # # # # def capitalize_first_and_join(*args):
# # # # # # # # #     capitalized_args = [arg.capitalize() for arg in args]
# # # # # # # # #     return ''.join(capitalized_args)

# # # # # # # # # # Mapping function names to their corresponding functions
# # # # # # # # # function_mapping = {
# # # # # # # # #     "pow": pow,
# # # # # # # # #     "cmp": cmp,
# # # # # # # # #     "join_with": join_with,
# # # # # # # # #     "capitalize_first_and_join": capitalize_first_and_join
# # # # # # # # # }

# # # # # # # # # # Read the number of queries
# # # # # # # # # num_queries = int(input("num").strip())

# # # # # # # # # # Process each query
# # # # # # # # # for _ in range(num_queries):
# # # # # # # # #     query = input().strip().split()
# # # # # # # # #     func_name = query[0]
# # # # # # # # #     func_args = query[1:]

# # # # # # # # #     func = function_mapping[func_name]
# # # # # # # # #     reversed_func = reversed_args(func)

# # # # # # # # #     result = reversed_func(*func_args)
# # # # # # # # #     print(result)

# # # # # # # # import io
# # # # # # # # import sys

# # # # # # # # def reversed_args(f):
# # # # # # # #     def g(*args):
# # # # # # # #         reversed_args = args[::-1]
# # # # # # # #         return f(*reversed_args)
# # # # # # # #     return g

# # # # # # # # # Sample functions
# # # # # # # # def pow(a, b):
# # # # # # # #     return a ** b

# # # # # # # # def cmp(a, b):
# # # # # # # #     if a < b:
# # # # # # # #         return -1
# # # # # # # #     elif a == b:
# # # # # # # #         return 0
# # # # # # # #     else:
# # # # # # # #         return 1

# # # # # # # # def join_with(separator, *args):
# # # # # # # #     return separator.join(args)

# # # # # # # # def capitalize_first_and_join(*args):
# # # # # # # #     capitalized_args = [arg.capitalize() for arg in args]
# # # # # # # #     return ''.join(capitalized_args)

# # # # # # # # # Mapping function names to their corresponding functions
# # # # # # # # function_mapping = {
# # # # # # # #     "pow": pow,
# # # # # # # #     "cmp": cmp,
# # # # # # # #     "join_with": join_with,
# # # # # # # #     "capitalize_first_and_join": capitalize_first_and_join
# # # # # # # # }

# # # # # # # # # Provide the input as a multi-line string
# # # # # # # # input_data = """4
# # # # # # # # pow 2 3
# # # # # # # # cmp 1 2
# # # # # # # # join_with coder best the are you,
# # # # # # # # capitalize_first_and_join first second third
# # # # # # # # """

# # # # # # # # # Redirect stdin to the input data
# # # # # # # # sys.stdin = io.StringIO(input_data)

# # # # # # # # # Read the number of queries
# # # # # # # # num_queries = int(input().strip())

# # # # # # # # # Process each query
# # # # # # # # for _ in range(num_queries):
# # # # # # # #     query = input().strip().split()
# # # # # # # #     func_name = query[0]
# # # # # # # #     func_args = query[1:]

# # # # # # # #     func = function_mapping[func_name]
# # # # # # # #     reversed_func = reversed_args(func)

# # # # # # # #     result = reversed_func(*func_args)
# # # # # # # #     print(result)

# # # # # # # import io
# # # # # # # import sys

# # # # # # # def reversed_args(f):
# # # # # # #     def g(*args):
# # # # # # #         reversed_args = args[::-1]
# # # # # # #         return f(*reversed_args)
# # # # # # #     return g

# # # # # # # # Sample functions
# # # # # # # def pow(a, b):
# # # # # # #     return a ** b

# # # # # # # def cmp(a, b):
# # # # # # #     if a < b:
# # # # # # #         return -1
# # # # # # #     elif a == b:
# # # # # # #         return 0
# # # # # # #     else:
# # # # # # #         return 1

# # # # # # # def join_with(separator, *args):
# # # # # # #     return separator.join(args)

# # # # # # # def capitalize_first_and_join(*args):
# # # # # # #     capitalized_args = [arg.capitalize() for arg in args]
# # # # # # #     return ''.join(capitalized_args)

# # # # # # # # Mapping function names to their corresponding functions
# # # # # # # function_mapping = {
# # # # # # #     "pow": pow,
# # # # # # #     "cmp": cmp,
# # # # # # #     "join_with": join_with,
# # # # # # #     "capitalize_first_and_join": capitalize_first_and_join
# # # # # # # }

# # # # # # # # Provide the input as a multi-line string
# # # # # # # input_data = """
# # # # # # # 4
# # # # # # # pow 2 3
# # # # # # # cmp 1 2
# # # # # # # join_with  coder best the are you,
# # # # # # # capitalize_first_and_join first second third
# # # # # # # """

# # # # # # # # Redirect stdin to the input data
# # # # # # # sys.stdin = io.StringIO(input_data)

# # # # # # # # Read the number of queries
# # # # # # # num_queries = int(input().strip())

# # # # # # # # Process each query
# # # # # # # for _ in range(num_queries):
# # # # # # #     query = input().strip().split()
# # # # # # #     func_name = query[0]
# # # # # # #     func_args = query[1:]

# # # # # # #     func = function_mapping[func_name]
# # # # # # #     reversed_func = reversed_args(func)

# # # # # # #     # Convert arguments to integers if needed
# # # # # # #     if func_name == "pow":
# # # # # # #         func_args = list(map(int, func_args))

# # # # # # #     result = reversed_func(*func_args)
# # # # # # #     print(result)

# # # # # # def reversed_args(f):
# # # # # #     def g(*args):
# # # # # #         reversed_args = args[::-1]
# # # # # #         return f(*reversed_args)
# # # # # #     return g

# # # # # # # Sample functions
# # # # # # def pow(a, b):
# # # # # #     return a ** b

# # # # # # def cmp(a, b):
# # # # # #     if a < b:
# # # # # #         return -1
# # # # # #     elif a == b:
# # # # # #         return 0
# # # # # #     else:
# # # # # #         return 1

# # # # # # def join_with(separator, *args):
# # # # # #     return separator.join(args)

# # # # # # def capitalize_first_and_join(*args):
# # # # # #     capitalized_args = [arg.capitalize() for arg in args]
# # # # # #     return ''.join(capitalized_args)

# # # # # # # Mapping function names to their corresponding functions
# # # # # # function_mapping = {
# # # # # #     "pow": pow,
# # # # # #     "cmp": cmp,
# # # # # #     "join_with": join_with,
# # # # # #     "capitalize_first_and_join": capitalize_first_and_join
# # # # # # }

# # # # # # # Read the number of queries
# # # # # # num_queries = int(input())

# # # # # # # Process each query
# # # # # # for _ in range(num_queries):
# # # # # #     query = input().split()
# # # # # #     func_name = query[0]
# # # # # #     func_args = query[1:]

# # # # # #     func = function_mapping[func_name]
# # # # # #     reversed_func = reversed_args(func)

# # # # # #     result = reversed_func(*func_args)
# # # # # #     print(result)

# # # # # def reversed_args(f):
# # # # #     def g(*args):
# # # # #         reversed_args = args[::-1]
# # # # #         return f(*reversed_args)
# # # # #     return g

# # # # # # Sample functions
# # # # # def pow(a, b):
# # # # #     return a ** b

# # # # # def cmp(a, b):
# # # # #     if a < b:
# # # # #         return -1
# # # # #     elif a == b:
# # # # #         return 0
# # # # #     else:
# # # # #         return 1

# # # # # def join_with(separator, *args):
# # # # #     return separator.join(args)

# # # # # def capitalize_first_and_join(*args):
# # # # #     capitalized_args = [arg.capitalize() for arg in args]
# # # # #     return ''.join(capitalized_args)

# # # # # # Mapping function names to their corresponding functions
# # # # # function_mapping = {
# # # # #     "pow": pow,
# # # # #     "cmp": cmp,
# # # # #     "join_with": join_with,
# # # # #     "capitalize_first_and_join": capitalize_first_and_join
# # # # # }

# # # # # # Read the number of queries
# # # # # num_queries = int(input())

# # # # # # Process each query
# # # # # for _ in range(num_queries):
# # # # #     query = input().split()
# # # # #     func_name = query[0]
# # # # #     func_args = query[1:]

# # # # #     if func_name == "join_with":
# # # # #         separator = func_args[0]
# # # # #         args = func_args[1:]
# # # # #         result = function_mapping[func_name](separator, *args)
# # # # #     else:
# # # # #         result = function_mapping[func_name](*func_args)

# # # # #     print(result)

# # # # # def reversed_args(f):
# # # # #     def g(*args):
# # # # #         return f(*reversed(args))
# # # # #     return g

# # # # # # Example functions
# # # # # def pow(a, b):
# # # # #     return a ** b

# # # # # def cmp(a, b):
# # # # #     if a < b:
# # # # #         return -1
# # # # #     elif a == b:
# # # # #         return 0
# # # # #     else:
# # # # #         return 1

# # # # # def join_with(*args):
# # # # #     return ",".join(args)

# # # # # def capitalize_first_and_join(*args):
# # # # #     capitalized_first_word = args[0].upper()
# # # # #     return ''.join([capitalized_first_word] + list(args[1:]))

# # # # # # Creating reversed versions of the example functions
# # # # # reversed_pow = reversed_args(pow)
# # # # # reversed_cmp = reversed_args(cmp)
# # # # # reversed_join_with = reversed_args(join_with)
# # # # # reversed_capitalize_and_join = reversed_args(capitalize_first_and_join)

# # # # # # Testing the reversed functions
# # # # # print(reversed_pow(2, 3))  # Output: 9
# # # # # print(reversed_cmp(1, 2))   # Output: 1
# # # # # print(reversed_join_with('coder' ,'best' ,'the', 'are' ,'you'))  # Output: 'coder, best, the, are, you'
# # # # # print(reversed_capitalize_and_join('first', 'second', 'third'))       # Output: 'THIRDSecondfirst'

# # # # # # Simulated TV show data
# # # # # simulated_data = {
# # # # #     "page": 1,
# # # # #     "per_page": 10,
# # # # #     "total": 4,
# # # # #     "total_pages": 1,
# # # # #     "data": [
# # # # #         {
# # # # #             "name": "Game of Thrones",
# # # # #             "imdb_rating": 9.3
# # # # #         },
# # # # #         {
# # # # #             "name": "Avatar: The Last Airbender",
# # # # #             "imdb_rating": 9.2
# # # # #         },
# # # # #         {
# # # # #             "name": "Hagane no renkinjutsushi",
# # # # #             "imdb_rating": 9.1
# # # # #         },
# # # # #         {
# # # # #             "name": "Shingeki no kyojin",
# # # # #             "imdb_rating": 8.9
# # # # #         }
# # # # #     ]
# # # # # }

# # # # # def bestinGenre(genre):
# # # # #     shows = simulated_data["data"]
# # # # #     highest_rating = -1
# # # # #     best_show = None

# # # # #     for show in shows:
# # # # #         rating = show["imdb_rating"]
# # # # #         if rating > highest_rating or (rating == highest_rating and show["name"] < best_show["name"]):
# # # # #             highest_rating = rating
# # # # #             best_show = show

# # # # #     return best_show["name"]

# # # # # # Sample input
# # # # # genre = "Action"

# # # # # # Call the function with the sample input
# # # # # result = bestinGenre(genre)
# # # # # print(result)

# # # # # def is_subsequence(word, s):
# # # # #     i = j = 0
# # # # #     while i < len(word) and j < len(s):
# # # # #         if word[i] == s[j]:
# # # # #             i += 1
# # # # #         j += 1
# # # # #     return i == len(word)

# # # # # def getValidWord(s, dictionary):
# # # # #     valid_words = [word for word in dictionary if is_subsequence(word, s)]
    
# # # # #     if not valid_words:
# # # # #         return "-1"
    
# # # # #     valid_words.sort()
# # # # #     return valid_words[0]

# # # # # # Sample Input 

# # # # # # s = "ocbms"
# # # # # # dictionary = ["rdnothix", "obms", "qhlrpiaiv", "ms", "jaupx"]

# # # # # s = "zafqz"
# # # # # dictionary = ["dvuyaufe", "gtxbc", "hbckuhyh"]

# # # # # # Call the function with the sample input
# # # # # result = getValidWord(s, dictionary)
# # # # # print(result)

# # # # # class Limit:
# # # # #     limit = 0
    
# # # # #     @classmethod
# # # # #     def set_limit(cls, n):
# # # # #         cls.limit = n
    
# # # # #     @classmethod
# # # # #     def get_limit(cls):
# # # # #         return cls.limit

# # # # # class Product:
# # # # #     product_count = 0
    
# # # # #     def __init__(self, name):
# # # # #         self.name = name
# # # # #         Product.product_count += 1
        
# # # # #         if Product.product_count <= Limit.get_limit():
# # # # #             print(f"{self.name} created")
# # # # #         else:
# # # # #             raise UserLimitExceeded(f"Product {self.name} cannot be created. Maximum {Limit.get_limit()} products allowed")
    
# # # # #     def __del__(self):
# # # # #         Product.product_count -= 1
# # # # #         print(f"{self.name} deleted successfully")
    
# # # # #     @staticmethod
# # # # #     def find_product(name):
# # # # #         if Product.product_count > 0:
# # # # #             return True
# # # # #         else:
# # # # #             return False

# # # # # class UserLimitExceeded(Exception):
# # # # #     def __init__(self, message):
# # # # #         super().__init__(message)

# # # # # # Set initial limit
# # # # # initial_limit = int(input())
# # # # # Limit.set_limit(initial_limit)

# # # # # # Read the number of operations
# # # # # num_operations = int(input())

# # # # # # Process operations
# # # # # for _ in range(num_operations):
# # # # #     operation_parts = input().split()
# # # # #     command = operation_parts[0]
# # # # #     product_name = " ".join(operation_parts[1:])
    
# # # # #     try:
# # # # #         if command == "new":
# # # # #             Product(product_name)
# # # # #         elif command == "del":
# # # # #             if Product.find_product(product_name):
# # # # #                 del_product = Product(product_name)
# # # # #                 del del_product
# # # # #             else:
# # # # #                 print(f"{product_name} not found")
# # # # #     except UserLimitExceeded as e:
# # # # #         print(e)


# # # # # def getKCount(s):
# # # # #     count = 0
# # # # #     n = 1  
# # # # #     import pdb;pdb.set_trace()
# # # # #     while True:
# # # # #         numerator = 2 * s - n * (n - 1)
# # # # #         denominator = 2 * n
        
# # # # #         if numerator <= 0:
# # # # #             break
        
# # # # #         if numerator % denominator == 0:
# # # # #             k = numerator // denominator
# # # # #             if k >= 1:
# # # # #                 count += 1
        
# # # # #         n += 1
    
# # # # #     return count

# # # # # # Test cases
# # # # # print(getKCount(125))  # Output: 4
# # # # # print(getKCount(5))    # Output: 2

# # # # # import requests
# # # # # def findCountries(keyword, region):
# # # # #     all_data=[]
# # # # #     base_url = f'https://jsonmock.hackerrank.com/api/countries/search/region-{region}'
# # # # #     page = 1
# # # # #     loop=True
# # # # #     result = []
# # # # #     while loop:
# # # # #         data = requests.get(f'{base_url}?name={keyword}&page={page}')
# # # # #         if data.json()['total_pages']==page:
# # # # #             loop=False    
# # # # #         if data.json()['total_pages']!=page:
# # # # #             page+=1
# # # # #         all_data.extend(data.json()['data'])
# # # # #         # print(all_data)
# # # # #     sorted_item=sorted(all_data,key=lambda item:item['population'])
# # # # #     for info in sorted_item:
# # # # #         result.append(f"{info['name']},{info['population']}")
# # # # #     print(result)
# # # # #     return result

# # # # # findCountries("Europe","de")

# # # # # def countBalancedWords(n, d):
# # # # #     MOD = 10**9 + 7

# # # # #     # Initialize dp for length 1
# # # # #     dp = [[0] * 26 for _ in range(n + 1)]
# # # # #     for j in range(26):
# # # # #         dp[1][j] = 1

# # # # #     # Build up the dp array
# # # # #     for i in range(2, n + 1):
# # # # #         for j in range(26):
# # # # #             for k in range(max(0, j - d), min(26, j + d + 1)):
# # # # #                 dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

# # # # #     # Sum up the final result
# # # # #     total_balanced_words = sum(dp[n]) % MOD
# # # # #     return total_balanced_words

# # # # # # Sample Input 0
# # # # # n = 2
# # # # # d = 2
# # # # # print(countBalancedWords(n, d))  # Output: 124

# # # # # # Sample Input 1
# # # # # n = 3
# # # # # d = 1
# # # # # print(countBalancedWords(n, d))  # Output: 224

# # # # # n= 2
# # # # # d = 3
# # # # # print(countBalancedWords(n, d)) # Output: 170
# # # # import requests
# # # # # def getRelevantFoodOutlets(city, maxCost):
# # # # #     page = 1
# # # # #     relevant_outlets = []
# # # # #     while True:
# # # # #         url = f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={page}"
# # # # #         response = requests.get(url)
# # # # #         data = response.json()

# # # # #         outlets = data["data"]
# # # # #         if not outlets:
# # # # #             break

# # # # #         for outlet in outlets:
# # # # #             if outlet["estimated_cost"] <= maxCost:
# # # # #                 relevant_outlets.append(outlet["name"])

# # # # #         total_pages = data["total_pages"]
# # # # #         if page >= total_pages:
# # # # #             break

# # # # #         page += 1

# # # # #     return relevant_outlets

# # # # # # Sample Input
# # # # # city="Houston"
# # # # # maxCost=30

# # # # # # city = "Denver"
# # # # # # maxCost = 50


# # # # # # Call the function with the sample input
# # # # # result = getRelevantFoodOutlets(city, maxCost)
# # # # # for outlet_name in result:
# # # # #     print(outlet_name)
    
    
# # # # # def getRelevantFoodOutlets(city, maxCost):
# # # # #     loop=True
# # # # #     pageNumber =1
# # # # #     total_data =[]
# # # # #     while loop:
# # # # #         data=requests.get(f'https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={pageNumber}')
# # # # #         info= data.json()
# # # # #         if pageNumber==info['total_pages']:
# # # # #             loop= False
# # # # #         if pageNumber<info['total_pages']:
# # # # #             pageNumber=pageNumber+1
# # # # #         total_data.extend(info['data'])
# # # # #     result = []
# # # # #     for data in total_data:
# # # # #         if data['estimated_cost'] <= maxCost: 
# # # # #             result.append(data['name'])
# # # # #     return result
# # # # # # Sample Input
# # # # # city="Houston"
# # # # # maxCost=30

# # # # # # city = "Denver"
# # # # # # maxCost = 50

# # # # # # Call the function with the sample input
# # # # # result=getRelevantFoodOutlets(city, maxCost)
# # # # # for outlet_name in result:
# # # # #     print(outlet_name)


# # # # # def findMaximumGreatness(arr):
# # # # #     n = len(arr)
# # # # #     freq = [0] * (n + 1)

# # # # #     for num in arr:
# # # # #         if num <= n:
# # # # #             freq[num] += 1

# # # # #     max_greatness = 0

# # # # #     for i in range(n, 0, -1):
# # # # #         freq[i] += freq[i]

# # # # #         if freq[i] >= i:
# # # # #             max_greatness = i
# # # # #             break

# # # # #     return max_greatness

# # # # # # Sample Input
# # # # # arr = [4, 1, 6, 3]
# # # # # print(findMaximumGreatness(arr))  # Output: 3

# # # # # def findMaximumGreatness(arr):
# # # # #     arr.sort()  # Sort the array in ascending order
# # # # #     n = len(arr)
    
# # # # #     max_greatness = 0

# # # # #     for i in range(n):
# # # # #         if arr[i] > i + 1:
# # # # #             max_greatness = i + 1

# # # # #     return max_greatness

# # # # # # Sample Input
# # # # # arr = [4, 1, 6, 3]
# # # # # print(findMaximumGreatness(arr))  # Output: 3

# # # # # arr = [1, 2, 6, 3, 2, 1]
# # # # # print(findMaximumGreatness(arr))  # Output: 4

# # # # # def findMaximumGreatness(arr):
# # # # #     backup_list = arr[:]
# # # # #     arr.sort()
# # # # #     total = 0
# # # # #     for i in range (len (backup_list)):
# # # # #         for jad in range(len(arr)):
# # # # #             if arr[jad] > backup_list[i]:
# # # # #                 arr.pop(jad)
# # # # #                 total +=1
# # # # #                 break
# # # # #     return total
# # # # # arr = [1, 2, 6, 3, 2, 1]
# # # # # print(findMaximumGreatness(arr))

# # # # # arr = [4, 1, 6, 3]
# # # # # print(findMaximumGreatness(arr))

# # # # # def findPoint(lines):
# # # # #     import pdb;pdb.set_trace()
# # # # #     min_distance = float('inf')
# # # # #     px, py = None, None
# # # # #     min_x, min_y = float('inf'), float('inf')

# # # # #     for line in lines:
# # # # #         x1, y1, x2, y2 = line
# # # # #         mx = (x1 + x2) // 2
# # # # #         my = (y1 + y2) // 2
# # # # #         distance = abs(mx - x1) + abs(mx - x2) + abs(my - y1) + abs(my - y2)

# # # # #         if distance < min_distance or (distance == min_distance and (mx < min_x or (mx == min_x and my < min_y))):
# # # # #             min_distance = distance
# # # # #             px, py = mx, my
# # # # #             min_x, min_y = mx, my

# # # # #     return [px, py]

# # # # # # Example usage:
# # # # # lines = [[4, 2, 4, 5], [3, 3, 5, 3], [0, 3, 0, 4]]
# # # # # result = findPoint(lines)
# # # # # print(result)  # Output should be [3, 3]

# # # # def findPoint(lines):
# # # #     min_distance = float('inf')
# # # #     px, py = None, None
# # # #     min_x, min_y = float('inf'), float('inf')

# # # #     for line in lines:
# # # #         import pdb;pdb.set_trace()
# # # #         x1, y1, x2, y2 = line
# # # #         mx = (x1 + x2) // 2
# # # #         my = (y1 + y2) // 2
# # # #         distance = abs(mx - x1) + abs(mx - x2) + abs(my - y1) + abs(my - y2)

# # # #         if distance < min_distance or (distance == min_distance and (mx < min_x or (mx == min_x and my < min_y))):
# # # #             min_distance = distance
# # # #             px, py = mx, my
# # # #             min_x, min_y = mx, my

# # # #     return [px, py]

# # # # # Example usage:
# # # # lines = [[4, 2, 4, 5], [3, 3, 5, 3], [0, 3, 0, 4]]
# # # # lines=[[2,4,2,0],[2,1,0,1],[4,3,4,4],[5,5,4,5]]
# # # # result = findPoint(lines)
# # # # print(result)  # Output should be [3, 3]

# # # # def findPoint(lines):
# # # #     # Find the minimum and maximum x and y coordinates of line segments.
# # # #     min_x = min(line[0] for line in lines)
# # # #     max_x = max(line[2] for line in lines)
# # # #     min_y = min(line[1] for line in lines)
# # # #     max_y = max(line[3] for line in lines)

# # # #     min_distance = float('inf')
# # # #     px, py = None, None

# # # #     for x in range(min_x, max_x + 1):
# # # #         for y in range(min_y, max_y + 1):
# # # #             distance = 0
# # # #             for line in lines:
# # # #                 x1, y1, x2, y2 = line
# # # #                 # Calculate Manhattan distance from point (x, y) to line segment.
# # # #                 distance += abs(x - x1) + abs(x - x2) + abs(y - y1) + abs(y - y2)
            
# # # #             if distance < min_distance or (distance == min_distance and (x < px or (x == px and y < py))):
# # # #                 min_distance = distance
# # # #                 px, py = x, y

# # # #     return [px, py]

# # # # # Example usage:
# # # # lines = [[4, 2, 4, 5], [3, 3, 5, 3], [0, 3, 0, 4]]
# # # # lines=[[2,4,2,0],[2,1,0,1],[4,3,4,4],[5,5,4,5]]
# # # # result = findPoint(lines)
# # # # print(result)  # Output should be [3, 3]


# # # import requests

# # # def bestinGenre(genre):
# # #     url = f"https://jsonmock.hackerrank.com/api/tvseries?genre={genre}"
# # #     response = requests.get(url)
    
# # #     if response.status_code != 200:
# # #         return "No shows found for the given genre"

# # #     data = response.json()
# # #     shows = data["data"]

# # #     highest_rating = -1
# # #     best_show = None

# # #     for show in shows:
# # #         rating = show["imdb_rating"]
# # #         if rating > highest_rating or (rating == highest_rating and show["name"] < best_show["name"]):
# # #             highest_rating = rating
# # #             best_show = show

# # #     return best_show["name"]

# # # # Sample input
# # # genre = "Action"

# # # # Call the function with the sample input
# # # result = bestinGenre(genre)
# # # print(result)


# # import requests

# # def bestinGenre(genre):
# #     import pdb;pdb.set_trace()
# #     base_url = "https://jsonmock.hackerrank.com/api/tvseries"
# #     page = 1
# #     highest_rating = float('-inf')
# #     best_series = None
    
# #     while True:
# #         url = f"{base_url}?page={page}&genre={genre}"
# #         response = requests.get(url)
# #         data = response.json()
        
# #         # Check if there are no more pages to fetch.
# #         if page < data['total_pages']:
# #             break
        
# #         series_data = data['data']
        
# #         for series in series_data:
# #             rating = series['imdb_rating']
# #             name = series['name']
            
# #             if rating > highest_rating or (rating == highest_rating and name < best_series):
# #                 highest_rating = rating
# #                 best_series = name
        
# #         page -= 1
    
# #     return best_series

# # # Example usage:
# # genre = "Action"
# # result = bestinGenre(genre)
# # print(result)  # Output should be "Game of Thrones" based on the provided sample input and output

# # import requests

# # def bestinGenre(genre):
# #     base_url = "https://jsonmock.hackerrank.com/api/tvseries"
# #     page = 1
# #     highest_rating = float('-inf')
# #     best_series = None
    
# #     while True:
# #         import pdb;pdb.set_trace()
# #         url = f"{base_url}?page={page}"
# #         response = requests.get(url)
# #         data = response.json()
        
# #         series_data = data['data']
        
# #         for series in series_data:
# #             series_genre = series['genre']
            
# #             # Check if the series belongs to the specified genre.
# #             if genre in series_genre:
# #                 rating = series['imdb_rating']
# #                 name = series['name']
                
# #                 if rating > highest_rating or (rating == highest_rating and name < best_series):
# #                     highest_rating = rating
# #                     best_series = name
        
# #         # Move to the next page.
# #         page += 1
        
# #         # Check if there are no more pages to fetch.
# #         if page > data['total_pages']:
# #             break

# #     return best_series

# # # Example usage:
# # genre = "Action"
# # result = bestinGenre(genre)
# # print(result)  # Output should be "Game of Thrones" based on the provided sample input and output

# # def reverse_list(arr):
# #     left = 0
# #     right = len(arr) - 1
# #     print(arr[right])
# #     while left < right:
# #         arr[left], arr[right] = arr[right], arr[left]
# #         print(arr[left], arr[right])
# #         print(arr[right], arr[left])
# #         left += 1
# #         right -= 1
# # my_list = [1, 2, 3, 4, 5]
# # reverse_list(my_list)
# # print(my_list) 
 
# # nums=[1,2,3,1]
# # k=3
# # for i in range(0,len(nums)-1):
# #     print(nums[i])
# #     for j in range(i+1,len(nums)):
# #         print(nums[j])
# #         if nums[i]==nums[j]:
# #             if abs(i - j) <= k:
# #                 print("true")
# #         else:
# #             print("false")

# def findMaximumGreatness(arr):
#     backup_list = arr[:]
#     arr.sort()
#     total = 0
#     for i in range (len (backup_list)):
#         for jad in range(len(arr)):
#             if arr[jad] > backup_list[i]:
#                 arr.pop(jad)
#                 total +=1
#                 break
#     return total
# arr = [1, 2, 6, 3, 2, 1]
# print(findMaximumGreatness(arr))

# # arr = [4, 1, 6, 3]
# # print(findMaximumGreatness(arr))


# def findMinimumPrice(price, m):
#     # Sort the prices in ascending order.
#     price.sort()
    
#     # Apply the discount coupons to the most expensive items.
#     for i in range(m):
#         price[-1] = price[-1] // 2
#         price.sort()  # Re-sort the prices after applying the discount.
    
#     # Calculate and return the total minimum price.
#     return sum(price)

# Example usage:
if __name__ == '__main__':
    price_count = int(input().strip())
    price = []
    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)
    m = int(input().strip())
    result = findMinimumPrice(price, m)
    print(result)

# def findMinimumPrice(price, m):
#     n = len(price)
#     total_cost = sum(price)
#     import pdb;pdb.set_trace()
#     # Create a list to keep track of the discounted prices
#     discounted_prices = price[:]
    
#     # Sort the items by their discounted prices in ascending order
#     sorted_items = sorted(range(n), key=lambda i: discounted_prices[i] // 2)
    
#     for i in sorted_items:
#         if m == 0:
#             break  # No more coupons to use
        
#         discount = min(discounted_prices[i] // 2, price[i] // 2)
#         if discount < discounted_prices[i]:
#             total_cost -= (discounted_prices[i] - discount)
#             discounted_prices[i] = discount
#             m -= 1

#     return total_cost

# # Example usage:
# n = 3
# price = [1, 2, 3]
# m = 1
# result = findMinimumPrice(price, m)
# print(result)  # Output should be 4

# def findMinimumPrice(price, m):
#     n = len(price)
    
#     # Sort the prices in descending order
#     price.sort(reverse=True)
    
#     total_cost = 0
    
#     for i in range(n):
#         # Check if we have enough coupons to use
#         if m > 0:
#             # Apply the coupon to reduce the price to floor(price[i]/2)
#             discounted_price = price[i] // 2
#             if discounted_price <= price[i]:
#                 total_cost += discounted_price
#                 m -= 1
#             else:
#                 total_cost += price[i]
#         else:
#             # No more coupons left, buy at regular price
#             total_cost += price[i]
    
#     return total_cost

# # Example usage:
# n = 3
# price = [1, 1, 1]
# m = 0
# result = findMinimumPrice(price, m)
# print(result)  # Output should be 4






