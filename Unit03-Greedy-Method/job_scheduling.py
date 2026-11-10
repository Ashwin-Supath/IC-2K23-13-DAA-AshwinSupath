import sys
from pathlib import Path
import random

# Dynamically link the root folder to access the analyzer
root_dir = str(Path(__file__).resolve().parents[2])
sys.path.insert(0, root_dir)
from Complexity_analyser import PerformanceAnalyzer

def job_scheduling(jobs):
    # jobs is a list of tuples: (job_id, deadline, profit)
    # Sort jobs in descending order based on profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Find the maximum deadline to determine the size of our time slot array
    max_deadline = max(jobs, key=lambda x: x[1])[1] if jobs else 0
    
    # Track free time slots (-1 indicates an empty slot)
    slots = [-1] * (max_deadline + 1)
    
    total_profit = 0
    
    for job in jobs:
        job_id, deadline, profit = job
        # Iterate backwards from the job's deadline to find the latest available slot
        for j in range(min(max_deadline, deadline), 0, -1):
            if slots[j] == -1:
                slots[j] = job_id
                total_profit += profit
                break
                
    return total_profit

if __name__ == "__main__":
    # Testing sizes scaled down due to O(N^2) worst-case time complexity
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    
    # Generate list of (Job ID, Deadline, Profit). 
    # Max deadline is bounded by N to simulate realistic constraints.
    data_generator = lambda n: [(i, random.randint(1, n), random.randint(10, 500)) for i in range(n)]
    
    PerformanceAnalyzer.run_and_plot(
        algorithms=[job_scheduling],
        sizes=sizes,
        data_generator=data_generator,
        title="Job Scheduling Performance",
        ylabel="Time (seconds) - O(N^2)"
    )