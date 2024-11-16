
print("This program allows you to calculate some functions in physics:")
print("")

def calculate_acceleration(final_velocity,initial_velocity,time_taken):
  acceleration = (final_velocity - initial_velocity) / time_taken
  return acceleration

def calculate_velocity(initial_velocity, acceleration, time):
  final_velocity = initial_velocity + acceleration * time
  return final_velocity

def calculate_kinetic_energy(mass, velocity):
  kinetic_energy = 0.5 * mass * velocity**2
  return kinetic_energy

def calculate_potential_energy(mass, gravity, height):
  potential_energy = mass * gravity * height
  return potential_energy

def calculate_work_done(force, displacement):
  work_done = force * displacement
  return work_done
  
print("")
print("1. Acceleration")
print("2. Final Velocity")
print("3. Kinetic Energy")
print("4. Potential Energy")
print("5. Work Done")
print("")
print("Type the option for the physics function (1-5): ")
reply = int(input())


if reply == 1:
  print("ACCELERATION")
  print("Input the value for final velocity:")
  final_velocity = int(input())
  print("Input the value for initial velocity:")
  initial_velocity = int(input())
  print("Input the value for time taken:")
  time_taken = int(input())
  acceleration = calculate_acceleration(final_velocity, initial_velocity, time_taken)
  print("Acceleration:", acceleration, "m")

if reply == 2:
  print("FINAL VELOCITY")
  print("")
  print("Input the value for initial velocity (u):")
  initial_velocity = int(input())
  print("Input the value for acceleration (a):")
  acceleration = int(input())
  print("Input the value for time (t):")
  time = int(input())
  final_velocity = calculate_velocity(initial_velocity, acceleration, time)
  print("Final Velocity:", final_velocity, "m/s")

if reply == 3:
  print("KINETIC ENERGY")
  print("")
  print("Input the value for mass (m):")
  mass = int(input())
  print("Input the value for final velocity (v):")
  final_velocity = int(input())
  kinetic_energy = calculate_kinetic_energy(mass, final_velocity)
  print("Kinetic Energy:", kinetic_energy, "J")

if reply == 4:
  print("POTENTIAL ENERGY")
  print("")
  print("Input the value for mass (m):")
  mass = int(input())
  print("Input the value for gravity (g):")
  gravity = int(input())
  print(("Input the value for height (h):"))
  height = float(input())
  potential_energy = calculate_potential_energy(mass, gravity, height)
  print("Potential Energy:", potential_energy, "J")

if reply == 5:
  print("WORK DONE")
  print("")
  print("Input the value for force (F):")
  force = int(input())
  print("Input the value for displacement (D):")
  displacement = float(input())
  work_done = calculate_work_done(force, displacement)
  print("Work Done:", work_done, "J")





