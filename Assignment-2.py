class Car:
	def __init__(self,color='Black', max_speed=0, acceleration=0, tyre_friction=0):
		self._color = color
		self._max_speed = max_speed
		self._acceleration = acceleration
		self._tyre_friction = tyre_friction
		self._is_engine_started = False
		self._current_speed = 0

		self.check_valid(max_speed,'max_speed')
		self.check_valid(acceleration,'acceleration')
		self.check_valid(tyre_friction,'tyre_friction')

	@staticmethod
	def check_valid(valid,attribute):
		try:
			if valid >= 0:
				pass
			else:
				raise ValueError
		except ValueError:
			raise ValueError('Invalid value for {}'.format(attribute))

	@property
	def color(self):
		return self._color

	@property
	def max_speed(self):
		return self._max_speed

	@property
	def acceleration(self):
		return self._acceleration

	@property
	def tyre_friction(self):
		return self._tyre_friction

	@property
	def is_engine_started(self):
		return self._is_engine_started

	@property
	def current_speed(self):
		return self._current_speed

	def start_engine(self):
		self._is_engine_started = True

	def stop_engine(self):
		self._is_engine_started = False

	def accelerate(self):
		if self.is_engine_started == True:
			if self._current_speed+self.acceleration >= self.max_speed:
				self._current_speed = self.max_speed
			else:
				self._current_speed += self.acceleration
		else:
			print('Start the engine to accelerate')

	def apply_brakes(self):
		if self._current_speed-self.tyre_friction >= 0:
			self._current_speed -= self.tyre_friction
		else:
			self._current_speed = 0

	def sound_horn(self):
		if self._is_engine_started == True:
			print('Beep Beep')
		else:
			print('Start the engine to sound_horn')

class Truck(Car):
	def __init__(self, color="Red", max_speed=0, acceleration=0, tyre_friction=0, max_cargo_weight=0):
		super().__init__(color, max_speed, acceleration, tyre_friction)
		self._max_cargo_weight = max_cargo_weight
		self._is_engine_started = False
		self.init_load = 0 
		if max_cargo_weight < 0:
			raise ValueError('Invalid value for max_cargo_weight')

	@property
	def max_cargo_weight(self):
		return self._max_cargo_weight
	
	@property
	def is_engine_started(self):
		return self._is_engine_started


	def sound_horn(self):
		if self._is_engine_started == True:
			print('Honk Honk')
		else:
			print('Start the engine to sound_horn')

	def load(self,weight):
		if weight<0:
			raise ValueError('Invalid value for cargo_weight')
		else:
			if (self._is_engine_started == False or self.is_engine_started==True) and self._current_speed == 0 and self.init_load+weight <= self._max_cargo_weight :
				self.init_load += weight
			elif self.init_load+weight > self._max_cargo_weight:
				print(f'Cannot load cargo more than max limit: {self._max_cargo_weight}')
			else:
				print('Cannot load cargo during motion')
			
	def unload(self,weight):
		if weight<0:
			raise ValueError('Invalid value for cargo_weight')
		else:
			if (self._is_engine_started == False or self._is_engine_started == True) and self._current_speed == 0 :
				self.init_load -= weight
			else:
				print('Cannot unload cargo during motion')
