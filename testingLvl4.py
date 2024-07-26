import Visualizer
import level4
import ReadInput

if __name__ == '__main__':
    file_path = 'input1_level4.txt'
    n, m, time_limit, fuel_capacity, raw_maze, maze, starts, goals = ReadInput.read_input_file(file_path)
    
    agents = [
        level4.Agent(starts[0], goals[0], fuel_capacity, time_limit, is_main=True, name="S"),
        level4.Agent(starts[1], goals[1], fuel_capacity, time_limit, name="S1"),
        level4.Agent(starts[2], goals[2], fuel_capacity, time_limit, name="S2"),
    ]

    # Find the path using WHCA*
    path = level4.whca_star(agents, maze, fuel_capacity)
    path = level4.get_agent_stop(path, agents, maze)
    visuals =  Visualizer.Visualizer()
    
    visuals.set_map(raw_maze)
    
    for i, point in enumerate(starts):
        visuals.add_point(point, 'S' if i == 0 else 'S' + str(i))
        
    for i, point in enumerate(goals):
        visuals.add_point(point, 'G' if i == 0 else 'G' + str(i))
        
    visuals.make_boxes()
    
    # print(visuals.maze)
    # visuals.root.mainloop()
    
    if path:
        print("Paths found:")
        print(path)
        for agent in agents:
            agent_path = [step for step in path if step[0] == agent.name]
            total_time = level4.calculate_path_time(agent_path, maze)
            print(f"Agent {agent.name}:")
            print(f"  Path: {agent_path}")
            print(f"  Total time: {total_time}")
            print(f"  Within time limit: {'Yes' if total_time <= agent.time_limit else 'No'}")

        # Plot the maze and paths
        # level4.plot_maze(maze, path, agents)
        visuals.draw_path_turn_based(path)
        
        # visuals.root.mainloop()
    else:
        print("No path found for at least one agent.")