# topics: recursion, hashes, stacks

# time: O(9^n)
# space: O(n) (not sure)

def generate_all_n_pairs_of_valid_parentheses(n) -> list:
    
    # store the order of parentheses in a stack
    # store the current combination in a stack
    # store the count of all parentheses in a hashmap
    # store the pairs of parentheses in a hashmap for lookup

    # TODO:
    # make a recursive backtracking function

        # can only place an opening parenthesis if its count is lower than n.
        # can only place a closing parenthesis if its count is lower than the count of opening parentheses (of its type)
            # the type of the closing parenthesis can easily be decided by what is the latest element in the order stack

        # if all parentheses' counts are n, return
        # in a for loop, call the recursive function, and then backtrack

    parentheses_pairs = {"(" : ")",
                         "[" : "]",
                         "{" : "}",}
    
    current_combination = []
    parentheses_order = []
    parentheses_count = {"(" : 0,
                         "[" : 0,
                         "{" : 0,
                         ")" : 0,
                         "]" : 0,
                         "}" : 0}

    result = []
    
    def backtrack():
        if all(i == n for i in parentheses_count.values()): # could be more efficient if it only counted the closing parentheses
            result.append(''.join(current_combination))
            return
        
        for i in "([{":
            if parentheses_count[i] < n:
                current_combination.append(i)
                parentheses_order.append(i)
                parentheses_count[i] += 1

                backtrack()

                current_combination.pop()
                parentheses_order.pop()
                parentheses_count[i] -= 1
                
        if not parentheses_order:
            return
        else:
            curr_opening_parenthesis = parentheses_order[-1]
            curr_closing_parenthesis = parentheses_pairs[parentheses_order[-1]]
            
            if parentheses_count[curr_opening_parenthesis] > parentheses_count[curr_closing_parenthesis]: 
                current_combination.append(curr_closing_parenthesis)
                parentheses_order.pop()
                parentheses_count[curr_closing_parenthesis] += 1

                backtrack()

                current_combination.pop()
                parentheses_order.append(curr_opening_parenthesis)
                parentheses_count[curr_closing_parenthesis] -= 1

    backtrack()
    return result


r = generate_all_n_pairs_of_valid_parentheses(1)
print(r)
