import spade
from spade.agent import Agent
from spade.behaviour import *
from time import sleep
import random
import json

HEIGHT = 10
WIDTH = HEIGHT
LABYRINTH = []

def generate_labyrinth(height, width, character):
    labyrinth = []
    for row in range(height):
        new_row = []
        for element in range(width):
            new_row.append(character)

        labyrinth.append(new_row)

    return labyrinth

def get_labyrinth():
    height = HEIGHT
    width = WIDTH
    starting_character = 'X'
    empty_character = 'O'
    wall_character = 'I'
    start_labyrinth = generate_labyrinth(height, width, starting_character)

    starting_point_height = random.randint(1, height - 2)
    starting_point_width = random.randint(1, width - 2)

    start_labyrinth[starting_point_height][starting_point_width] = empty_character

    walls = []
    walls.append([starting_point_height-1, starting_point_width])
    walls.append([starting_point_height, starting_point_width-1])
    walls.append([starting_point_height, starting_point_width+1])
    walls.append([starting_point_height+1, starting_point_width])

    start_labyrinth[starting_point_height-1][starting_point_width] = wall_character
    start_labyrinth[starting_point_height][starting_point_width-1] = wall_character
    start_labyrinth[starting_point_height][starting_point_width+1] = wall_character
    start_labyrinth[starting_point_height+1][starting_point_width] = wall_character

    while walls:
        random_wall = random.choice(walls)
        rw_height = random_wall[0]
        rw_width = random_wall[1]

        if rw_width != 0:
            if start_labyrinth[rw_height][rw_width - 1] == starting_character and start_labyrinth[rw_height][rw_width - 1] == empty_character:
                number_surrounding_cells = count_surrounding_cells(start_labyrinth, random_wall, empty_character)

                if number_surrounding_cells < 2:
                    start_labyrinth[rw_height][rw_width] = empty_character

                    if rw_height != 0:
                        if start_labyrinth[rw_height - 1][rw_width] != empty_character:
                            start_labyrinth[rw_height - 1][rw_width] = wall_character
                        if [rw_height - 1, rw_width] not in walls:
                            walls.append([rw_height - 1, rw_width])

                    if rw_height != height - 1:
                        if start_labyrinth[rw_height + 1][rw_width] != empty_character:
                            start_labyrinth[rw_height + 1][rw_width] = wall_character
                        if [rw_height + 1, rw_width] not in walls:
                            walls.append([rw_height + 1, rw_width])

                    if rw_width != 0:
                        if start_labyrinth[rw_height][rw_width - 1] != empty_character:
                            start_labyrinth[rw_height][rw_width - 1] = wall_character
                        if [rw_height, rw_width - 1] not in walls:
                            walls.append([rw_height, rw_width - 1])
                
                for wall in walls:
                    if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                        walls.remove(wall)
                continue


        if rw_height != 0:
            if start_labyrinth[rw_height - 1][rw_width] == starting_character and start_labyrinth[rw_height + 1][rw_width] == empty_character:
                number_surrounding_cells = count_surrounding_cells(start_labyrinth, random_wall, empty_character)

                if number_surrounding_cells < 2:
                    start_labyrinth[rw_height][rw_width] = empty_character

                    if rw_height != 0:
                        if start_labyrinth[rw_height - 1][rw_width] != empty_character:
                            start_labyrinth[rw_height - 1][rw_width] = wall_character
                        if [rw_height - 1, rw_width] not in walls:
                            walls.append([rw_height - 1, rw_width])

                    if rw_width != 0:
                        if start_labyrinth[rw_height][rw_width - 1] != empty_character:
                            start_labyrinth[rw_height][rw_width - 1] = wall_character
                        if [rw_height, rw_width - 1] not in walls:
                            walls.append([rw_height, rw_width - 1])

                    if rw_width != width - 1:
                        if start_labyrinth[rw_height][rw_width + 1] != empty_character:
                            start_labyrinth[rw_height][rw_width + 1] = wall_character
                        if [rw_height, rw_width + 1] not in walls:
                            walls.append([rw_height, rw_width + 1])
                
                for wall in walls:
                    if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                        walls.remove(wall)
                continue

        if rw_height != height - 1:
            if start_labyrinth[rw_height + 1][rw_width] == starting_character and start_labyrinth[rw_height - 1][rw_width] == empty_character:
                number_surrounding_cells = count_surrounding_cells(start_labyrinth, random_wall, empty_character)

                if number_surrounding_cells < 2:
                    start_labyrinth[rw_height][rw_width] = empty_character

                    if rw_height != height - 1:
                        if start_labyrinth[rw_height + 1][rw_width] != empty_character:
                            start_labyrinth[rw_height + 1][rw_width] = wall_character
                        if [rw_height + 1, rw_width] not in walls:
                            walls.append([rw_height + 1, rw_width])

                    if rw_width != 0:
                        if start_labyrinth[rw_height][rw_width - 1] != empty_character:
                            start_labyrinth[rw_height][rw_width - 1] = wall_character
                        if [rw_height, rw_width - 1] not in walls:
                            walls.append([rw_height, rw_width - 1])

                    if rw_width != width - 1:
                        if start_labyrinth[rw_height][rw_width + 1] != empty_character:
                            start_labyrinth[rw_height][rw_width + 1] = wall_character
                        if [rw_height, rw_width + 1] not in walls:
                            walls.append([rw_height, rw_width + 1])
                
                for wall in walls:
                    if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                        walls.remove(wall)
                continue

        if rw_width != width - 1:
            if start_labyrinth[rw_height][rw_width + 1] == starting_character and start_labyrinth[rw_height][rw_width - 1] == empty_character:
                number_surrounding_cells = count_surrounding_cells(start_labyrinth, random_wall, empty_character)

                if number_surrounding_cells < 2:
                    start_labyrinth[rw_height][rw_width] = empty_character

                    if rw_width != width - 1:
                        if start_labyrinth[rw_height][rw_width + 1] != empty_character:
                            start_labyrinth[rw_height][rw_width + 1] = wall_character
                        if [rw_height, rw_width + 1] not in walls:
                            walls.append([rw_height, rw_width + 1])

                    if rw_height != height - 1:
                        if start_labyrinth[rw_height + 1][rw_width] != empty_character:
                            start_labyrinth[rw_height + 1][rw_width] = wall_character
                        if [rw_height + 1, rw_width] not in walls:
                            walls.append([rw_height + 1, rw_width])

                    if rw_height != 0:
                        if start_labyrinth[rw_height - 1][rw_width] != empty_character:
                            start_labyrinth[rw_height - 1][rw_width] = wall_character
                        if [rw_height - 1, rw_width] not in walls:
                            walls.append([rw_height - 1, rw_width])
                
                for wall in walls:
                    if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                        walls.remove(wall)
                continue

        for wall in walls:
                    if (wall[0] == random_wall[0] and wall[1] == random_wall[1]):
                        walls.remove(wall)


    #Sve preostale u zidove
    for i in range(height):
        for j in range(width):
            if start_labyrinth[i][j] == starting_character:
                start_labyrinth[i][j] = wall_character

    #Ulaz
    for i in range(width):
        if start_labyrinth[1][i] == empty_character:
            #start_labyrinth[0][i] = empty_character
            start_labyrinth[0][i] = 'U'
            break

    #Izlaz
    for i in range(width - 1, 0, -1):
        if start_labyrinth[height - 2][i] == empty_character:
            #start_labyrinth[height - 1][i] = empty_character
            start_labyrinth[height - 1][i] = "E"
            break

        
    return start_labyrinth

