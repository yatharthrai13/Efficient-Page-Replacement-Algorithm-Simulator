import matplotlib.pyplot as plt
from collections import deque, Counter

# FIFO Page Replacement Algorithm
def fifo(pages, frames):
    memory, page_faults, page_hits = deque(), 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                memory.popleft()
            memory.append(page)
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# LRU Page Replacement Algorithm
def lru(pages, frames):
    memory, page_faults, page_hits = [], 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
            memory.remove(page)
        else:
            page_faults += 1
            if len(memory) == frames:
                memory.pop(0)
        memory.append(page)
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# LFU Page Replacement Algorithm
def lfu(pages, frames):
    memory, freq, page_faults, page_hits = [], Counter(), 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                least_used = min(memory, key=lambda p: freq[p])
                memory.remove(least_used)
            memory.append(page)
        freq[page] += 1
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# MFU Page Replacement Algorithm
def mfu(pages, frames):
    memory, freq, page_faults, page_hits = [], Counter(), 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                most_used = max(memory, key=lambda p: freq[p])
                memory.remove(most_used)
            memory.append(page)
        freq[page] += 1
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# Optimal Page Replacement Algorithm
def optimal(pages, frames):
    memory, page_faults, page_hits = [], 0, 0
    frame_updates = []
    
    for i, page in enumerate(pages):
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                future_use = {}
                for mem_page in memory:
                    try:
                        future_use[mem_page] = pages[i+1:].index(mem_page)
                    except ValueError:
                        future_use[mem_page] = float('inf')
                page_to_replace = max(future_use, key=future_use.get)
                memory.remove(page_to_replace)
            memory.append(page)
        
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    
    return page_faults, page_hits, frame_updates

# Plotting results
def plot_results(results):
    labels, faults, hits = zip(*[(algo, faults, hits) for algo, faults, hits, _ in results])
    plt.bar(labels, faults, color='red', label='Page Faults')
    plt.bar(labels, hits, bottom=faults, color='green', label='Page Hits')
    plt.xlabel("Algorithms")
    plt.ylabel("Counts")
    plt.title("Page Replacement Algorithm Comparison")
    plt.legend()
    plt.show()

# User input handling
def get_user_input():
    length = int(input("Enter the length of the trace: "))
    manual = input("Do you want to enter pages manually? (y/n): ").strip().lower()
    
    if manual == 'y':
        pages = list(map(int, input("Enter space-separated page references: ").replace(",", " ").split()))
    else:
        import random
        pages = [random.randint(1, 10) for _ in range(length)]
        print("Generated Page References:", pages)

    frames = int(input("Enter the number of frames: "))
    
    algorithms = {"1": fifo, "2": lru, "3": lfu, "4": mfu, "5": optimal}
    print("Select algorithms to run:")
    print("1. FIFO\n2. LRU\n3. LFU\n4. MFU\n5. Optimal\n6. Run All")
    selection = input("Enter your choice (comma-separated numbers, e.g., 1,2,3,4,5): ")
    selected_algos = selection.replace(" ", "").split(",")

    return pages, frames, selected_algos, algorithms

# Main function to execute selected algorithms
def main():
    pages, frames, selected_algos, algorithms = get_user_input()
    results = []
    
    for algo in selected_algos:
        if algo == "6":
            results = [(name.upper(), *func(pages, frames)) for name, func in algorithms.items()]
            break
        elif algo in algorithms:
            name, func = list(algorithms.items())[int(algo) - 1]
            faults, hits, frame_updates = func(pages, frames)
            results.append((name.upper(), faults, hits, frame_updates))

    for name, faults, hits, frame_updates in results:
        total = faults + hits
        print(f"\n{name} Algorithm")
        for update in frame_updates:
            print(update)
        print(f"\nPage Faults: {faults}, Page Hits: {hits}")
        print(f"Miss Ratio: {faults / total:.2%}, Hit Ratio: {hits / total:.2%}")

    plot_results(results)

if __name__ == "__main__":
    main()
