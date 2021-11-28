"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (Le., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using Stacks.

1)
D
DD
DDD     --     --

2)
        D
DDD     DD     --

3)
        D
--      DD     DDD

4)
D       DD     DDD

5)
               DD
D       --     DDD

6)
               D
               DD
--      --     DDD
"""


def towers_of_hanoi(disks, origin='Origin', buffer='Buffer', destination='Destination'):
    if not disks:
        return

    # move top n - 1 disks from orIgIn to buffer, using destination as a buffer.
    towers_of_hanoi(disks - 1, origin, destination, buffer)

    # move top from origin to destination
    print(f'Moving Top disk from {origin} to {destination}')
    
    # move top n - 1 disks from buffer to destination, using origin as a buffer.
    towers_of_hanoi(disks - 1, buffer, origin, destination)
