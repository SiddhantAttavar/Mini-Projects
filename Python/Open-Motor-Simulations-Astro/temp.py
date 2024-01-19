from motorlib import motor, grains, propellant
from motorlib.units import convert
import pprint

printer = pprint.PrettyPrinter(indent = 4)

bates_grain = grains.BatesGrain()
bates_grain.setProperties({
	'diameter': convert(0.024, 'm', 'in'),
	'length': convert(0.095, 'm', 'in'),
	'coreDiameter': convert(0.012, 'm', 'in'),
	'inhibitedEnds': 'Top',
})

sim_motor = motor.Motor()
sim_motor_config = motor.MotorConfig()
sim_motor.grains.append(bates_grain)
bates_grain.simulationSetup(sim_motor_config)

sim_motor.nozzle.setProperties({
	'throat': convert(0.012, 'm', 'in'),
	'throatLength': 0,
	'exit': convert(0.014476875, 'm', 'in'),
	'efficiency': 1,
	'divAngle': 15,
	'convAngle': 45,
	'slagCoeff': 0,
	'erosionCoeff': 0,
})

sim_motor.propellant = propellant.Propellant()
sim_motor.propellant.setProperties({
	'name': 'KNDX',
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

# print(printer.pprint(sim_motor.getDict()))

sim_res = sim_motor.runSimulation()
assert sim_res != None
print(sim_res.channels['time'].getData())
with open('out.csv', 'w') as out_file:
	out_file.write(sim_res.getCSV())
