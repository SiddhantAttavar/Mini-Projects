from motorlib import motor, grains, propellant
import pprint

printer = pprint.PrettyPrinter(indent = 4)

bates_grain = grains.BatesGrain()
bates_grain.setProperties({
	'diameter': 0.024,
	'length': 0.095,
	'coreDiameter': 0.012,
	'inhibitedEnds': 'Top',
})

sim_motor = motor.Motor()
sim_motor_config = motor.MotorConfig()
sim_motor.grains.append(bates_grain)
bates_grain.simulationSetup(sim_motor_config)

sim_motor.nozzle.setProperties({
	'throat': 0.012,
	'throatLength': 0,
	'exit': 0.014476875,
	'efficiency': 1,
	'divAngle': 15,
	'convAngle': 45,
	'slagCoeff': 0,
	'erosionCoeff': 0,
})

sim_motor.propellant = propellant.Propellant()
sim_motor.propellant.setProperties({
	'name': 'Naka - KNDX',
	'density': 1785,
	'tabs': [{
		'a': 1.0537671694797537e-05,
		'k': 1.1308,
		'm': 42.39,
		'maxPressure': 11204375.0,
		'minPressure': 8501535.0,
		'n': 0.444,
		't': 1625.0
	}]
})

print(printer.pprint(sim_motor.getDict()))

sim_res = sim_motor.runSimulation()
with open('out.csv', 'w') as out_file:
	out_file.write(sim_res.getCSV())
