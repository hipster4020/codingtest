def generator():
    a = [1, 2, 3]
    for i in a:
        print(i)
        yield i
        
def main():
    gen = generator()
    
    for i in range(10):
        next(gen)
    
if __name__ == "__main__":
    main()