def print_labyrinth(labyrinth):
    for i in range(len(labyrinth)):
        print(labyrinth[i])
    print()
    return

def count_surrounding_cells(labyrnith, random_wall, character):
    cell_count = 0
    rw_height = random_wall[0]
    rw_width = random_wall[1]

    if labyrnith[rw_height - 1][rw_width] == character:
        cell_count += 1
    if labyrnith[rw_height + 1][rw_width] == character:
        cell_count += 1
    if labyrnith[rw_height][rw_width - 1] == character:
        cell_count += 1
    if labyrnith[rw_height][rw_width + 1] == character:
        cell_count += 1

    return cell_count

LABYRINTH = get_labyrinth()
print_labyrinth(LABYRINTH)


def remove_visited_indices(old_available_indices, visited_indices):
    
    available_indices = [x for x in old_available_indices if x not in visited_indices]

    return available_indices


def look_around(index_string):
    
    vision = [['Z','Z','Z'],['Z','Z','Z'],['Z','Z','Z']]
    split_index = index_string.split("-")
    index_row = int(split_index[0])
    index_column = int(split_index[1])

    vision[1][1] = index_string

    if index_row - 1 >= 0:
        vision[0][1] = LABYRINTH[index_row - 1][index_column]

    if index_row + 1 < HEIGHT:
        vision[2][1] = LABYRINTH[index_row + 1][index_column]

    if  index_column - 1 >= 0:
        vision[1][0] = LABYRINTH[index_row][index_column - 1]
    
    if  index_column + 1 < WIDTH:
        vision[1][2] = LABYRINTH[index_row][index_column + 1]

    return vision


