from app_initializer import process_line

if __name__ == '__main__':
    file = open("employees_input.txt", "r")
    for count,line in enumerate(file):
        process_line(line, count)
        
