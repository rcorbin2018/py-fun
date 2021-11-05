class TowersOfHanoi:

    def __init__(self):
        self.numberOfDisks = 3
        self.disklist = [disk+1 for disk in range(self.numberOfDisks)]
        self.roddictionary = {"fromTower":self.disklist, "extraTower":[], "toTower":[]}

    def move_disks(self,numberOfDisks,fromTower,toTower,extraTower):
        if(numberOfDisks == 1):
            towers_of_hanoi.update_tower_dictionary(fromTower,toTower)
        else:
            towers_of_hanoi.move_disks(numberOfDisks - 1, fromTower, extraTower, toTower)
            towers_of_hanoi.move_disks(1, fromTower, toTower, extraTower)
            towers_of_hanoi.move_disks(numberOfDisks - 1, extraTower, toTower, fromTower)

    def update_tower_dictionary(self,fromTower,toTower):
        smallestdiskfromrod1 = min(self.roddictionary[fromTower])
        self.roddictionary[fromTower].remove(smallestdiskfromrod1)
        self.roddictionary[fromTower] = self.roddictionary[fromTower]
        self.roddictionary[toTower].insert(0,smallestdiskfromrod1)
        towers_of_hanoi.print_current_board()

    def print_current_board(self):
        line = []
        for key in self.roddictionary:
            line.append((key, self.roddictionary[key]))
        print (line) 


if __name__ == '__main__':
    print("*****Welcome to the Towers of Hanoi!***********************")
    towers_of_hanoi = TowersOfHanoi()
    towers_of_hanoi.print_current_board()
    towers_of_hanoi.move_disks(towers_of_hanoi.numberOfDisks, 'fromTower', 'toTower', 'extraTower')
    print("*****Towers of Hanoi have spoken****************************")
