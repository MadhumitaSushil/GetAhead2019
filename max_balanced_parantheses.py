def max_balanced_parantheses(seq):
    """
    Given a string of parentheses, find the size of the longest contiguous substring of balanced parentheses.
    Parentheses are considered balanced when there is a valid closing parenthesis for an opening one.

    Example:

    In this string: ())(()), the longest continuous set would be 4 characters long (the last 4 characters of the input):
    For )(()))))((((() , the max length would be 4:
    """

    maxlen = 0
    last_idx = -1

    stack = list()

    for i in range(len(seq)):
        if seq[i] == '(':
            stack.append(i)  # push index to stack if opening parenthesis
        elif seq[i] == ')':
            if not len(stack):
                continue  # discard symbol if no current matching opening parenthesis in stack

            cur_len = i - stack.pop() + 1  # pop the last open parenthesis and calculate valid length

            if last_idx == i - cur_len:  # if the current subsequence is a continuation of the last valid subsequence
                maxlen += cur_len
                last_idx = i  # tracking last symbol of current valid subsequence
            elif cur_len >= maxlen:  # if the current subsequence is longer than previous longest subsequece
                maxlen = cur_len
                last_idx = i  # tracking last symbol of current valid subsequence

    return maxlen


def longest_balanced(string):
    """
    provided solution -- handles '()()' case differently as maxlen 2
    :param string: string to evaluate
    :return: longest balanced parantheses length
    """
    stack = []  # O(n) space.
    longest = 0
    for i, char in enumerate(string):  # O(n) time.
        if char == '(':
            # Remember index of the opening parenthesis.
            stack.append(i)
        elif char == ')':
            # If we previously encountered an opening parenthesis,
            if stack:
                # We recall the index of the last one that hasn't been matched yet.
                open_i = stack.pop()
                # And compute the distance between them.
                # All the parentheses between these two must have been balanced!
                length = i - open_i + 1
                # Keep track of the longest encountered so far
                if length > longest:
                    longest = length
    # And return it.
    return longest


if __name__ == '__main__':

    assert(max_balanced_parantheses('())(())') == 4)
    assert(max_balanced_parantheses(')(()))))((((()') == 4)
    assert(max_balanced_parantheses('()()') == 4)
    assert(max_balanced_parantheses('(()())') == 6)
    assert(max_balanced_parantheses('') == 0)
    assert(max_balanced_parantheses(')') == 0)
    assert(max_balanced_parantheses('(') == 0)
    assert(max_balanced_parantheses(')(') == 0)
    assert(max_balanced_parantheses('()') == 2)
    assert(max_balanced_parantheses('(((((') == 0)
    assert(max_balanced_parantheses(')))))') == 0)
    assert(max_balanced_parantheses(')))))()') == 2)
    assert(max_balanced_parantheses('(((()') == 2)
    assert(max_balanced_parantheses('()((()') == 2)
    assert(max_balanced_parantheses('()(((') == 2)
