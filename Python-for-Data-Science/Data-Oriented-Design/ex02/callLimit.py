# callLimit(limit) is called with the specified limit.
# Inside callLimit, a new function callLimiter is defined.
# This function takes function as an argument.
# When you decorate a function with @callLimit(limit),
# it's essentially equivalent to function = callLimit(limit)(function).
# So, function is passed as an argument to callLimiter.
# Within callLimiter, function is accessible as it's part of the closure.
# This allows callLimiter to wrap around function
#  and control its execution based on the given limit.

def callLimit(limit: int):
    """Returns a decorator that limits the number
of calls to the decorated function."""
    count = 0

    def callLimiter(function):
        """Decorator function that limits the number
of calls to the decorated function."""
        def limit_function(*args: any, **kwds: any):
            """Wrapper function that checks if the call limit is
exceeded before calling the decorated function."""
            try:
                nonlocal count
                count += 1

                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise Exception(function, "call too many times")

            except Exception as error:
                print("Error:", error)
        return limit_function
    return callLimiter


def main():

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
