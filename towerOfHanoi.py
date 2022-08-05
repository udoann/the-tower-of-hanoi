"""THE TOWER OF HANOI, by Nnaemeka Nwankwo usmekuzee93@gmail.com
A stack-moving puzzle game."""

import copy
import sys

TOTAL_DISKS = 5  #more disk means a more difficult puzzle.

#start with all disks on tower A:
SOLVED_TOWER = list(range(TOTAL_DISKS,0,-1))
def main():
    """Runs a single game of the Tower of Hanoi."""
    print(
        """THE TOWER OF HANOI, by Nnaemeka Nwankwo usmekuzee93@gmail.com
        Move the tower of disks, one disks at a time, to another tower. Larger 
        disks cannot rest on top of a smaller disk.
        
        More info at https://en wikipediaorg/wiki/tower_of_hanoi
        """
    )
    """The towers dictionary has keys "A", "B", "C", and values
    that are lists representing a tower of disks. The list contains
    integers representing disks of different sizes, and the start of 
    the list is the bottom of the tower. For a game with 5 disks,
    list [5,4,3,2,1] represents a completed tower. The blank
    list [] represents a tower of no disk. the list [1.3] has a 
    larger disk on top of a smaller disk and is an invalid
    confuguration. The list [3,1] is allowed since smaller disks
    can go on top of larger ones. """
    towers = {"A":copy.copy(SOLVED_TOWER),"B":[], "C":[]}

    while True:  # Run a single turn on each iteration of this loop.
        # Display the towers and disk:
        displayTower(towers)

        # Ask the user for a move:
        fromTower, toTower = getPlayerMove(towers)

        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)
        
        # Check if the user has solved the puzzle:
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTower(towers)  # display the towers one last time.
            print("You have solved the puzzle! well done!")
            sys.exit()
def getPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""
    while True:
        print(" Enter the letters of 'from'  and 'to' towers, or QUIT.")
        print("(e.g., AB to moves a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing")
            sys.exit()

        # MAke sure the user entered valid tower letters:
        if response not in ("AB","AC","BA","BC","CA","CB"):
            print("Enter one of AB, AC, BA, BC, CA, OR CB.")
            continue # ask player again for their move.

        # Use a more descriptive Varaible names:
        fromTower, toTower = response[0],response[1]

        if len(towers[fromTower]) == 0:
            # the "from" tower cannot be an empty tower:
            print("You selected a tower with no disks.")
            continue  # Ask player again for their move.
        elif len(towers[toTower]) == 0:
            # Any disk can be moved onto an empty "to" tower:
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("can't put larger disks on top of smaller ones.")
            continue # Ask player again for their move.
        else:
            # this is a valid move, so return the selected towers:
            return fromTower,toTower

def displayTower(towers):
    """Display the three towers with their disks."""

    # display the three towers:
    for level in range(TOTAL_DISKS,-1,-1):
        for tower in (towers["A"],towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0) # Display the bare pole with no disk.
            else:
                displayDisk(tower[level])  # Display the disk.
        print()

    # Display the tower labels A, B, and C:
    empty_space = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))

def displayDisk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{empty_space}||{empty_space}",end="")
    else:
        # display the disk:
        disk = "@" * width
        num_label = str(width).rjust(2,"_")
        print(f"{empty_space}{disk}{num_label}{disk}{empty_space}", end="")

if __name__ == "__main__":
    main()