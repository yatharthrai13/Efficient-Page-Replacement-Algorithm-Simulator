# Efficient-Page-Replacement-Algorithm-Simulator
Efficient Page Replacement Algorithm Simulator

Team Members:

1.GOPALA TUSHAL KUMAR

2.DHANUN JAYA KUMAR GOLIVE

3.AJAY PASUPALETI

Project Description:

Efficient Page Replacement Algorithm Simulator is a tool designed to analyze and compare various page replacement algorithms used in operating systems. This simulator helps understand how different algorithms handle memory management and optimize page faults.

Features:

1.Simulates multiple page replacement algorithms: FIFO, LRU, LFU, MFU, and Optimal

2.Allows users to input page references manually or generate them randomly

3.Provides a detailed output of memory states after each page reference

4.Calculates and displays page faults, page hits, miss ratio, and hit ratio

5.Generates a comparative visualization of algorithm performance using Matplotlib

Technologies:

Programming Language: Python

Libraries and Tools: Matplotlib, Collections (Deque & Counter), Random

Other Tools: GitHub for version control

Installation: 1.Install IDLE

2.pip install matplotlib

Usage:

1.Enter the length of the page reference string.

2.Choose to enter page references manually or generate them randomly.

3.Specify the number of frames.

4.Select the algorithms to simulate.

5.View the output with page hits, faults, and a comparison graph.

Example Output:

Generated Page References: 1,2,3,2,1,4,5,2,1,3,4,5

Enter the number of frames: 3

Selected Algorithms: FIFO, LRU

FIFO Algorithm:

1 : 1

2 : 1 2

3 : 1 2 3

2 : 1 2 3 (hit)

Page Faults: 8, Page Hits: 4

Miss Ratio: 66.67%, Hit Ratio: 33.33%

Future Enhancements:

1.Implement more advanced algorithms like NRU and Working Set

2.Add GUI for better user experience

3.Extend simulation to real-time process memory management
