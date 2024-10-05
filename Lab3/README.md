Exam Scheduling with Graph Coloring and Heuristics

Overview

This project solves an exam scheduling problem using graph coloring with two heuristics:

	•Minimum Remaining Values (MRV)
	•Degree Heuristic

The graph represents exams (nodes) and conflicts (edges) between exams with shared students. The objective is to assign time slots to exams while avoiding conflicts.

Features

	•Graph Representation: Exams are nodes, and conflicts are edges.
	•Heuristics:
	•MRV: Selects the exam with the fewest valid time slots.
	•Degree Heuristic: Selects the exam with the most conflicts.
	•Backtracking Algorithm: Used to find a valid time slot assignment.
	•Visualization: Displays the graph with exams colored based on their assigned time slots.