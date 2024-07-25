import Visualizer
import level3
import ReadInput

file_path = 'input.txt'
n, m, time_limit, fuel_capacity, maze, positions = ReadInput.read_input_file(file_path)

start = positions['S']  # Starting point 'S'
goal = positions['G']  # Goal point 'G'
path = level3.a_star_fuel(start, goal, time_limit, fuel_capacity, maze)
visualizer = Visualizer.Visualizer(maze)
if path:
    print("Path found:", path)
    total_cost = sum(level3.cost_to_move() for i in range(len(path)-1))
    print(f"Total cost: {total_cost}")
    for node in path:
        visualizer.update_current(node)
        visualizer.draw_screen()
        visualizer.root.after(200)
    visualizer.root.mainloop()
else:
    print("No path found within the given constraints.")