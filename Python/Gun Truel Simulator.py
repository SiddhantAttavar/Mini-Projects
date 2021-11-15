skill = [1, 2, 3]
probability = [0, 0, 0]

def solve(currChance, people, turn, recursionDepth, skipNumber):
	if recursionDepth == 15 or skipNumber == len(people):
		return

	if len(people) == 2:
		#Shoot at the next person
		#Hit the person
		probability[turn] += skill[turn] / 6 * currChance
		
		#Miss the person
		solve((3 - skill[turn]) / 6 * currChance, people, (turn + 1) % 2, recursionDepth + 1, 0)

		#Don't Shoot
		solve(currChance / 2, people, (turn + 1) % 2, recursionDepth + 1, skipNumber + 1)
	else:
		#Shoot at the next person
		#Hit the person
		peopleA = people.copy()
		peopleA.pop((turn + 1) % 3)
		solve(skill[turn] / 9 * currChance, peopleA, (turn + 2) % 3, recursionDepth + 1, 0)

		#Miss the person
		solve((3 - skill[turn]) / 9 * currChance, people, (turn + 1) % 3, recursionDepth + 1, 0)

		#Shoot at the next to next person
		#Hit the person
		peopleB = people.copy()
		peopleB.pop((turn + 2) % 3)
		solve(skill[turn] / 9 * currChance, peopleB, (turn + 1) % 3, recursionDepth + 1, 0)

		#Miss the person
		solve((3 - skill[turn]) / 9 * currChance, people, (turn + 1) % 3, recursionDepth + 1, 0)

		#Don't Shoot
		solve(currChance / 3, people, (turn + 1) % 3, recursionDepth + 1, skipNumber + 1)

solve(1, [0, 1, 2], 0, 0, 0)
print(f'{probability[0] * 100:.2f}% {probability[1] * 100:.2f}% {probability[2] * 100:.2f}%')