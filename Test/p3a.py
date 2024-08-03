#3- max element in stack


def process_queries(queries):
    stack = []
    max_stack = []
    result = []
    
    for query in queries:
        parts = query.split()
        q_type = int(parts[0])
        
        if q_type == 1:
            x = int(parts[1])
            stack.append(x)
            # Push to max_stack if necessary
            if not max_stack or x >= max_stack[-1]:
                max_stack.append(x)
        
        elif q_type == 2:
            if stack:
                top_element = stack.pop()
                if top_element == max_stack[-1]:
                    max_stack.pop()
        
        elif q_type == 3:
            if max_stack:
                result.append(max_stack[-1])
    
    return result


num_queries = int(input('Enter the number of queries:'))
queries = list(int('Enter the queries:'))

output = process_queries(queries)
for res in output:
    print(res)
