def PRT():
    """Main function."""
    # Print the title of the program
    print("Park Run Timer")
    print("~~~~~~~~~~~~~~")
    
    # Print message to start the program
    print("Let's go!")
    
    # Initialize variables 
    total_runners = 0
    total_time = 0
   # Initialize fastest_time to infinity to track the fastest running time
    fastest_time = float('inf') 
    slowest_time = 0
    fastest_runner = 0
    
    # Loop to take input from user until the word 'END' is entered
    while True:
        line = input(">")
        if line == 'END' or line == 'End' or line == 'end':
            break
        try:
            # Split the input line into runner number and elapsed time
            runner_no, elapsed_time = line.split('::')
            # Convert elapsed time and runner number to an integer
            elapsed_time = int(elapsed_time)
            runner_no = int(runner_no)
            
            # Update fastest time and runner if current time is faster
            if elapsed_time < fastest_time:
                fastest_time = elapsed_time
                fastest_runner = runner_no
                
            # Update slowest time if current time is slower
            if elapsed_time > slowest_time:
                slowest_time = elapsed_time
                
            # Increment total runners and total time
            total_runners += 1
            total_time += elapsed_time
            
        except:
            # Print message if there is an error in the input data
            print("Error in data stream. Ignoring. Carry on.")
            
    # If no runners were entered, print a message
    if total_runners == 0:
        print("No data found. Nothing to do. What a pity.")
    else:
        # Calculate and print average time
        avg_time = total_time / total_runners
        minutes = avg_time // 60
        seconds = avg_time % 60
        print("Total Runners:",total_runners)
        
        #To check whether the elapsed time is in minute or minutes
        if minutes == 1.0:
            print("Average Time:",minutes,"minute,",seconds,"seconds")
        else:
            print("Average Time:",minutes,"minutes,",seconds,"seconds")
            
       
        # Convert fastest time to minutes and seconds and print
        minutes_fas = fastest_time // 60
        seconds_fas = fastest_time % 60
        if minutes_fas == 1:
            print("Fastest Time:",minutes_fas,"minute,",seconds_fas,"seconds")
        else:
            print("Fastest Time:",minutes_fas,"minutes,",seconds_fas,"seconds")
            
        
        # Convert slowest time to minutes and seconds and prints
        minutes_slo = slowest_time // 60
        seconds_slo = slowest_time % 60
        if minutes_slo == 1:
            print("Slowest Time:",minutes_slo,"minute,",seconds_slo,"seconds")
        else:
            print("Slowest Time:",minutes_slo,"minutes,",seconds_slo,"seconds")
            
        
        # Print the runner with the fastest time
        print("Best Time Here: Runner#",fastest_runner)
PRT()