class ExplorerAgent(Agent):
    class ExploreLocationBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=100)
            if msg:
                next_location = msg.body
                vision = look_around(next_location)

                msg = spade.message.Message(
                    to = "mojagent1@jabbers.one",
                    body = json.dumps(vision),
                    )
                await self.send(msg)
                
            else:
                print(f"{self.agent.name}: Didn't recieve a response!")

    async def setup(self):
        print(f"{self.name}: Starting!")

        exploreLocationBehaviour = self.ExploreLocationBehaviour()
        self.add_behaviour(exploreLocationBehaviour)

class SupervisorAgent(Agent):

    class SendAgentBehaviour(PeriodicBehaviour):
        async def run(self):
            possible_agents = ["mojagent2@jabbers.one", "mojagent3@jabbers.one"]
            chosen_agent = random.choice(possible_agents)

            self.agent.available_indices = remove_visited_indices(self.agent.available_indices, self.agent.visited_indices)
            print(self.agent.available_indices)
            next_location = random.choice(self.agent.available_indices)
            self.agent.visited_indices.append(next_location)

            msg = spade.message.Message(
                to = chosen_agent,
                body = next_location,
                )

            await self.send(msg)
                
    class ReceiveVisionBehaviour(CyclicBehaviour):
        async def run(self):
            msg = await self.receive(timeout=100)
            if msg:
                new_vision = json.loads(msg.body)

                visited_location = new_vision[1][1]
                split_index = visited_location.split("-")
                index_row = int(split_index[0])
                index_column = int(split_index[1])

                if new_vision [0][1] != 'Z':
                    self.agent.labyrinth[index_row - 1][index_column] = new_vision [0][1]
                
                if new_vision [2][1] != 'Z':
                    self.agent.labyrinth[index_row + 1][index_column] = new_vision [2][1]
                
                if new_vision [1][0] != 'Z':
                    self.agent.labyrinth[index_row][index_column - 1] = new_vision [1][0]

                if new_vision [1][2] != 'Z':
                    self.agent.labyrinth[index_row][index_column + 1] = new_vision [1][2]

                print()
                print_labyrinth(self.agent.labyrinth)
                
                if new_vision [0][1] == 'E' or new_vision [2][1] == 'E' or new_vision [1][0] == 'E' or new_vision [1][2] == 'E':
                    
                    print("Pronaden je izlaz!!!")
                    quit()


                if new_vision [0][1] == 'O':
                    index_empty_row = index_row - 1
                    index_empty_column = index_column
                    new_empty_location = str(index_empty_row) + '-' + str(index_empty_column)
                    self.agent.available_indices.append(new_empty_location)
                
                if new_vision [2][1] == 'O':
                    index_empty_row = index_row + 1
                    index_empty_column = index_column
                    new_empty_location = str(index_empty_row) + '-' + str(index_empty_column)
                    self.agent.available_indices.append(new_empty_location)
                
                if new_vision [1][0] == 'O':
                    index_empty_row = index_row 
                    index_empty_column = index_column - 1
                    new_empty_location = str(index_empty_row) + '-' + str(index_empty_column)
                    self.agent.available_indices.append(new_empty_location)

                if new_vision [1][2] == 'O':
                    index_empty_row = index_row 
                    index_empty_column = index_column + 1
                    new_empty_location = str(index_empty_row) + '-' + str(index_empty_column)
                    self.agent.available_indices.append(new_empty_location)

                
            else:
                print(f"{self.agent.name}: Didn't recieve a response!")

    async def setup(self):
        self.labyrinth = generate_labyrinth(HEIGHT, WIDTH, 'X')
        print(f"{self.name}: Starting!")

        self.visited_indices = []
        self.available_indices = []
        
        for index, cell in enumerate(LABYRINTH[0]):
            if cell == 'U':
                entrance_index = '0' + '-' + str(index)
                self.available_indices.append(entrance_index)
                self.labyrinth[0][index] = 'U'
        
        sendAgentBehaviour = self.SendAgentBehaviour(1)
        receiveVisionBehaviour = self.ReceiveVisionBehaviour()

        self.add_behaviour(sendAgentBehaviour)
        self.add_behaviour(receiveVisionBehaviour)

def main():

    agent1 = SupervisorAgent("mojagent1@jabbers.one", "agentlozinka")
    agent2 = ExplorerAgent("mojagent2@jabbers.one", "agentlozinka")
    agent3 = ExplorerAgent("mojagent3@jabbers.one", "agentlozinka")

    agent2.start()
    agent3.start()
    sleep(3)
    agent1.start()

    input("Press ENTER to exit.\n")

    agent1.stop()
    agent2.stop()
    agent3.stop()

    spade.quit_spade()

    return

if __name__ == '__main__':

    main()